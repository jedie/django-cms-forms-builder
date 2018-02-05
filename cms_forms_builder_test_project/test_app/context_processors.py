
import django
from django.contrib.auth import get_user_model


def debug_info(request):
    User = get_user_model()
    usernames = User.objects.filter(is_staff=True, is_active=True).values_list("username", flat=True)

    return {
        "django_version": django.__version__,
        "usernames": usernames,
    }
