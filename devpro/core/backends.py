from django.contrib.auth.backends import ModelBackend

from .models import User


class CpfBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return

        try:
            user = User.objects.get(cpf=username)
        except User.DoesNotExist:
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
