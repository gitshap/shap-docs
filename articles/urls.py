from unicodedata import name
from django.urls import path
from articles import views

urlpatterns = [
    path('', views.home, name='home'),


    # posts
    path('post/create_post/', views.create_post, name='create_post'),

    # posts view posts
    path('post/view_post/<int:id>', views.view_post, name='view_post'),
    path('post/update_post/<int:id>', views.update_post, name='update_post'),
    path('post/delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('post/all_post/<int:id>', views.all_post, name='all_post'),
    path('post/search_post/', views.search_post, name='search_post'),

    path('test/', views.testing_tailwind, name='testing_tailwind')
]
