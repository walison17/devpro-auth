from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login

from .views import signup, dashboard

app_name = 'core'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='core/signin.html', redirect_authenticated_user=True), name='login'),
    path('logout/', logout_then_login, name='logout'),
]
