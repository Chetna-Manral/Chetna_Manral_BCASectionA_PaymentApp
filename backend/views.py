from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from django.conf import settings
import stripe

stripe.api_key = 'your_stripe_secret_key'

class ScanProductView(APIView):
    def post(self, request):
        barcode = request.data.get("barcode")
        product = Product.objects.filter(barcode=barcode).first()
        if product:
            return Response({
                "name": product.name,
                "price": str(product.price),
            })
        return Response({"error": "Product not found"}, status=404)

class CreatePaymentIntent(APIView):
    def post(self, request):
        amount = float(request.data.get("amount")) * 100  # convert to cents
        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency='usd',
        )
        return Response({"client_secret": intent.client_secret})
