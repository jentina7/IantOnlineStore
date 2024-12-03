from django.contrib import admin
from modeltranslation.admin import TranslationInlineModelAdmin, TranslationAdmin
from .models import *


class ProductInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = Product
    extra = 1


class BrandInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = Brand
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 1


@admin.register(Category)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Store)
class StoreAdmin(TranslationAdmin):
    inlines = [BrandInline, ProductInline, ContactInfoInline, ProductImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Courier)
admin.site.register(StoreReview)
