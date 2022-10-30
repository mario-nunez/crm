from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),
    
    path('', views.home, name="home"),
    path('user/', views.user_page, name="user-page"),
    path('account/', views.account_settings, name="account"),
    
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('update-customer/<str:pk>/', views.update_customer, name="update-customer"),

    path('create-order/<str:pk>', views.create_order, name="create-order"),
    path('update-order/<str:pk>/', views.update_order, name="update-order"),
    path('delete-order/<str:pk>/', views.delete_order, name="delete-order"),


    # Add a template using template_name='accounts/password_reset.html'
    path('reset-password/',
         auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset-password-sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset-password-complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='reset_password_complete'),

]
