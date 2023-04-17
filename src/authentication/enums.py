from django.db import models


class Role(models.TextChoices):
    admin = "admin", "Администратор"
    staff = "staff", "Модератор"
    user = "user", "Пользователь"
