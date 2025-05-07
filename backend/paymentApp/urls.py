from django.urls import path
from .views import ScanProductView, CreatePaymentIntent

urlpatterns = [
    path('scan/', ScanProductView.as_view()),
    path('pay/', CreatePaymentIntent.as_view()),
]