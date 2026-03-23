from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    isbn = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, db_index=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    published_date = models.DateField()
    cover_image = models.URLField(blank=True, default='',
        help_text="Paste a URL to the book cover image (leave blank for placeholder)")

    def __str__(self):
        return self.title

class Patron(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    membership_id = models.CharField(max_length=10, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.membership_id:
            super().save(*args, **kwargs)
            self.membership_id = str(self.id).zfill(5)
            super().save(update_fields=["membership_id"])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.membership_id} {self.first_name} {self.last_name}"

class Borrow(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(db_index=True)
    return_date = models.DateField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.patron} borrowed {self.book.title} on {self.borrow_date}"