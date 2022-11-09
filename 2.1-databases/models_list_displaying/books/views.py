from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def book(request):
    template = 'books/book.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def book_for_date(request, pub_date):
    template = 'books/books_date.html'
    books = Book.objects.filter(pub_date=pub_date)



    books_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()
    context = {'books': books, 'books_next': books_next, 'previous_book': books_previous, }

    return render(request, template, context)
