from django.db import models


from django.contrib.auth.models import PermissionsMixin, User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from PIL import Image
import uuid






# def get_profile_image_filepath(self):
#     return f'profile_images/{self.pk}/{"profile_image.png"}'

# def get_default_profile_image():
#     return 'images/avtar/1.jpg'
# # Create your models here. 


# class Reg_User(AbstractBaseUser):
# 	# name = models.CharField(max_length=100)
#     email = models.EmailField(verbose_name="email", max_length=90, unique=True)
#     username = models.CharField(max_length=30, unique = True) # help_text=("Required.150 characters or fewer. Letters, digits"))# error_messages={'unique':("A user with that username already exists. in the db")}) 
#     # password = models.CharField(max_length=45)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
#     last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     # profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default =  get_default_profile_image)
#     hide_email = models.BooleanField(default = True)


#     objects = MyAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

# #perms means permissions

#     def __str__(self):
#         return self.username


#     def get_profile_image_filename(self):
#         return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

#     def has_perm(self, perm, obj = None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True


class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    auth_token = models.CharField(max_length=100, default=False)
    password = models.CharField(max_length=45, default=False)
    c_password = models.CharField(max_length=45, default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
   
    def __str__(self):
        return self.user.username




class Add_Products(models.Model):
    product_title = models.CharField(max_length = 125, default = None)
    product_sku = models.CharField(max_length = 30, default = None)
    TECHNOLOGY = 'technology'
    FASHION = 'fashion'
    ACCESSORIES = 'accessory'
    PRODUCT_CATEGORIES = [
    (TECHNOLOGY, 'Technology'),
    (FASHION, 'Fashion'),
    (ACCESSORIES, 'Accessory'),
    ]
    product_categories = models.CharField(max_length=150, choices = PRODUCT_CATEGORIES, default=True)
    product_price = models.FloatField(default=True)
    product_summary = models.TextField(max_length=255, help_text="Input some information", verbose_name="Product Detail")
    product_status = models.BooleanField(default = False)
    product_description = models.TextField(max_length=255, default=False, help_text="Input some information", verbose_name="Product Detail")
    product_meta_title = models.CharField(max_length = 125, default = None)   
    product_meta_description = models.TextField(max_length=255, default=False, help_text="Input some information", verbose_name="Product Detail")



class Upload_Product(models.Model):
    def get_product_uploaded_image_filepath(self,upload_to):
        return f'product_upload_images/{self.product_categories}/{self.pk}/{"product_upload_local_image.png"}'
        # return "product_upload_images{/%Y/%m/%d/product_upload_local_image.png"

    def get_product_rating(self):
        pass


    product_name = models.CharField(max_length=255, default=None)
    # product_image = models.ImageField(upload_to = get_product_uploaded_image_filepath, max_length=255, null = True, blank = True, default = None)
    product_price = models.FloatField(default=True)
    is_discount_price = models.BooleanField(default=False)
    product_discount_price = models.FloatField(default=True)
    product_description = models.TextField(max_length=255, help_text="Input some information", verbose_name="Product Detail")
    product_local_image = models.FileField(upload_to=get_product_uploaded_image_filepath, max_length=300, default=False)

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

    # def is_upperclass(self):
    #     return self.product_size in {self.SMALL, self.LARGE}

    def is_upperclass(self):
        return self.product_color in {self.RED, self.GREEN}

    def __str__(self):
        return self.product_name


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