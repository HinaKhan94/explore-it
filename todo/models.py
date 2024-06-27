from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Todo(models.Model):
    """
    Model for activities listing.
    """
    category = models.ForeignKey(
        'Category', null=True,
        blank=True, on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )
    location = models.TextField()
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2, null=True,
        blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Messages(models.Model):
    """
    model for storing user's inquiry
    when they fill in the form
    via contact page. This is for both registered and
    unregistered users
    """
    class Meta:
        verbose_name_plural = 'Messages'
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name