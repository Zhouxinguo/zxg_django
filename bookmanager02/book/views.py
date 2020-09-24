from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from book.models import BookInfo

def create_book(request):
    book = BookInfo.objects.create(
        name = 'abc',
        pub_date = '2000-1-1',
        readcount=10
    )

    return HttpResponse('create')





