from django.db import models


from django.contrib.auth.models import PermissionsMixin, User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid







class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    auth_token = models.CharField(max_length=100, default=False)
    password = models.CharField(max_length=45, default=False)
    # c_password = models.CharField(max_length=45, default=False)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
    created_at = models.DateTimeField(auto_now_add = True)
   
    def __str__(self):
        return self.user.username





class UploadProduct(models.Model):
    def get_product_uploaded_front_image_filepath(self,upload_to):
        return f'product_upload_front_images/{self.product_categories}/{self.id}/product_upload_front_image.png'

    def get_product_uploaded_back_image_filepath(self,upload_to):
        return f'product_upload_back_images/{self.product_categories}/{self.id}/product_upload_back_image.png'
    


    product_name = models.CharField(max_length=255, default=None)
    product_price = models.FloatField(default=True)
    is_discount_price = models.BooleanField(default=False)
    product_discount_price = models.FloatField(default=True)
    product_description = models.TextField(max_length=255, help_text="Input some information", verbose_name="Product Detail")
    product_front_image = models.FileField(upload_to=get_product_uploaded_front_image_filepath, max_length=300, default=False)
    product_back_image = models.ImageField(upload_to = get_product_uploaded_back_image_filepath, max_length=255, null = True, blank = True, default = None)
    product_status = models.BooleanField(default = False)
    product_is_digital = models.BooleanField(default=False, null = True, blank = True)
    product_meta_title = models.CharField(max_length = 125, default = False, null = True, blank=True)   
    product_meta_description = models.TextField(max_length=255, default=False, help_text="Input some information", verbose_name="Product Detail")

    date_added = models.DateTimeField(auto_now_add = True)


    TECHNOLOGY = 'technology'
    FASHION = 'fashion'
    ACCESSORIES = 'accessory'
    PRODUCT_CATEGORIES = [
    (TECHNOLOGY, 'Technology'),
    (FASHION, 'Fashion'),
    (ACCESSORIES, 'Accessory'),
    ]
    product_categories = models.CharField(max_length=150, choices = PRODUCT_CATEGORIES, default=True)


    NORMAL = 'normal'
    SMALL = 'small'
    LARGE = 'large'
    PRODUCT_SIZE_CHOICES = [
    (SMALL, 'Small'),
    (NORMAL, 'Normal'),
    (LARGE, 'Large'),
    ]
    product_size = models.CharField(max_length=25, choices = PRODUCT_SIZE_CHOICES, default=NORMAL)


    # product_quantity = 
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    PRODUCT_COLOR_CHOICES = [
    (RED, 'Red'),
    (BLUE, 'Blue'),
    (GREEN, 'Green'),
    ]

    product_color = models.CharField(max_length=25, choices = PRODUCT_COLOR_CHOICES, default=RED)

    

    def is_upperclass(self):
        return self.product_color in {self.RED, self.GREEN}

    def __str__(self):
        return (f'({self.id}). Name of Product is {self.product_name} and the price is {self.product_price}')


    def get_product_rating(self):
        
        pass


    #Not needed code just for a reference

    # class CityAutoComp(autocomplete.Select2QuerySetView):
    #     def get_queryset(self):
    #         qs = City.objects.all()

    #         if self.q:
    #             qs = qs.filter(name___istartswith = self.q)
    #         return qs


MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
]




# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     name = models.CharField(max_length=255, default=None)
#     email = models.CharField(max_length=255, default=None)

#     def __str__(self):
#         return self.user.username
    


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length=255, null = True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(UploadProduct, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)



class ShippingAddress(models.Model):
    shipping_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    customer = models.ForeignKey(UserRegistration, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    address = models.CharField(max_length=255, null = False)
    city = models.CharField(max_length=255, null = False)
    state = models.CharField(max_length=255, null = False)
    zipcode = models.CharField(max_length=255, null = False)
    
    date_added = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.customer.user.username