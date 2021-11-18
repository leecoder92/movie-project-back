from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/',obtain_jwt_token),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]
