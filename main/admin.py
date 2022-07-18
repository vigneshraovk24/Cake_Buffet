from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import Customer
from main.models import Item,CartItems,CustomCakes,Custom_Orders,Reviews
# Register your models here.

admin.site.site_header = 'Cake Buffet'

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('user','get_item_name','get_phone','status',)

    @admin.display(description='Phone', ordering='user__phone_number')
    def get_phone(self,obj):
        return obj.user.phone_number

    @admin.display(description='Cake name', ordering='item_title')
    def get_item_name(self,obj):
        return obj.item.title

class Custom_OrdersAdmin(admin.ModelAdmin):
    list_display = ('user','get_phone','custom_status',)

    @admin.display(description='Phone', ordering='user__phone_number')
    def get_phone(self,obj):
        return obj.user.phone_number

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review','get_name','get_item')

    @admin.display(description='Username')
    def get_name(self,obj):
        return obj.user.username

    @admin.display(description='Review for')
    def get_item(self,obj):
        return obj.item.title

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(CartItems, CartItemsAdmin)
admin.site.register(CustomCakes)
admin.site.register(Custom_Orders,Custom_OrdersAdmin)
admin.site.register(Reviews,ReviewsAdmin)