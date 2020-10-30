from django import forms
from .models import *

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # self.fields['title'].disabled = True
        # self.fields['author'].disabled = True 
        # self.fields['google_id'].disabled = True
        #self.fields['status'].disabled = True 
    
    class Meta:
        model = Book  #Book Model
        fields = ('title','author','google_id','stock')

    # def change_status(self):
    #     self.fields['title'].disabled = False
    #     self.fields['author'].disabled = False
    #     self.fields['google_id'].disabled = False

    def clean(self):
        cleaned_data = self.cleaned_data
        stock = cleaned_data.get('stock')
        status = cleaned_data.get('status')
    
    def save(self, commit=True):
        book = super().save(commit=False)
        stock = self.cleaned_data.get('stock')
        if stock > 0:
            book.status = 'Available'
        else:
            book.status = 'Out Of Stock'
        book.save()
        return book