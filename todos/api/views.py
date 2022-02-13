from rest_framework.decorators import (
    api_view, renderer_classes, authentication_classes, permission_classes
)
from rest_framework.response import Response
from rest_framework.renderers import(
    BrowsableAPIRenderer
)
from account.models import Account

from todos.api.serializer import TodoCreateSerailizer, TodoSerializer, TodoTeamSerializer
from todos.models import Todos





@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'Endpoint':'/view/',
        'method': 'GET',
        'body': None,
        'description': 'Return an array of todos'
        },
        {'Endpoint':'/view/id/',
        'method': 'GET',
        'body': None,
        'description': 'Return a single todo object'
        },
        {'Endpoint':'/create/',
        'method': 'POST',
        'body': {'body': ""},
        'description': 'Creates new todos with post request'
        },
        {'Endpoint':'/view/id/update/',
        'method': 'PUT',
        'body': {'body': ""},
        'description': 'Updates existing todo with post request'
        },
        {'Endpoint':'/view/id/delete/',
        'method': 'DELETE',
        'body': {'body': ""},
        'description': 'Delete todo from the database'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def viewTodos(request):
    todos = Todos.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailView(request, pk):
    todos = Todos.objects.get(id=pk)
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
# @renderer_classes([BrowsableAPIRenderer])
def createTodo(request, format=None):

    if request.method == 'POST':
        request.data["user"] = Account.username
        serializer = CreateTodoSerailizer(data=request.data)
        data = {}
        if serializer.is_valid():
            todo = serializer.save()
            data['response'] = 'Successfully added'
            data['title'] =  todo.title
            data['username'] = todo.user
        else:
            data = serializer.errors
        return Response(data)

def updateTodo(request):
    pass

def deleteTodo(request):
    pass




@api_view(['POST'])
def createTeam(request):
    if request.method == 'POST':
        serializer = TodoTeamSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            team = serializer.save()
            data['status'] = 'Team successfullt created'
        else:
            data = serializer.errors
        return Response(data)
