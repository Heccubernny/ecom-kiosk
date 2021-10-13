from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.views.generic import *
from .models import *
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



# content_type = ContentType.objects.get_for_model(Upload_Product)
# permission = permission.objects.create(
#     codename = {can_add_product: 'can_add_product', can_delete_product: 'can_delete_product'}

#     content_type = content_type
#     )


# Create your views here.
class LoginUserView(View):
    def get(self, request):
        return render(request, 'html/login.html')


class RegisterUserView(View):
    def get(self, request):
        template_name = "html/register.html"
        context = {}
        return render(request, template_name, context)

class BaseView(View):
    """docstring for BaseView"""
    def get(self, request):
        template_name = 'html/recom/base.html'
        product_objects = Upload_Product.objects.all()     

        product_name = request.GET.get('product_name')
        context = {
            'product_objects': product_objects
        }
        if product_name !='' and product_name is not None:
            product_objects = product_objects.filter(title__icontains=product_name)

        return render(request, template_name, context)

class HomeView(View):
    def get(self, request):
        template_name = 'html/index.html'
        context = {
        }
        return render(request, template_name, context)


class ShopView(View):
    def get(self, request):
        template_name = 'html/shop.html'
        # model = {
        # Upload_Product,
        # }

        # paginate_by = 100
        # product_details = get_object_or_404(Upload_Product)


        context = {
            # 'product_details': product_details,
            # 'error_message': "No Product was found",
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


# ADMIN VIEW LIST
class AdminLoginView(View):
    def get(self, request):
        template_name = 'admin/login.html'
        context = {
            'success': "You have successfully login",
        }

        
        u_name = Reg_User.objects.get(username)
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
            pass

        # return HttpResponseRedirect(reverse('html/index.html'))
        return render(request, template_name, context)


    @login_required(login_url = 'admin/login.html')
    def user_limit(request):
        next = 'html/index.html'
        if not request.user.is_authenticated:
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

class AdminIndexView(View):
    def get(self, request):
        template_name = 'admin/index.html'
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