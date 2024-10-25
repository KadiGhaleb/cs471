from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
    path('', views.index,name='index'), #the main root, http:127.0.0.1/8000/
    path('books', views.books), #the root is books http:127.0.0.1/8000/books
    path('book/<int:bId>', views.book)
]
