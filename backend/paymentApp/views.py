from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from django.conf import settings
import stripe

# Use Stripe secret key from settings
stripe.api_key = settings.STRIPE_SECRET_KEY

class ScanProductView(APIView):
    def post(self, request):
        barcode = request.data.get("barcode")
        
        if not barcode:
            return Response({"error": "Barcode is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the product from the database based on the barcode
        product = Product.objects.filter(barcode=barcode).first()
        
        if product:
            return Response({
                "name": product.name,
                "price": str(product.price),
            })
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class CreatePaymentIntent(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        
        if not amount:
            return Response({"error": "Amount is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = float(amount) * 100  # Convert to cents
        except ValueError:
            return Response({"error": "Invalid amount format"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a PaymentIntent with Stripe
            intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency='usd',
            )
            return Response({"client_secret": intent.client_secret}, status=status.HTTP_201_CREATED)
        except stripe.error.StripeError as e:
            # Handle Stripe API errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
