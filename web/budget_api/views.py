# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.views.generic import CreateAPIView, RetrieveAPIView
from rest_framework import generics
from .serializers import UserSerializer, User


class RegisterApiView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# class BudgetApiView(generics.RetrieveAPIView):
#     permission_classes = ''
#     serializer_class = UserSerializer

#     queryset = Budget.objects.filter(id=self.kwargs['pk'])
#     serializer_class = Group


# class TransactionApiView(generics.RetrieveAPIView):
#     permission_classes = ''
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         return Transaction.objects.filter(id=self.kwargs['pk'])
