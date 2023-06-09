from django.shortcuts import render , get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request,'book-outlet/index.html',{
        'books': books,
    })

def book_detail(request,slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request,'book-outlet/book-detail.html',{
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestselller': book.is_best_selling,
    })
