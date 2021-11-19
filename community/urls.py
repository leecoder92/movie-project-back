from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.article_update_delete, name='article_update_delete')
]
