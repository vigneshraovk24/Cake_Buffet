from django.shortcuts import render, get_object_or_404, redirect
from main.models import Item,CartItems,CustomCakes,Custom_Orders,Reviews
from users.models import Customer
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.conf import settings
from django.core.mail import send_mail


class MenuListView(ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'menu_items'

def menuDetail(request, slug):
    item = Item.objects.filter(slug=slug).first() 
    reviews = Reviews.objects.filter(rslug=slug).order_by('-id')
    context = {
        'item' : item,
        'reviews':reviews,
    }
    return render(request, 'dishes.html', context)

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    cart_item = CartItems.objects.create(
        item=item,
        user=request.user,
        ordered=False,
    )
    messages.info(request, "Added to Cart!!!")
    return redirect("main:cart")

@login_required
def get_cart_items(request):
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    bill = cart_items.aggregate(Sum('item__price'))
    number = cart_items.aggregate(Sum('quantity'))
    pieces = cart_items.aggregate(Sum('item__pieces'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    total_pieces = pieces.get("item__pieces__sum")
    context = {
        'cart_items':cart_items,
        'total': total,
        'count': count,
        'total_pieces': total_pieces
    }
    return render(request, 'cart.html', context)

class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CartItems
    success_url = '/cart'

    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.user:
            return True
        return False

@login_required
def profile(request):
    user = Customer.objects.all()
    return render(request,"profile.html")

@login_required
def order_item(request):
    return render(request,"user_order_details.html")

@login_required
def user_order_details(request):
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    ordered_date=timezone.now()



    delivery_addrs = request.POST.get('addr')
    inst = request.POST.get('ins')

    cart_items.update(delivery_addrs=delivery_addrs,inst=inst)
    cart_items.update(ordered=True,ordered_date=ordered_date)
    user= request.user
    subject = ' CAKEBUFFET ORDER SUCCESSFULL'
    sub = 'NEW ORDER ARRIVED'
    message = f'Hi!!!{user.username},Your cakes have been successfully ordered and Our deliver partner will reach the location within 30-40 minutes.Order Again!!!'
    msg = f'Our customer {user.username} have order a new item. Assign a deliver partner soon!!!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    to = ['vigneshrauvk13@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    send_mail(sub, msg, email_from, to)
    messages.info(request, "Successfully Ordered!!!")
    return render(request,"order_successful.html")

@login_required
def order_details(request):
    items = CartItems.objects.filter(user=request.user, ordered=True,status="Ordered").order_by('-ordered_date')
    cart_items = CartItems.objects.filter(user=request.user, ordered=True,status="Delivered").order_by('-ordered_date')
    custom_cart_items = Custom_Orders.objects.filter(user=request.user,custom_ordered=True,custom_status="Waiting for confirmation").order_by('-custom_ordered_date')
    bill = items.aggregate(Sum('item__price'))
    number = items.aggregate(Sum('quantity'))
    pieces = items.aggregate(Sum('item__pieces'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    total_pieces = pieces.get("item__pieces__sum")
    context = {
        'items':items,
        'cart_items':cart_items,
        'custom_cart_items':custom_cart_items,
        'total': total,
        'count': count,
        'total_pieces': total_pieces,
    }
    return render(request, 'order_details.html', context)

class CustomView(ListView):
    model = CustomCakes
    template_name = 'custom_order.html'
    context_object_name = 'custom_items'

def custom_menu(request, slug):
    custom_item = CustomCakes.objects.filter(custom_slug=slug).first() 
    context = {
        'custom_item' : custom_item,
    }
    return render(request, 'cinfos.html', context)

@login_required
def custom_cart(request, slug):
    custom_item = get_object_or_404(CustomCakes, custom_slug=slug)
    custom_cart= Custom_Orders.objects.create(
        custom_item=custom_item,
        user=request.user,
        custom_ordered=False,
    )

    return redirect('main:custom_user_dtl')

@login_required
def custom_user_dtl(request):
    return render(request, 'custom_user_order_details.html')

@login_required
def custom_user_order_details(request):
    custom_cart_items = Custom_Orders.objects.filter(user=request.user,custom_ordered=False)
    custom_ordered_date=timezone.now()


    quantity_in_kg = request.POST.get('ckg')
    delivery_address = request.POST.get('caddr')
    custom_instructions = request.POST.get('cins')

    
    custom_cart_items.update(delivery_address=delivery_address,custom_instructions=custom_instructions,quantity_in_kg=quantity_in_kg)
    custom_cart_items.update(custom_ordered=True,custom_ordered_date=custom_ordered_date)
    user= request.user
    custom_subject = ' CAKEBUFFET CUSTOM ORDER SUCCESSFULL'
    custom_sub = 'NEW CUSTOM ORDER ARRIVED'
    custom_message = f'Hi!!!{user.username},Your customizing cake have been successfully ordered and Our deliver partner will reach the location within 3-4hours after the confirmation phone call by our admin.Order Again!!!'
    custom_msg = f'Our customer {user.username} have order a new customizing cake. Call the customer for the confirmation'
    custom_email_from = settings.EMAIL_HOST_USER
    custom_recipient_list = [user.email]
    custom_to = ['vigneshrauvk13@gmail.com']
    send_mail( custom_subject, custom_message, custom_email_from, custom_recipient_list )
    send_mail(custom_sub, custom_msg, custom_email_from, custom_to)
    messages.info(request, "Successfully Ordered!!!")
    return render(request,'order_successful.html')

@login_required
def cake_reviews(request):
    if request.method == "POST":
        user = request.user
        rslug = request.POST.get("rslug")
        item = Item.objects.get(slug=rslug)
        review = request.POST.get("review")

        reviews = Reviews(user=user, item=item, review=review, rslug=rslug)
        reviews.save()
        messages.success(request, "Thank You for the review !!")
    return redirect(f"/dishes/{item.slug}")