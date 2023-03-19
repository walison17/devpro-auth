from django.views.generic import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm


@login_required
def dashboard(request):
    return HttpResponse(f'Bem-vindo {request.user}')


class Signup(CreateView):
    form_class = UserCreationForm
    template_name = 'core/signup.html'
    success_url = reverse_lazy('core:dashboard')


signup = Signup.as_view()
