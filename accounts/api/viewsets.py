from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import Account
from accounts.api.serializer import (AccountSerializer, AccountViewSerializer,
                                     CreateAccountSerializer, )


class AccountsViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return AccountSerializer
        if self.action == 'create':
            return CreateAccountSerializer
        if self.action == 'retrieve':
            return AccountViewSerializer
        if self.action == 'update':
            return AccountViewSerializer
        return AccountSerializer



    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many = True)
    #     return Response(serializer.data)


    def create(self, request):
        self.serializer_class = CreateAccountSerializer
        self.serializer = CreateAccountSerializer(data=request.data)
        data = {}
        if self.serializer.is_valid():
            account = self.serializer.save()
            data['response'] = 'Successfully added'
            data['name'] =  f'{account.first_name} {account.last_name}'
            data['username'] = account.username
        else:
            data = self.serializer.errors
        return Response(data)


    # def retrieve(self, request, pk):
    #     # if request.method == 'GET':
    #     self.serializer_class = CreateAccountSerializer
    #     self.queryset = Account.objects.get(id=pk)
    #     serializer = self.serializer_class(self.queryset, many=False)
    #     return Response(serializer.data)


#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass