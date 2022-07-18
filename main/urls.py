from django.urls import path
from . import views
from .views import (
    MenuListView,
    menuDetail,
    add_to_cart,
    get_cart_items,
    order_item,
    user_order_details,
    order_details,
    CartDeleteView,
    profile,
    CustomView,
    custom_menu,
    custom_cart,
    custom_user_dtl,
    custom_user_order_details,
    cake_reviews,
)
app_name = "main"

urlpatterns = [
    path('', MenuListView.as_view(), name='home'),
    path('dishes/<slug>', views.menuDetail, name='dishes'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.get_cart_items, name='cart'),
    path('remove-from-cart/<int:pk>/', views.CartDeleteView.as_view(), name='remove-from-cart'),
    path('ordered/', views.order_item, name='ordered'),
    path('user-order-details',views.user_order_details,name='user_order_details'),
    path('order_details/', views.order_details, name='order_details'),
    path('profile/',views.profile,name='profile'),
    path('custom-order', CustomView.as_view(), name='custom'),
    path('custom-order-menu/<slug>', views.custom_menu, name='custom_menu'),
    path('custom-order-details/<slug>',views.custom_cart,name='custom_cart'),
    path('custom-user-dtl/',views.custom_user_dtl,name='custom_user_dtl'),
    path('custom-user-order-details/',views.custom_user_order_details,name='custom_uod'),
    path('cake-review/',views.cake_reviews,name="cake_reviews"),

]