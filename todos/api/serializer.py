from rest_framework import serializers

from todos.models import Todos
from account.models import Account


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ('id', 'title', 'user', 'is_completed')


class TodoViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todos
        fields = '__all__'


class TodoCreateSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Todos
        fields = ('title', 'user', 'desc', 'todo_date', 'is_completed',)

    def save(self):
        todo = Todos(
            title = self.validated_data['title'],
            user = self.validated_data['user'],
            desc = self.validated_data['desc'],
            todo_date = self.validated_data['todo_date'],
            is_completed = self.validated_data['is_completed'],
        )
        todo.save()
        return todo


