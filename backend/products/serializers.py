from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_url = serializers.SerializerMethodField()
    discount_percent = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            if hasattr(obj.image, 'url'):
                url = obj.image.url
                # Cloudinary URLs are already absolute
                if url.startswith('http'):
                    return url
                # Local media — build absolute URL
                if request:
                    return request.build_absolute_uri(url)
        return None

    def get_discount_percent(self, obj):
        if obj.original_price and obj.original_price > obj.price:
            discount = ((obj.original_price - obj.price) / obj.original_price) * 100
            return round(discount)
        return None

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description',
            'category_name',
            'price', 'original_price', 'discount_percent',
            'rating', 'badge',
            'image_url',
            'is_active',
        ]
