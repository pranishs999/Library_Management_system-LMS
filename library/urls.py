from django.urls import path
from .views import BookListViews, AddBookViews, PatronListViews, AddPatronViews, BorrowListViews, AddBorrowViews, EditBookViews, EditPatronViews, EditBorrowViews, DeleteBookViews, DeleteBorrowViews, DeletePatronViews, search_patron, search_borrow_by_user_and_book, dashboard, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Use HomeView CBV for home
    path('books/', BookListViews.as_view(), name='book_list'),
    path('books/add/', AddBookViews.as_view(), name='add_book'),
    path('books/edit/<int:pk>/', EditBookViews.as_view(), name='edit_book'),
    path('books/delete/<int:pk>/', DeleteBookViews.as_view(), name='delete_book'),

    path('patrons/', PatronListViews.as_view(), name='patron_list'),
    path('patrons/add/', AddPatronViews.as_view(), name='add_patron'),
    path('patrons/edit/<int:pk>/', EditPatronViews.as_view(), name='edit_patron'),
    path('patrons/delete/<int:pk>/', DeletePatronViews.as_view(), name='delete_patron'),

    path('borrows/', BorrowListViews.as_view(), name='borrow_list'),
    path('borrows/add/', AddBorrowViews.as_view(), name='add_borrow'),
    path('borrows/edit/<int:pk>/', EditBorrowViews.as_view(), name='edit_borrow'),
    path('borrows/delete/<int:pk>/', DeleteBorrowViews.as_view(), name='delete_borrow'),

    path('search/patron/', search_patron, name='search_patron'),
    path('search/borrow/', search_borrow_by_user_and_book, name='search_borrow'),

    path('dashboard/', dashboard, name='dashboard'),
    path('edit_book/<int:pk>/', EditBookViews.as_view(), name='edit_book'),
    path('edit_patron/<int:pk>/', EditPatronViews.as_view(), name='edit_patron'),
    path('edit_borrow/<int:pk>/', EditBorrowViews.as_view(), name='edit_borrow'),
]
