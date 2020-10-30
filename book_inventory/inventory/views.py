from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    items = Book.objects.all()

    context = {
        'items': items, #table
    }

    return render(request, 'index.html', context = context) #render table in main page

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            google_id = form.cleaned_data['google_id']   #Getting Google_ID field from the form which is automatically filled with AJAX API request
            
            if not Book.objects.filter(google_id = google_id).exists(): #Book does not exist in inventory
                #print(google_id)
                form.save()
                messages.success(request, 'Added New Book To Inventory')
                return redirect('index')

            else: #Book exists in inventory
                item = get_object_or_404(Book, google_id = google_id) #Get the item with corresponding GID
                additional_stock = form.cleaned_data['stock']  #Get the extra stock from the form stock field
                existing_stock = item.stock 
                updated_stock = existing_stock + additional_stock
                #print(updated_stock)
                item.stock = updated_stock #Update existing stock
                if updated_stock == 0:
                    item.status = 'Out Of Stock'
                else:
                    item.status = 'Available'
                item.save() #save with updated inventory
                messages.info(request, "Updated Existing Inventory")
                return redirect('index')
        else:
            # for field, items in form.errors.items():
            #     for item in items:
            #         messages.error(request, '{}: {}'.format(field, item))
            # for msg in form.error_messages:
            #     messages.error(request, f"{msg}: {form.error_messages[msg]}")
            messages.error(request, "Search For Book Below To Autofill")
            return render(request, 'add_book.html', {'form': form})
    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})

def edit_book(request, pk):
    item = get_object_or_404(Book, pk=pk) #select statement with pk
    if request.method == "POST":
        form = BookForm(request.POST, instance=item)   #populate form with information with the information brought earlier
        if form.is_valid(): #Valid Form
            messages.success(request, "Book Successfully Edited")
            form.save()
            return redirect('index')
        else: #Invalid Form
            form = BookForm(instance=item)
            return render(request, 'edit_book.html', {'form':form})
    else:
        form = BookForm(instance=item)
        return render(request, 'edit_book.html', {'form':form})

def delete_book(request, pk):
    Book.objects.filter(id=pk).delete()
    
    items = Book.objects.all()

    context = {
        'items': items
    }

    messages.success(request, "Book Successfully Deleted")
    return render(request, 'index.html', context)