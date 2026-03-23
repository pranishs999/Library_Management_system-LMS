from django import forms
from .models import Book, Patron, Borrow
from django.forms import DateInput, TextInput, EmailInput, Select, URLInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm

CLASS_INPUT = "w-full px-4 py-2.5 text-sm text-gray-900 dark:text-white bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
CLASS_SELECT = "w-full px-4 py-2.5 text-sm text-gray-900 dark:text-white bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none transition-all"

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'Enter book title'}),
            'author': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'Author name'}),
            'published_date': DateInput(attrs={'class': CLASS_INPUT, 'type': 'date'}),
            'isbn': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'e.g. 978-3-16-148410-0'}),
            'category': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'e.g. Fiction, Science'}),
            'total_copies': TextInput(attrs={'class': CLASS_INPUT, 'type': 'number', 'min': '1'}),
            'available_copies': TextInput(attrs={'class': CLASS_INPUT, 'type': 'number', 'min': '0'}),
            'cover_image': URLInput(attrs={'class': CLASS_INPUT, 'placeholder': 'https://example.com/cover.jpg (optional)'}),
        }

class PatronForm(forms.ModelForm):
    class Meta:
        model = Patron
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'Last name'}),
            'email': EmailInput(attrs={'class': CLASS_INPUT, 'placeholder': 'email@example.com'}),
        }

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['patron', 'book', 'borrow_date', 'return_date']
        widgets = {
            'patron': Select(attrs={'class': CLASS_SELECT}),
            'book': Select(attrs={'class': CLASS_SELECT}),
            'borrow_date': DateInput(attrs={'class': CLASS_INPUT, 'type': 'date'}),
            'return_date': DateInput(attrs={'class': CLASS_INPUT, 'type': 'date'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'First name'}),
            'last_name': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'Last name'}),
            'username': TextInput(attrs={'class': CLASS_INPUT, 'placeholder': 'Username'}),
            'email': EmailInput(attrs={'class': CLASS_INPUT, 'placeholder': 'email@example.com'}),
        }

class StyledPasswordChangeForm(DjangoPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': CLASS_INPUT})
