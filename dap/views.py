from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.views.generic import *
from dap.models import *
from rest_framework import generics
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
import uuid
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

# content_type = ContentType.objects.get_for_model(Upload_Product)
# permission = permission.objects.create(
#     codename = {can_add_product: 'can_add_product', can_delete_product: 'can_delete_product'}

#     content_type = content_type
#     )


# Create your views here.
class LoginUserView(View):
    def get(self, request):
        if request.method != 'POST':
            return render(request, 'html/login.html')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username).first()

        if user is None:
            messages.success(request, 'User not found.')
            return redirect('/login')

        profile_obj = UserRegistration.objects.filter(user = user).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        user = authentication(username = username or email, password = password)

        if user is None:
            messages.success(request, 'Wrong username or password.')
            return redirect('/login')

        login(request, user)

        return redirect('/index')


class RegisterUserView(View):

    def get(self, request):
        template_name = "html/register.html"
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        if request.method != 'POST':
            return
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username  = request.POST.get('uname')
        email = request.POST['email']
        password = request.POST['password']
        # c_password = request.POST['c_password']

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken')
                return redirect('/register')
            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken')
                return redirect('/register')
            # if User.objects.filter(password1 == password2).first():
            #     messages.success(request, 'password does not match')
            #     return redirect('/register')


            user = User(username = username, email = email)
            user.set_password(password)
            # user.set_password(c_password)
            user.save()
            current_site = get_current_site(request)
            auth_token = str(uuid.uuid4())
            profile_obj = UserRegistration.objects.create(user = user, auth_token = auth_token)
            # profile_obj.set_password(password)
            # profile_obj.set_password(c_password)
            # profile_obj.check_password(password)
            profile_obj.save()

            send_mail_after_registration(email, auth_token)


            # return redirect('/token')

        except Exception as e:
            print(e)

        return redirect('/token')

    def send_mail_after_registration(self, token):
        subject = 'Your accounts need to be verified'
        message = f' you are re receiving this email because you requested a password reset for your user account at Kiosk Please go to the following page and choose a new password: Hi paste the link to verify your account https://127.0.0.1:8000/verify/{token} Thanks for using our site. The Kiosk team'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self]
        send_mail(subject, message, email_from, recipient_list)


    def verify(self, request, auth_token):
        try:
            if profile_obj := UserRegistration.objects.filter(
                auth_token=auth_token
            ).first():
                success_message = "Your Account has been verified."
                if profile_obj.is_verified:
                    verify_message = "Your Account is been verify"
                    messages.success(request, verify_message)
                    return redirect('/login')

                else:
                    error_message = "Your Account creation was not successful, Please check your input"
                    messages.success(request, error_message)
                    return redirect('/register')

        except Exception as e:
                print(e)




class BaseView(View):
    """docstring for BaseView"""
    def get(self, request):
        template_name = 'html/recom/base.html'
        product_objects = UploadProduct.objects.all()     

        product_name = request.GET.get('product_name')
        context = {
            'product_objects': product_objects
        }
        if product_name !='' and product_name is not None:
            product_objects = product_objects.filter(title__icontains=product_name)

        return render(request, template_name, context)


class CartHomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer = customer, complete = False)
            items = order.orderitem_set.all()

        else:
            items = []
            template_name = 'html/cart.html'
        context = {
            'items': items
        }
        return render(request, template_name, context)


class HomeView(View):
    # @login_required(login_url = 'login.html')
    def get(self, request):

        template_name = 'html/index.html'
        context = {
        }
        return render(request, template_name, context)


class ShopView(View):
    def get(self, request):
        template_name = 'html/shop.html'
        model = {
        UploadProduct,
        }

        paginate_by = 100
        # product_details = get_object_or_404(UploadProduct)

        products = UploadProduct.objects.all()



        context = {
            'products': products,
            'error_message': "No Product was found",
        }



        return render(request, template_name, context)


# class DefaultView(View):
#     def get(self, request):
#         template_name = "html/index.html"
#         context = {}

#         return render(request, template_name, context)

class Error404View(View):
    def get(self, request):
        template_name = 'html/404.html'
        context = {}

        return render(request, template_name, context)

class AboutView(View):
    def get(self, request):
        template_name = 'html/about.html'
        context = {}

        return render(request, template_name, context)


class ProductPageView(View):
    def get(self, request):
        template_name = 'html/productPage.html'
        context = {}

        return render(request, template_name, context)


# class LoginFormView(edit.FormView):
#     form_class = FileFieldForm
#     template_name = '/dapbestreact/login.html'


# class LoginListCreate(generics.ListCreateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer




def token_send(request):
    return render(request, 'html/token_send.html')


def forget_password(request):
    return render(request, 'html/forget-pwd.html')

def email_verified(request):
    return render(request, 'html/email_verified.html')



# ADMIN VIEW LIST
class AdminLoginView(View):
    def get(self, request):
        template_name = 'admin/login.html'
        context = {
            'success': "You have successfully login",
        }


        u_name = user.objects.get(username)
        pword = Reg_User.objects.get(password)
        username = request.POST['username']
        password = request.POST['password']



        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('html/index.html')
        else:
            # Return an 'invalid login' error message.
            return "not found"
        # return HttpResponseRedirect(reverse('html/index.html'))
        return render(request, template_name, context)


    @login_required(login_url = 'admin/login.html')
    def user_limit(self):
        if not self.user.is_authenticated:
            next = 'html/index.html'
            # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
            return redirect_to_login(next, login_url, redirect_field_name = 'next')
        else:
            print('An Error has occur')

def login_view(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #     ...
    # else:
    #     # Return an 'invalid login' error message.
    #     return "Not found"

    # if request.method == 'GET':
    #     login(request, user)


    return render(request, 'admin/login.html')

class AdminHomeView(View):
    def get(self, request):
        template_name = 'admin/home.html'
        context = {}

        return render(request, template_name, context)



class AdminProfileView(View):
    def get(self, request):
        template_name = 'admin/profile.html'
        context = {}

        return render(request, template_name, context)


def logout_view(request):
    logout(request)


class AddDigitalProductView(View):
    def get(self, request):
        template_name = 'admin/add-digital-product.html'
        context = {}

        return render(request, template_name, context)




# def change_password(request):
#     if request.method == 'POST':
#         form = passwordChangeForm(user = request.user, data=request.POST)

#         if form.is_valid():
#             form.save()

#             update_session_auth_hash(request, form.user)
#             success_message = "Congrats {}, Your password was updated Successfully"
#             messages.success(request, success_message.format(request.user))
#             return redirect("/admin")

#         else:
#             error_message = "Please cross check the error below"
#             messages.error(request, error_message)
#             return redirect("/")

#     else:
#         form = PasswordChangeForm(user = request.user)
#         template_name = 'change.html'
#         context = {
#             "form": form
#         }
#         return render(request, template_name, context)