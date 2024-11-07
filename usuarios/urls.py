from django.urls import path
from .views import UserList, UsuariosList

urlpatterns = [
    path('', UsuariosList.as_view(), name='user_list'),
    path('<str:email>/', UserList.as_view(), name='single_user_list')
]
