from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.review_create, name='review_create'),
    path('<int:review_pk>', views.review_update_delete, name='review_update_delete')
]
