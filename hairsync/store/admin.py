from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Product
from .models import CategoryManager
from .models import Address
from .models import ShoppingCart
from .models import CartItem
from .models import Order
from .models import OrderItem
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name',)
    search_fields = ('name',)
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'price', 'category', 'quantity_in_stock', 'description')
    search_fields = ('name',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'user', 'created_at', 'updated_at', 'status')
    search_fields = ('user__username',)
    list_filter = ('status',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'cart', 'product', 'quantity')
    search_fields = ('product__name',)
    list_filter = ('cart__status',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'cart', 'total_amount', 'order_status', 'created_at')
    search_fields = ('user__username', 'cart__cart_id')
    list_filter = ('order_status',)
    readonly_fields = ('created_at',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'order', 'cart_item', 'product', 'quantity', 'unit_price')
    search_fields = ('product__name', 'order__user__username')
    list_filter = ('order__order_status',)
    readonly_fields = ('unit_price',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'user', 'street_address', 'town', 'zipcode', 'county')
    search_fields = ('user__username', 'street_address', 'town', 'zipcode')
    list_filter = ('user',)
    readonly_fields = ('address_id',)