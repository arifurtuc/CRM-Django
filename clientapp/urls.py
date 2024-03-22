from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('user-login', views.user_login, name='user-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('client-dashboard', views.client_dashboard, name='client-dashboard'),
    path('add-client', views.add_client, name='add-client'),
    path('client-details/<int:pk>', views.view_client, name='client-details'),
    path('update-client/<int:pk>', views.update_client, name='update-client'),
    path('delete-client/<int:pk>', views.delete_client, name='delete-client'),
]