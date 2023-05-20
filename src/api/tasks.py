from celery import shared_task

from actorshere.celery import app
from core_app.models import Response, Notification, Casting, FavoritesCasting

from datetime import timedelta

from django.utils import timezone


# @shared_task
# def send_notification(response_id):
#     response = Response.objects.select_related('casting__casting_owner').get(id=response_id)
#     employer = response.casting.casting_owner
#     notification = Notification.objects.create(casting_owner=employer, text='New response received')
#     return notification


@shared_task
def check_casting_end_dates():
    current_time = timezone.now()
    current_time = current_time.date()
    end_date_threshold = current_time + timedelta(days=3)

    castings = Casting.objects.filter(end_of_application__lte=end_date_threshold)
    for casting in castings:
        favorites = FavoritesCasting.objects.filter(casting=casting)
        for favorite in favorites:
            user = favorite.user
            # Создаем уведомление
            notification = Notification.objects.create(
                owner=user,
                text=f"Кастинг '{casting.header}' заканчивается через 3 дня!",
            )

            # Отправляем уведомление пользователю
            # Здесь должен быть код для отправки уведомления (например, через Push-уведомления или электронную почту)
            # Можно использовать библиотеки, такие как Firebase Cloud Messaging (FCM) или SendGrid для этой цели

            # Помечаем уведомление как непрочитанное
            notification.is_read = False
            notification.save()
