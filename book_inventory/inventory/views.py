from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    items = Book.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'index.html', context = context)

def display_books(request):
    items = Book.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'index.html', context = context)

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print("WTF")
    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})