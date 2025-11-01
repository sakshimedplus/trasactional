# ...existing code...
from celery import shared_task
import time
from django.db import transaction as db_transaction
from django.utils import timezone
from .models import Transaction

@shared_task(bind=True)
def process_transaction(self, transaction_id):
    """
    Idempotent background processing:
    - Uses select_for_update inside transactions to avoid concurrent processing.
    - Simulates external call with a 30s sleep.
    - Updates status and processed_at on success.
    """
    try:
        # Acquire DB lock briefly to check status and prevent dup processing
        with db_transaction.atomic():
            tx = Transaction.objects.select_for_update().get(transaction_id=transaction_id)
            if tx.status == 'PROCESSED':
                return 'already_processed'
            # If status is PROCESSING or FAILED, we proceed (idempotency ensured by checks below)

        # Simulate external API call (30s)
        time.sleep(30)

        # Finalize processing
        with db_transaction.atomic():
            tx = Transaction.objects.select_for_update().get(transaction_id=transaction_id)
            # double-check to avoid race
            if tx.status != 'PROCESSED':
                tx.status = 'PROCESSED'
                tx.processed_at = timezone.now()
                tx.save()
        return 'processed'
    except Transaction.DoesNotExist:
        # nothing to do; webhook might not have created the DB row
        return 'not_found'
    except Exception as exc:
        # mark failed if possible, then re-raise to allow retry or inspect logs
        try:
            with db_transaction.atomic():
                tx = Transaction.objects.filter(transaction_id=transaction_id).first()
                if tx and tx.status != 'PROCESSED':
                    tx.status = 'FAILED'
                    tx.save()
        except Exception:
            pass
        raise exc