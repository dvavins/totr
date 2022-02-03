from django import forms

from tranx.models import Transactions


class AddTransactionForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = ['name', 'desc', 'amount', 'paid_on']
