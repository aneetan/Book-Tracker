from django.urls import path
from . import views

urlpatterns = [
    path('', views.addBook, name="addBook"),
    path('viewBooks/', views.viewBook, name="viewBook"),
    path('editBook/<int:book_id>/', views.editBook, name="editBook"),

]
