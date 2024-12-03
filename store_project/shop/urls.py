from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users_list')
router.register(r'cart', CartViewSet, basename='cart_list')
router.register(r'cart_item', CartItemViewSet, basename='cart_item_list')
router.register(r'order', OrderViewSet, basename='order_list')
router.register(r'courier', CourierViewSet, basename='courier_list')
router.register(r'store_review', StoreReviewViewSet, basename='store_review_list')

urlpatterns = [
    path('', include(router.urls)),
    path("store/", StoreListApiView.as_view(), name= "store_list"),
    path("store/<int:pk>", StoreDetailApiView.as_view(), name= "store_detail"),
]