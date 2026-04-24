import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    user, created = User.objects.get_or_create(username=username)

    # Always update password
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()

    if created:
        print("Superuser created")
    else:
        print("Superuser exists, password updated")
else:
    print("Missing username or password")