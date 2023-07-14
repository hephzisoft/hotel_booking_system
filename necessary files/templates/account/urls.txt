from django.urls import path
from account.views import login, register, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('login/', login, name='login'),
   path('register/', register, name='register'),
   path('logout/', user_logout, name="logout"),

   path(
      'password_reset/', 
      auth_views.PasswordResetView.as_view(
         template_name='account/password-reset/password_reset.html'
      ), 
      name='password_reset'
   ),

   path(
      'password_reset_done/',
      auth_views.PasswordResetDoneView.as_view(
         template_name='account/password-reset/password_reset_done.html'
      ),
      name='password_reset_done'
   ),

   path(
      'password_reset_confirm/<uidb64>/<token>/',
      auth_views.PasswordResetConfirmView.as_view(
         template_name='account/password-reset/password_reset_confirm.html'
      ),
      name='password_reset_confirm'
   ),

   path(
      'password_reset_complete/',
      auth_views.PasswordResetCompleteView.as_view(
         template_name='account/password-reset/password_reset_complete.html'
      ),
      name='password_reset_complete'
   ),
]