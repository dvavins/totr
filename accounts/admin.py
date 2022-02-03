from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Account




class AccountAdmin(UserAdmin):
    field_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username', 'email')

    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()

    list_filter = ('is_staff', 'is_admin', 'is_active')


    fieldsets = (
        (_('Login Details'), {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (_('Types And Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin' )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Permissions'), {'fields': ('groups', 'user_permissions')}),
    )


admin.site.site_header = 'Todos&Transactions'
admin.site.site_title = "Todos&Transactions Admin Portal"
admin.site.index_title = "Welcome to Totra"

admin.site.register(Account, AccountAdmin)
