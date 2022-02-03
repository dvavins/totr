from rest_framework import viewsets

from todos.models import Todos
from todos.api.serializer import TodoSerializer, TodoCreateSerailizer, TodoViewSerializer


class TodosViewset(viewsets.ModelViewSet):

    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TodoSerializer
        if self.action == 'create':
            return TodoCreateSerailizer
        elif self.action == 'retrieve':
            return TodoViewSerializer
        return TodoSerializer