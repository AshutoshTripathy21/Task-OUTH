from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

class RegistrationInviteTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp)

invite_token_generator = RegistrationInviteTokenGenerator()

def send_invitation_email(user_email, request):
    uid = urlsafe_base64_encode(user_email.encode())
    token = invite_token_generator.make_token(user_email)

    registration_url = request.build_absolute_uri(f'/register/{uid}/{token}/')

    message = render_to_string('registration/invite_email.html', {
        'user_email': user_email,
        'registration_url': registration_url,
    })

    send_mail(
        'Invitation to Join Task Manager',
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
