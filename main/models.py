from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import signals
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.shortcuts import reverse
from users.models import Customer
# Create your models here.

class Item(models.Model):
    LABELS = (
        ('Premium', 'Premium'),
        ('Eggless', 'Eggless'),
        ('Normal', 'Normal'),
    )   

    LABEL_COLOUR = (
        ('danger', 'danger'),
        ('success', 'success'),
        ('primary', 'primary'),
        ('info', 'info'),
        ('warning', 'warning'),
    )
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250,blank=True)
    price = models.FloatField()
    pieces = models.IntegerField(default=1)
    instructions = models.CharField(max_length=250,default="Available")
    image = models.ImageField(upload_to='images/')
    labels = models.CharField(max_length=25, choices=LABELS, blank=True)
    label_colour = models.CharField(max_length=15, choices=LABEL_COLOUR, blank=True)
    slug = models.SlugField(default="cakes")
    created_by = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cake'
        verbose_name_plural = 'Cakes'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:dishes", kwargs={'slug': self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("main:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_item_delete_url(self):
        return reverse("main:item-delete", kwargs={
            'slug': self.slug
        })

    def get_update_item_url(self):
        return reverse("main:item-update", kwargs={
            'slug': self.slug
        })

class CartItems(models.Model):
    ORDER_STATUS = (
        ('Ordered', 'Ordered'),
        ('Delivered', 'Delivered'),
        ('Cancelled','Cancelled')
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    delivery_addrs = models.CharField(max_length=400,blank=True,verbose_name='Current Delivery Address')
    inst = models.CharField(max_length=400,blank=True,verbose_name='Instructions')
    ordered_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Ordered')
    delivery_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.item.title
    
    def get_remove_from_cart_url(self):
        return reverse("main:remove-from-cart", kwargs={
            'pk' : self.pk
        })

    def update_status_url(self):
        return reverse("main:update_status", kwargs={
            'pk' : self.pk
        })

class CustomCakes(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    custom_title = models.CharField(max_length=150,verbose_name='Cake Name')
    custom_price = models.IntegerField(default=0,verbose_name='Price')
    custom_description = models.CharField(max_length=250,blank=True,verbose_name='Description')
    custom_image = models.ImageField(upload_to='custom_images/')
    custom_slug = models.SlugField(default="custom-cakes",verbose_name='Slug')

    class Meta:
        verbose_name = 'Custom Cake'
        verbose_name_plural = 'Custom Cakes'

    def __str__(self):
        return self.custom_title

    def get_custom_url(self):
        return reverse("main:custom_menu", kwargs={'cslug': self.custom_slug})

class Custom_Orders(models.Model):
    ORDER_STATUS = (
        ('Ordered', 'Ordered'),
        ('Delivered', 'Delivered'),
        ('Cancelled','Cancelled'),
        ('Waiting for confirmation','Waiting for confirmation'),
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    custom_item = models.ForeignKey(CustomCakes, on_delete=models.CASCADE)
    custom_ordered = models.BooleanField(default=False,verbose_name='Ordered')
    quantity_in_kg = models.IntegerField(default=2)
    delivery_address = models.CharField(max_length=400,blank=True,verbose_name='Current Delivery Address')
    custom_total = models.IntegerField(default=0,verbose_name='Total Price')
    custom_instructions = models.CharField(max_length=400,blank=True,verbose_name='Instructions')
    custom_ordered_date = models.DateField(default=timezone.now,verbose_name='Ordered on')
    custom_status = models.CharField(max_length=40, choices=ORDER_STATUS, default='Waiting for confirmation',verbose_name='Order Status')
    custom_delivery_date = models.DateTimeField(default=timezone.now,verbose_name='Delivery Date')

    class Meta:
        verbose_name = 'Custom Order'
        verbose_name_plural = 'Custom Orders'

    def __str__(self):
        return self.custom_item.custom_title

    def save(self,*args,**kwargs):
        self.custom_total = self.custom_item.custom_price * self.quantity_in_kg
        super(Custom_Orders,self).save(*args,**kwargs)

class Reviews(models.Model):
    user = models.ForeignKey(Customer, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    rslug = models.SlugField()
    review = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.review

@receiver(pre_save, sender= CartItems,dispatch_uid='del_send')
def del_send(sender, instance,**kwargs):
    if instance.status == 'Delivered':
        user = instance.user
        sub = 'YOUR ORDER DELIVERED'
        msg = 'Hi %s Your order has been delivered' %(instance.user.first_name)
        frm_email = settings.EMAIL_HOST_USER
        to = [user.email]
        send_mail(sub, msg,frm_email,to)


@receiver(pre_save, sender= Custom_Orders,dispatch_uid='del_send')
def del_send(sender, instance,**kwargs):
    if instance.custom_status == 'Delivered':
        user = instance.user
        sub = 'YOUR CUSTOM ORDER DELIVERED'
        msg = 'Hi %s Your custom order has been delivered. Order Again !!!' %(instance.user.first_name)
        frm_email = settings.EMAIL_HOST_USER
        to = [user.email]
        send_mail(sub, msg,frm_email,to)