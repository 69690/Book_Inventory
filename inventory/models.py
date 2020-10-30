from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        ordering = ['id']  #To make things in ascending order

    title = models.CharField(max_length = 200, blank = False)
    author = models.CharField(max_length = 200, blank = False)  
    google_id = models.CharField(max_length = 50, blank = False) #Google Books Volume ID
    stock = models.PositiveIntegerField(default=0)  #Number of Items In Inventory

    choices = (
        ('Available', 'Item is in stock'),
        ('Out Of Stock', 'Item is out of stock'),
        ('Not Available', 'Item is not in inventory')
    )

    status = models.CharField(max_length = 15, choices = choices, blank = False)  #Available, Out Of Stock, Not Available

    def __str__(self):
        return 'Title: {0} Author: {1} Stock: {2}'.format(self.title, self.author, self.stock)