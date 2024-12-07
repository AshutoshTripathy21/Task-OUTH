from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages

def user_register(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(email=uid)

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            messages.error(request, "Invalid or expired registration link.")
            return redirect('home')

        if request.method == "POST":
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')

        return render(request, 'registration/register.html', {'user': user})
    except Exception as e:
        messages.error(request, "Something went wrong.")
        return redirect('home')
