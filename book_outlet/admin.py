from django.contrib import admin
from .models import Book, Author, Address, Country


class  AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author')
    list_filter = ('rating','author')

  

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Address)
admin.site.register(Country)

