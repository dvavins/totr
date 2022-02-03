from django import forms
from todos.models import Todos


class AddTodoForm(forms.ModelForm):

    class Meta:
        model = Todos
        fields = ['name', 'desc', 'todo_date', 'is_completed']
