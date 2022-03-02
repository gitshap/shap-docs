from django.urls import path
from articles import views

urlpatterns = [
    path('', views.home, name='home'),   


    # posts
    path('post/create_post/', views.create_post, name='create_post'),
    
    # posts view posts
    path('post/view_post/<int:id>', views.view_post, name='view_post'),
    path('post/update_post/<int:id>', views.update_post, name='update_post'),
]