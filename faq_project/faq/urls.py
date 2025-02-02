from django.urls import path
from .views import FAQListView, FAQDetailView  # Ensure FAQDetailView is imported

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),  # Add this
]
