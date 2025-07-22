from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Donor
from recipients.models import Recipient
from .forms import DonorForm, CSVUploadForm
from .utils import normalize_donor_data
from django.db.models import Q, Count
import csv
import io

class DonorCreateView(SuccessMessageMixin, CreateView):
    model = Donor
    form_class = DonorForm
    template_name = 'donor_form.html'
    success_url = reverse_lazy('donor_list')
    success_message = "Thank you! You’re added to the life-saving donor list."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register as a Donor'
        return context

class DonorListView(ListView):
    model = Donor
    template_name = 'donor_list.html'
    context_object_name = 'donors'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(area__icontains=query) | Q(blood_group__icontains=query)
            )
        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            donors_data = []
            for donor in context['donors']:
                donors_data.append({
                    'id': donor.id,
                    'full_name': donor.full_name,
                    'blood_group': donor.blood_group,
                    'area': donor.area,
                    'phone_number': donor.phone_number,
                    'available': donor.available,
                    'last_donation_date': donor.last_donation_date.strftime('%B %d, %Y') if donor.last_donation_date else 'N/A'
                })
            return JsonResponse({'donors': donors_data})
        return super().render_to_response(context, **response_kwargs)

class DonorUpdateView(SuccessMessageMixin, UpdateView):
    model = Donor
    form_class = DonorForm
    template_name = 'donor_form.html'
    success_url = reverse_lazy('donor_list')
    success_message = "Your information has been updated successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Donor Information'
        return context

class DonorToggleStatusView(View):
    def get(self, request, pk):
        donor = get_object_or_404(Donor, pk=pk)
        donor.available = not donor.available
        donor.save()
        return redirect('donor_list')

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_requests'] = Recipient.objects.filter(is_fulfilled=False).count()
        context['fulfilled_requests'] = Recipient.objects.filter(is_fulfilled=True).count()
        context['available_donors'] = Donor.objects.filter(available=True).values('blood_group').annotate(count=Count('id'))
        return context

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)
            donor_data = list(reader)

            processed_data = normalize_donor_data(donor_data)

            for row in processed_data:
                Donor.objects.get_or_create(
                    full_name=row['full_name'],
                    phone_number=row['phone_number'],
                    blood_group=row['blood_group'],
                    area=row['area']
                )
            return redirect('donor_list')
    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})
