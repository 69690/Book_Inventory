from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
import requests
from django.http import HttpResponseRedirect

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

def search_book(request):
    #https://www.googleapis.com/books/v1/volumes
    # ?q=flowers+inauthor:keyes&key=AIzaSyCeb83AnvleYBTR9XFIQVl82cNeQyw_q0c
    try:
        query = request.GET['query']
        URL = 'https://www.googleapis.com/books/v1/volumes'
        PARAMS = {
            'q': query, 
            'key': 'AIzaSyCeb83AnvleYBTR9XFIQVl82cNeQyw_q0c'
        }

        r = requests.get(url = URL, params = PARAMS)

        class Book_s:
            def __init__(self, title, author, google_id, description=''):
                self.pk = None
                self.title = title
                self.author = author
                self.google_id = google_id
                self.description = description
                if not Book.objects.filter(google_id = google_id).exists(): #If not in inventory
                    self.status = "Not Available"
                else: #if book is in inventory
                    item = get_object_or_404(Book, google_id = google_id) #fetching item

                    #checking if stock > 0
                    if item.stock > 0:
                        self.pk = item.pk
                        self.status = "Available"
                    else:
                        self.pk = item.pk
                        self.status = "Out Of Stock"

        data = r.json()

        #creating a list to store all objects from the search result along with their status in inventory using above class
        search_results = []
        for i in data['items']:
            try: #check if all fields exist
                #x = i['volumeInfo']['authors']
                t = i['volumeInfo']['title']
                a = i['volumeInfo']['authors']
                st_a = ''
                if len(a) == 1:
                    st_a += a[0]
                else:
                    for i in range(len(a)-1):
                        st_a += a[i]
                        st_a += ', '
                    st_a += a[-1]

                i_d = i['id']
                try:
                    d = i['volumeInfo']['description']
                    obj = Book_s(t,st_a,i_d,d)
                except:
                    obj = Book_s(t,st_a,i_d)
                
                # print(obj.google_id)
                # print(obj.status)
                # print()
                search_results.append(obj)
                # print(item['id'])
                # print(item['volumeInfo']['authors'])
                #print()
            except:
                print(i)
                print()
                pass

                #print(i['volumeInfo'])
        # for key, value in data['items'].items():
        #     print(key,' : ',value)
        
        # for item in data['items']:
        #     for v in item['volumeInfo']:
        #         if 'authors' in v.keys():
        #             print(v['authors'])
            #print(item['volumeInfo']['authors'])
        context = {
            'search_results': search_results,
            'length': len(search_results)
        }

        messages.success(request, 'Search Results...')
        return render(request, 'search.html', context)
    except:
        messages.error(request, "Enter a search query")
        return redirect('index')

def about(request):
    messages.info(request, "Welcome To About Me")
    return render(request, 'about.html')