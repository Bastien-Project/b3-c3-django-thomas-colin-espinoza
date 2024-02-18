from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

from .views import index, site_list, add_site, edit_site, delete_site, signup


urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sitelist/', views.site_list, name='site_list'),
    path('addsite/', views.add_site, name='add_site'),
    path('edit/<int:pk>/', views.edit_site, name='edit_site'),
    path('delete/<int:pk>/', views.delete_site, name='delete_site'),
    path('signup/', signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #   path('export/csv/', views.export_sites_csv, name='export_sites_csv'),
]
