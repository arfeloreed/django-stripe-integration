import stripe
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse

# global variables
stripe.api_key = settings.STRIPE_PRIVATE_KEY


# Create your views here.
# view route for home page
def index(request):
    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": "price_1NqXyoLgqjDd97XOYuOf5P5R",
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("payment-success"))
        + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse("payment-failed")),
    )

    return render(
        request,
        "donations/index.html",
        {
            "session_id": session.id,
            "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        },
    )


# view route for payment successful page
def payment_success(request):
    return render(
        request,
        "donations/payment-success.html",
    )


# view route for payment failed page
def payment_failed(request):
    return render(
        request,
        "donations/payment-failed.html",
    )
