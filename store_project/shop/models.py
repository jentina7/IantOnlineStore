from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    ROLE_CHOICES = (
        ('клиент', 'клиент'),
        ('владелец', 'владелец'),
        ('курьер', 'курьер')
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='клиент')

    def __str__(self):
        return f" {self.first_name} - {self.last_name}"


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name


class Store(models.Model):
    store_name = models.CharField(max_length=32)
    store_image = models.ImageField(upload_to="store_images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    description = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name


class ContactInfo(models.Model):
    contact_info = PhoneNumberField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="contacts")

    def __str__(self):
        return f"{self.store} - {self.contact_info}"


class Brand(models.Model):
    brand_name = models.CharField(max_length=32)
    brand_image = models.ImageField(upload_to="brand_images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='brands')
    description = models.TextField()

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    product_store = models.ForeignKey(Store, related_name="products", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product_images = models.ImageField(upload_to="product_images/")
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='product_images')


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="cart")

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.product}, {self.quantity }"


class Order(models.Model):
    client = models.ForeignKey(UserProfile, related_name="orders", on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ("Ожидает обработки", "Ожидает обработки"),
        ("В процессе доставки", "В процессе доставки"),
        ("Доставлен", "Доставлен"),
        ("Отменен", "Отменен")
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default="Ожидает обработки", null=True, blank=True)
    delivery_address = models.CharField(max_length=64)
    courier = models.ForeignKey(UserProfile, related_name="couriers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.client} - {self.status} - {self.courier}"


class Courier(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="courier")
    current_orders = models.ForeignKey(Order, related_name="couriers", on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ("доступен", "доступен"),
        ("занят", "занят")
    )
    status_courier = models.CharField(max_length=16, choices=STATUS_CHOICES, default="доступен")

    def __str__(self):
        return f" {self.user} - {self.status_courier}"


class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_review")
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.store}"
