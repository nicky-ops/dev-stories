from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'  

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to the home page
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.profile, name='profile')
]
