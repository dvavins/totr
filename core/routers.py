from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter, Route, DynamicRoute


from account.api.viewsets import AccountsViewset
from todos.api.viewsets import TodosViewset
from tranx.api.viewsets import TranxViewset


# class CustomRouter(SimpleRouter):
#     routes = [
#         Route(
#             url = r'^{prefix}$',
#             mapping={'get':'list'},
#             name='{basename}-list',
#             detail=False,

#         ),
#     ]




router = DefaultRouter()
router.register('account', AccountsViewset, basename='acount_api')
router.register('todos', TodosViewset, basename='todo_api')
router.register('tranx', TranxViewset, basename='tranx_api')