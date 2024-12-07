from django.contrib import admin
from .models import Task, GoogleOAuthKey
# Register your models here.
admin.site.register(Task)
admin.site.register(GoogleOAuthKey)