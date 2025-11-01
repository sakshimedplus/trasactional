from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'transaction_id',
            'source_account',
            'destination_account',
            'amount',
            'currency',
            'status',
            'created_at',
            'processed_at',
        ]
        read_only_fields = ['status', 'created_at', 'processed_at']