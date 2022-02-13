# # from django.contrib.auth.decorators import login_required

# from rest_framework.response import Response
# from rest_framework.renderers import BrowsableAPIRenderer
# from rest_framework.decorators import (api_view, authentication_classes, permission_classes, 
#                                     renderer_classes, parser_classes, throttle_classes)
# from rest_framework.throttling import (AnonRateThrottle, BaseThrottle, 
#                             ScopedRateThrottle, SimpleRateThrottle, UserRateThrottle)
# from account.models import Account




# from tranx.models import Transactions
# from tranx.api.serializers import CreateTranxSerializer, TranxSerializer, TranxViewSerializer


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#         'endpoint':'/view/',
#         'authentication needed': 'Yes',
#         'method': 'GET',
#         'description': 'Return an array of transactions.'
#         },
#         {
#         'endpoint':'/view/id/',
#         'authentication needed': 'Yes',
#         'method': 'GET',
#         'description': 'Return a detailed view of transaction.'
#         },
#         {
#         'endpoint':'/create/',
#         'authentication needed': 'Yes',
#         'method': 'POST',
#         'description': 'Add new transaction with post request.'
#         },
#         {
#         'endpoint':'/view/id/update/',
#         'authentication needed': 'Yes',
#         'method': 'PUT',
#         'description': 'Updates details of transaction with post request.'
#         },
#         {
#         'Endpoint':'/view/id/delete/',
#         'authentication needed': 'Yes',
#         'method': 'DELETE',
#         'description': 'Delete transaction history.'
#         }
#     ]
#     return Response(routes)


# @api_view(['GET'])
# def viewTranx(request):
#     tranx = Transactions.objects.all()
#     serializer = TranxSerializer(tranx, many=True)
#     return Response(serializer.data)


# @api_view(['GET',])
# def detialView(request, pk):
#     tranx = Transactions.objects.get(id=pk)
#     serializer = TranxViewSerializer(tranx, many=False)
#     return Response(serializer.data)


# # def updateTranx(request):
    
# @api_view(['POST'])
# def addTranx(request, format=None):

#     if request.method == 'POST':
#         print(request.data['user'])
#         print(request.data['user'])
#         print(request.data['user'])
#         print(request.data['user'])
#         print(request.data['user'])
#         serializer = CreateTranxSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             tranx = serializer.save()
#             data['status'] = 'Transaction added successfully'
#             data['title'] = tranx.title
#         else:
#             data = serializer.errors
#         return Response(data)
