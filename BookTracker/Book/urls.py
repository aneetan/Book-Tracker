from django.urls import path
from . import views

urlpatterns = [
    path('', views.addBook, name="addBook"),
    path('viewBooks/', views.viewBook, name="viewBook"),

]