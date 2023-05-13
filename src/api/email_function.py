from django.core.mail import send_mail
from django.conf import settings


def send_forget_password_mail(email, token):
    subject = "Ваша ссылка для восстановления пароля"
    message = (
        f"Здравствуйте, нажми здесь, если вы хотите восстановить пароль {settings.API_LINK}/changePassword/{token}/"
    )
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
