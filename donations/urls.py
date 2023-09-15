from django.urls import path

from . import views

# url paths
urlpatterns = [
    path("", views.index, name="home"),
    path("payment-success/", views.payment_success, name="payment-success"),
    path("payment-failed/", views.payment_failed, name="payment-failed"),
]
