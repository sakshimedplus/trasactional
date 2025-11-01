from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check, name='health_check'),
    path('v1/webhooks/transactions', views.WebhookView.as_view(), name='webhook'),
    path('v1/transactions/<str:transaction_id>', views.get_transaction, name='get_transaction'),
]