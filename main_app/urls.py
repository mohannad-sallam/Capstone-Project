from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('part/<int:pk>/', views.part_detail, name='part_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('part/<int:pk>/review/', views.add_review, name='add_review'),
    path('part/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/update/', views.update_comment, name='update_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),

]
