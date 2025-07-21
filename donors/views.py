from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Donor
from .forms import DonorForm
from django.db.models import Q

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
