from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .utils import send_invitation_email

class UserAdmin(admin.ModelAdmin):
    actions = ['invite_new_user']

    def invite_new_user(self, request, queryset):
        for user in queryset:
            # Send invitation email to the selected user
            send_invitation_email(user.email, request)
            messages.success(request, f'Invitation sent to {user.email}')

    invite_new_user.short_description = "Send registration invite email to selected user(s)"

# Unregister the default User model and register the custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
