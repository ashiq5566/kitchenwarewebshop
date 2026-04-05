from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    BADGE_CHOICES = [
        ('', 'None'),
        ('Best Seller', 'Best Seller'),
        ('New', 'New'),
        ('Popular', 'Popular'),
        ('Top Rated', 'Top Rated'),
        ('Sale', 'Sale'),
        ('Limited', 'Limited'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        help_text='Set this to show a strikethrough original price (for discounts)'
    )
    rating = models.DecimalField(
        max_digits=3, decimal_places=1,
        default=5.0,
        help_text='Rating out of 5'
    )
    badge = models.CharField(
        max_length=50, blank=True,
        choices=BADGE_CHOICES,
        default='',
        help_text='Optional badge shown on the product card'
    )
    image = models.ImageField(
        upload_to='products/',
        null=True, blank=True,
        help_text='Product image (uploaded to Cloudinary in production)'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Uncheck to hide this product from the website'
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text='Lower number = shown first. Use this to reorder products.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name
