import os
import django

# SET SETTINGS MODULE FIRST
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

# SETUP DJANGO
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

try:
    if username and password:
        user, created = User.objects.get_or_create(username=username)

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        if created:
            print("Superuser created")
        else:
            print("Superuser already exists, password updated")
    else:
        print("Missing environment variables")

except Exception as e:
    print("Error creating superuser:", e)