from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"
    

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.street}, {self.postal_code}, {self.city}'
    
    class Meta:
        verbose_name_plural="Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MaxValueValidator(10),MinValueValidator(1)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    is_best_selling = models.BooleanField(default=False)  
    slug = models.SlugField(default="", null=False, db_index=True)
    published_country = models.ManyToManyField(Country, null=False)

    def __str__(self) -> str:
        return f'{self.title} ({self.rating})'
    
    def get_absolute_url(self):
        return reverse("book-detail-url", kwargs={"slug":self.slug})
    