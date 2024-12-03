from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name"]


class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ["contact_info"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["product_images"]


class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ["product_name", "product_image", "price", "description"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["brand_name", "brand_image", "category", "description", "store"]


class StoreSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["store_name"]


class StoreReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    client = UserProfileReviewSerializer()
    store = StoreSimpleSerializer()
    class Meta:
        model = StoreReview
        fields = ["client", "store", "comment", "rating", "created_date"]


class StoreListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Store
        fields = ["id", "store_name", "store_image", "category"]


class StoreDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    products = ProductSerializer(many= True, read_only= True)
    brands = BrandSerializer(many=True, read_only=True)
    contacts = ContactInfoSerializer(many=True, read_only=True)
    store_review = StoreReviewSerializer(many=True, read_only=True)
    owner = UserProfileSimpleSerializer()
    class Meta:
        model = Store
        fields = ["id", "store_name", "store_image", "category", "products", "brands", "description", "address",
                  "owner", "contacts", "store_review"]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    class Meta:
        model = Order
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    current_orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = Courier
        fields = ["user", "current_orders", "status_courier"]