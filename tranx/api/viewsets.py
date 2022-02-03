from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from tranx.models import Transactions
from tranx.api.serializers import TranxSerializer, TranxViewSerializer, TranxCreateSerializer


class TranxViewset(viewsets.ModelViewSet):

    queryset = Transactions.objects.all()
    serializer_class = TranxSerializer

    authentication_classes = (SessionAuthentication, TokenAuthentication)


    def get_serializer_class(self):
        if self.action == 'list':
            return TranxViewSerializer
        if self.action == 'retrieve':
            return TranxViewSerializer
        if self.action == 'create':
            return TranxCreateSerializer
        if self.action == 'update':
            return TranxCreateSerializer
        return TranxSerializer


    # def get_authenticators(self):
    #     if self.action == 'list':
    #         return TokenAuthentication
    #     return []
    
    # def get_object(self, queryset=None, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     return get_list_or_404(Transactions, user=pk)



    def list(self, request, ):
        self.queryset = Transactions.objects.all()
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


    # def create(self, request):
    #     self.serializer_class = TranxCreateSerializer
    #     self.serializer = TranxCreateSerializer(data=request.data)
    #     data = {}
    #     if self.serializer.is_valid():
    #         tranx = self.serializer.save()
    #         data['response'] = 'Successfully added'
    #         data['title'] = tranx.title
    #         data['user'] = tranx.user
    #     else:
    #         data = self.serializer.errors
    #     return Response(data)

    @action(methods=['GET'], detail=False)
    def pruser(self, request, user):
        user = request.data[user]
        return Response(user)

    @action(methods=['GET',], detail=False,)
    def helps(self, request):
        routes = [
            {
            'endpoint':'/view/',
            'authentication needed': 'Yes',
            'method': 'GET',
            'description': 'Return an array of transactions.'
            },
            {
            'endpoint':'/view/id/',
            'authentication needed': 'Yes',
            'method': 'GET',
            'description': 'Return a detailed view of transaction.'
            },
            {
            'endpoint':'/create/',
            'authentication needed': 'Yes',
            'method': 'POST',
            'description': 'Add new transaction with post request.'
            },
            {
            'endpoint':'/view/id/update/',
            'authentication needed': 'Yes',
            'method': 'PUT',
            'description': 'Updates details of transaction with post request.'
            },
            {
            'Endpoint':'/view/id/delete/',
            'authentication needed': 'Yes',
            'method': 'DELETE',
            'description': 'Delete transaction history.'
            }
        ]
        return Response(routes)