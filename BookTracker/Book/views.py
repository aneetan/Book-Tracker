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

def editBook(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        # Update the book details
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.pages = request.POST.get('pages')
        book.time_mins = request.POST.get('time_mins')
        book.save()

        messages.success(request, "Book updated successfully")
        return redirect('viewBook')
    
    return render(request, 'Book/edit_book.html', {'book': book})