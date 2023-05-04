from django.contrib import admin

from authentication.models import User
from core_app.models import ActorProfile

admin.site.register(User)
admin.site.register(ActorProfile)
