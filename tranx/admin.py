from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Transactions

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount', 'date_created')
    list_display_links = ('name', 'user')

    search_fields = ('name', 'desc',)
    readonly_fields = ('date_created', 'slug')
    filter_horizontal = ()
    
    fieldsets = (
        (_('Done By'), {'fields': ('user',)}),
        (_('Transaction Details'), {'fields': ('name', 'slug', 'amount','desc')}),
        (_('Important dates'), {'fields': ('paid_on','date_created',)}),
    )


admin.site.register(Transactions, TransactionAdmin)
