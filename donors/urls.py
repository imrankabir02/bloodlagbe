from django.urls import path
from .views import DonorCreateView, DonorListView, DonorUpdateView, DonorToggleStatusView, LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('register/', DonorCreateView.as_view(), name='donor_create'),
    path('list/', DonorListView.as_view(), name='donor_list'),
    path('<int:pk>/update/', DonorUpdateView.as_view(), name='donor_update'),
    path('<int:pk>/toggle-status/', DonorToggleStatusView.as_view(), name='donor_toggle_status'),
]
