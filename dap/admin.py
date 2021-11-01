from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *
# # Register your models here.

# # admin.site.register(Reg_User, UserAdmin)
# # admin.site.register(Reg_User)

# class Reg_User_Admin(UserAdmin):
# 	"""docstring for Reg_User"""
# 	list_display = ('email', 'username', 'created_at', 'last_login', 'is_admin', 'is_staff')
# 	search_fields = ('email', 'username')
# 	readonly_fields = ('id', 'date_joined', 'last_login')
# 	filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()


# admin.site.register(Reg_User, Reg_User_Admin)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Reg_User
    list_display = ('email', 'username', 'date_joined', 'last_login','is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    readonly_fields = ('id', 'date_joined', 'last_login')

    class Media:
        js = ('js/placeholder.js',)
        css = {
            'all': ('css/admin.css',)
        }




admin.site.register(Reg_User, CustomUserAdmin)

admin.site.register(Upload_Product)

admin.site.register(Add_Products)

# class UserAdmin(admin.ModelAdmin):
#     form = UserLogForm