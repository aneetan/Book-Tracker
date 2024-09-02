from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book


# Create your views here.

def addBook(request):
    if request.method == 'POST':
        book = Book.objects.create(
            name = request.POST.get('name'),
            author = request.POST.get('author'),
            pages = request.POST.get('pages'),
            time_mins = request.POST.get('time_mins') 
        )

        messages.success(request, "Book added successfully")
        return redirect('viewBook')
        
    return render(request, 'Book/tracking.html')


def viewBook(request):
    book = Book.objects.all()
    return render(request, 'Book/book_view.html', {'books': book})
