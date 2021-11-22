from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.article_update_delete, name='article_update_delete'),
    path('<int:article_pk>/comments/', views.comment_list_create, name='comment_list_create'),
    path('<int:article_pk>/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]
