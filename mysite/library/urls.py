from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>', views.author, name='author'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', views.search, name='search'),
    path('myboooks/', views.LoanBooksListView.as_view(), name='my-borrowed'),
    path('register/', views.register, name='register'),
    path('profile/', views.profilis, name='profile')
]
