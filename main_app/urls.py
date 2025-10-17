from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('part/<int:pk>/', views.part_detail, name='part_detail'),
    path('accounts/signup/', views.signup, name='signup'),
]
