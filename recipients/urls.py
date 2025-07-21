from django.urls import path
from .views import RecipientCreateView, RecipientListView, RecipientUpdateView, RecipientToggleStatusView

urlpatterns = [
    path('request/', RecipientCreateView.as_view(), name='recipient_create'),
    path('requests/', RecipientListView.as_view(), name='recipient_list'),
    path('request/<int:pk>/update/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('request/<int:pk>/toggle-status/', RecipientToggleStatusView.as_view(), name='recipient_toggle_status'),
]
