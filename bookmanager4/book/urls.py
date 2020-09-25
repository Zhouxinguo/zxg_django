from django.urls import path
from book.views import creates

urlpatterns = {
    path('create/',creates),
}