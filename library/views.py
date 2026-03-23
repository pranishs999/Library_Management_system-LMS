from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Book, Patron, Borrow
from .forms import BookForm, BorrowForm, PatronForm, ProfileUpdateForm, StyledPasswordChangeForm

# ─────────────────── Auth Views ───────────────────

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Account created! Please log in.')
        return super().form_valid(form)

class UserSettingsView(LoginRequiredMixin, View):
    template_name = 'settings.html'

    def get(self, request):
        return render(request, self.template_name, {
            'profile_form': ProfileUpdateForm(instance=request.user),
            'password_form': StyledPasswordChangeForm(request.user),
        })

    def post(self, request):
        if 'update_profile' in request.POST:
            profile_form = ProfileUpdateForm(request.POST, instance=request.user)
            password_form = StyledPasswordChangeForm(request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('settings')
        elif 'change_password' in request.POST:
            profile_form = ProfileUpdateForm(instance=request.user)
            password_form = StyledPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully!')
                return redirect('settings')
        else:
            profile_form = ProfileUpdateForm(instance=request.user)
            password_form = StyledPasswordChangeForm(request.user)

        return render(request, self.template_name, {
            'profile_form': profile_form,
            'password_form': password_form,
        })

# ─────────────────── Home View ───────────────────

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

# ─────────────────── List Views ───────────────────

class BookListViews(LoginRequiredMixin, ListView):
    template_name = "book_list.html"
    model = Book
    context_object_name = 'books'

class PatronListViews(LoginRequiredMixin, ListView):
    template_name = "patron_list.html"
    model = Patron
    context_object_name = 'patrons'

class BorrowListViews(LoginRequiredMixin, ListView):
    template_name = "borrow_list.html"
    model = Borrow
    context_object_name = 'borrows'

    def get_queryset(self):
        # Prevent N+1 query by using select_related for foreign keys
        return Borrow.objects.select_related('patron', 'book').all().order_by('-borrow_date')

# ─────────────────── Create Views ───────────────────

class AddBookViews(LoginRequiredMixin, CreateView):
    template_name = "add_book.html"
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        messages.success(self.request, 'Book added successfully!')
        return super().form_valid(form)

class AddPatronViews(LoginRequiredMixin, CreateView):
    template_name = "add_user.html"
    model = Patron
    form_class = PatronForm
    success_url = reverse_lazy('patron_list')

    def form_valid(self, form):
        messages.success(self.request, 'Patron added successfully!')
        return super().form_valid(form)

class AddBorrowViews(LoginRequiredMixin, CreateView):
    template_name = "add_borrow.html"
    model = Borrow
    form_class = BorrowForm
    success_url = reverse_lazy('borrow_list')

    def form_valid(self, form):
        messages.success(self.request, 'Borrow recorded successfully!')
        return super().form_valid(form)

# ─────────────────── Edit Views ───────────────────

class EditBookViews(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'edit_book.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)

class EditPatronViews(LoginRequiredMixin, UpdateView):
    model = Patron
    template_name = 'edit_patron.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('patron_list')

    def form_valid(self, form):
        messages.success(self.request, 'Patron updated successfully!')
        return super().form_valid(form)

class EditBorrowViews(LoginRequiredMixin, UpdateView):
    model = Borrow
    template_name = 'edit_borrow.html'
    fields = ['borrow_date', 'return_date']
    success_url = reverse_lazy('borrow_list')

    def form_valid(self, form):
        messages.success(self.request, 'Borrow record updated successfully!')
        return super().form_valid(form)

# ─────────────────── Delete Views ───────────────────

class DeleteBookViews(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book_list')

class DeleteBorrowViews(LoginRequiredMixin, DeleteView):
    model = Borrow
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('borrow_list')

class DeletePatronViews(LoginRequiredMixin, DeleteView):
    model = Patron
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('patron_list')

# ─────────────────── Search Views ───────────────────

@login_required
def search_patron(request):
    if 'membership_id' in request.GET:
        membership_id = request.GET['membership_id']
        patron = Patron.objects.filter(membership_id=membership_id)
        return render(request, 'search_patron.html', {'patron': patron})
    return render(request, 'search_patron.html')

@login_required
def search_borrow_by_user_and_book(request):
    if 'membership_id' in request.GET and 'isbn' in request.GET:
        membership_id = request.GET['membership_id']
        isbn = request.GET['isbn']
        patron = Patron.objects.get(membership_id=membership_id)
        book = Book.objects.get(isbn=isbn)
        borrow = Borrow.objects.filter(patron=patron, book=book)
        return render(request, 'search_borrow.html', {'borrow': borrow})
    return render(request, 'search_borrow.html')

# ─────────────────── Dashboard ───────────────────

@login_required
def dashboard(request):
    total_books = Book.objects.count()
    total_patrons = Patron.objects.count()
    # Optimize active borrows query to avoid N+1 when rendering table
    borrowed_books = Borrow.objects.select_related('patron', 'book').filter(return_date__isnull=True).order_by('-borrow_date')
    return render(request, 'dashboard.html', {
        'total_books': total_books,
        'total_patrons': total_patrons,
        'borrowed_books': borrowed_books,
    })
