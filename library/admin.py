from django.contrib import admin
from .models import Book, Patron, Borrow

# Custom admin site branding
admin.site.site_header = '📚 LibManager Control Panel'
admin.site.site_title = 'LibManager Admin'
admin.site.index_title = 'Library Administration Dashboard'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'available_copies', 'total_copies', 'published_date')
    search_fields = ('title', 'author', 'isbn', 'category')
    list_filter = ('category', 'published_date')
    list_per_page = 25
    ordering = ('title',)
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'isbn', 'category', 'published_date')
        }),
        ('Inventory', {
            'fields': ('total_copies', 'available_copies')
        }),
        ('Media', {
            'fields': ('cover_image',),
            'classes': ('collapse',),
        }),
    )

@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    list_display = ('membership_id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'membership_id')
    readonly_fields = ('membership_id',)
    list_per_page = 25
    ordering = ('last_name', 'first_name')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('id', 'patron', 'book', 'borrow_date', 'return_date', 'is_active')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('patron__first_name', 'patron__last_name', 'book__title')
    list_per_page = 25
    ordering = ('-borrow_date',)
    raw_id_fields = ('patron', 'book')

    def is_active(self, obj):
        return obj.return_date is None
    is_active.boolean = True
    is_active.short_description = 'Active?'