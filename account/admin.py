from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Account, Profile, Referral, Contact

# Inlines for Account and Contacts
# Inline for Profile and Referral


# class AdminPage(admin.AdminSite):
#     pass

class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact', 'user')


class ContactInline(admin.StackedInline):
    model = Contact
    fk_name = 'user'
    extra = 0


class RefAdmin(admin.ModelAdmin):
    list_display = ('user', 'used_by', 'used_on', 'is_used')
    list_display_links = ('user', 'used_by')
    readonly_fields = ('ref_code', 'used_on')
    fieldsets = (
        (_('User Detail'), {'fields': ('user', 'ref_code', 'is_used')}),
        (_('Used Detail'), {'fields': ('used_by', 'used_on')})
    )


class AccountAdmin(UserAdmin):
    field_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('date_joined', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_admin')
    fieldsets = (
        (_('Login Details'), {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (_('Types And Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Permissions'), {'fields': ('groups', 'user_permissions')}),
    )

    inlines = [ContactInline, ]

admin.site.site_header = 'Todos&Transactions'
admin.site.site_title = "Todos&Transactions Admin Portal"
admin.site.index_title = "Welcome to Totr"

admin.site.register(Account, AccountAdmin)
admin.site.register(Profile)
admin.site.register(Referral, RefAdmin)
admin.site.register(Contact, ContactAdmin)
