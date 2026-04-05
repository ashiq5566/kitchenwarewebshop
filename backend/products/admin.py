from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order', 'product_count']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order', 'name']

    def product_count(self, obj):
        count = obj.products.filter(is_active=True).count()
        return f'{count} products'
    product_count.short_description = 'Active Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price_display', 'original_price',
        'badge', 'rating', 'is_active', 'order', 'image_preview'
    ]
    list_editable = [ 'original_price', 'badge', 'rating', 'is_active', 'order']
    list_filter = ['category', 'is_active', 'badge']
    search_fields = ['name', 'description']
    ordering = ['order', '-created_at']
    readonly_fields = ['image_preview', 'created_at', 'updated_at']

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'description', 'category')
        }),
        ('Pricing', {
            'fields': ('price', 'original_price'),
            'description': 'Set original_price higher than price to show a discount badge automatically.'
        }),
        ('Display', {
            'fields': ('badge', 'rating', 'order', 'is_active')
        }),
        ('Image', {
            'fields': ('image', 'image_preview')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def price_display(self, obj):
        return f'₹{obj.price:,.2f}'
    price_display.short_description = 'Price'
    price_display.admin_order_field = 'price'

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:80px; border-radius:8px;" />',
                obj.image.url
            )
        return '—'
    image_preview.short_description = 'Preview'


# Customize admin site header
admin.site.site_header = 'SteelNest Admin'
admin.site.site_title = 'SteelNest'
admin.site.index_title = 'Manage Products & Categories'
