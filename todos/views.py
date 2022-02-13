from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


from todos.models import Todos
from todos.forms import AddTodoForm


@login_required(login_url='account:signin')
def addtodo(request):
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            data = Todos()
            data.user = request.user
            data.name = form.cleaned_data['name']
            data.desc = form.cleaned_data['desc']
            data.todo_date = form.cleaned_data['todo_date']
            data.is_completed = form.cleaned_data['is_completed']
            data.save()
            return redirect('/account/dashboard')
    else:
        form = AddTodoForm()
    context = {'form': form}
    return render(request, 'todos/addtodo.html', context)


@login_required(login_url='account:signin')
def viewtodos(request):
    try:
        todos_items = Todos.objects.filter(user=request.user)
    except ObjectDoesNotExist:
        pass

    context = {
        'todos_items': todos_items
    }
    return render(request, 'todos/viewtodos.html', context)


@login_required(login_url='account:signin')
def tododetail(request, todo_name):
    item = Todos.objects.get(user=request.user, slug=todo_name)
    context = {
        'todo': item,
    }
    return render(request, 'todos/detailtodo.html', context)


@login_required(login_url='account:signin')
def deletetodo(request, todo_name):
    item = Todos.objects.get(user=request.user, slug=todo_name)
    item.delete()
    return redirect('/todos/view/')


# Add option for update todo

