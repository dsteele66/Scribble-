from django.urls import path
from . import views
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('comments/', views.comment_list, name='comment_list'), 
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('posts/new', views.post_create, name='post_create'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]