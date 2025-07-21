from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from .models import Recipient
from .forms import RecipientForm
from django.db.models import Q

class RecipientCreateView(SuccessMessageMixin, CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'recipient_form.html'
    success_url = reverse_lazy('recipient_list')
    success_message = "Your request has been submitted successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Request for a Blood'
        return context

class RecipientUpdateView(SuccessMessageMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'recipient_form.html'
    success_url = reverse_lazy('recipient_list')
    success_message = "Your request has been updated successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Blood Request'
        return context

from django.http import JsonResponse

class RecipientListView(ListView):
    model = Recipient
    template_name = 'recipient_list.html'
    context_object_name = 'recipients'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(hospital_name__icontains=query) | Q(blood_group__icontains=query)
            )
        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            recipients_data = []
            for recipient in context['recipients']:
                recipients_data.append({
                    'id': recipient.id,
                    'patient_name': recipient.patient_name,
                    'blood_group': recipient.blood_group,
                    'hospital_name': recipient.hospital_name,
                    'contact_number': recipient.contact_number,
                    'required_date': recipient.required_date.strftime('%B %d, %Y'),
                    'is_fulfilled': recipient.is_fulfilled,
                })
            return JsonResponse({'recipients': recipients_data})
        return super().render_to_response(context, **response_kwargs)

class RecipientToggleStatusView(View):
    def get(self, request, pk):
        recipient = get_object_or_404(Recipient, pk=pk)
        recipient.is_fulfilled = not recipient.is_fulfilled
        recipient.save()
        return redirect('recipient_list')
