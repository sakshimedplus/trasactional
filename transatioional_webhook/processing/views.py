# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.utils import timezone
from .models import Transaction
from .serializers import TransactionSerializer
from .tasks import process_transaction
from django.shortcuts import get_object_or_404


class WebhookView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        transaction_id = data['transaction_id']
        transaction, created = Transaction.objects.get_or_create(
            transaction_id=transaction_id,
            defaults={
                'source_account': data.get('source_account'),
                'destination_account': data.get('destination_account'),
                'amount': data.get('amount'),
                'currency': data.get('currency'),
                'status': 'PROCESSING',
            }
        )

        if created:
            # enqueue background processing (non-blocking)
            process_transaction.delay(transaction_id)

        # immediate acknowledgement
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def health_check(request):
    return Response({
        'status': 'HEALTHY',
        'current_time': timezone.now().isoformat()
    })

@api_view(['GET'])
def get_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)