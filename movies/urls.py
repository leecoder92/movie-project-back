from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.get_movies, name="get_movies"),
    path('<int:detail_id>/', views.get_reviews, name="get_reviews"),
    path('<int:detail_id>/<int:review_id>/', views.delete_reviews, name="delete_reviews"),
# <<<<<<< Updated upstream
#     path('recommendation/', views.get_my_reviews, name = "get_my_reviews")
    path('recommend/', views.recommend, name="recommend"),

]
