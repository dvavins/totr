from rest_framework.decorators import (
    api_view, renderer_classes, authentication_classes, permission_classes
)
from rest_framework.response import Response
from rest_framework.renderers import(
    BrowsableAPIRenderer
)


from accounts.models import Account
from accounts.api.serializer import AccountSerializer, CreateAccountSerializer




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
def viewAccounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailView(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account, many=False)
    return Response(serializer.data)


@api_view(['POST'])
# @renderer_classes([BrowsableAPIRenderer])
def createAccount(request, format=None):

    if request.method == 'POST':
        serializer = CreateAccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully added'
            data['name'] =  f'{account.first_name} {account.last_name}'
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)



def updateTodo(request):
    pass

@api_view(['DELETE'])
def deleteTodo(request, pk):
    
    if request.method == 'DELETE':
        account = Account.objects.get(id=pk)
        data = {}
        




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
