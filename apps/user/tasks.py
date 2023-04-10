from celery import shared_task
import datetime
from django.utils import timezone
import uuid
from .models import User, EmailVerification
from portfolio.celery import app

@shared_task
def send_verification_email(user_id):
    user = User.objects.get(id=user_id)
    expiration = timezone.now() + datetime.timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()

# app.autodiscover_tasks()
