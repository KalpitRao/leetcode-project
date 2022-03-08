from django.urls import path
from leetcodeadmin import views

urlpatterns = [
    path('admin', views.create_admin)
]
