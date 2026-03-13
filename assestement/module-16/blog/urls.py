from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # User Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Blog Management
    path('add-post/', views.add_post, name='add_post'),
    path('edit-post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete-post/<int:id>/', views.delete_post, name='delete_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),

    # Interaction Features
   path('like/<int:id>/', views.like_post, name='like_post'),
   path('comment/<int:id>/', views.add_comment, name='add_comment'),
   path('follow/<int:id>/', views.follow_user, name='follow_user'),
]