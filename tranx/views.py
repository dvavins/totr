from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from tranx.models import Transactions
from tranx.forms import AddTransactionForm

@login_required(login_url='account:signin')
def addtranx(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            data = Transactions()
            data.user = request.user
            data.name = form.cleaned_data['name']
            data.desc = form.cleaned_data['desc']
            data.paid_on = form.cleaned_data['paid_on']
            data.amount = form.cleaned_data['amount']
            data.save()
            return redirect('/account/dashboard')
    else:
        form = AddTransactionForm()
    return render(request, 'tranx/addtranx.html', context={'form': form})


@login_required(login_url='account:signin')
def viewtranx(request):
    try:
        tranx_items = Transactions.objects.filter(user=request.user)
    except ObjectDoesNotExist:
        pass
    context={
        'tranx_items': tranx_items
    }
    return render(request, 'tranx/viewtranx.html', context)



@login_required(login_url='account:signin')
def detailtranx(request, tranx_name):
    item = Transactions.objects.get(user=request.user, slug=tranx_name)
    context = {
        'item': item
    }
    return render(request, 'tranx/detailtranx.html', context)
