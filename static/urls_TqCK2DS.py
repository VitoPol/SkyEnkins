from django.contrib.auth.views import LogoutView
from django.urls import path, include

from app import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, basename="user")

urlpatterns = [
    path('', views.UserViewSet.auth_page),
    path('signup/', views.UserCreate.as_view(), name="signup"),
    path('login/', views.AuthView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('upload/', views.UploadView.as_view(), name="upload"),
    path('home/', views.FileListView.as_view(), name="home"),
    path('del/<pk>/', views.FileDelView.as_view(), name="del"),
    path('update/<pk>/', views.FileUpdateView.as_view(), name="update"),
]
