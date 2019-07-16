from visits.models import Visit
from visits.serializers import VisitSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from visits.serializers import UserSerializer
from visits.permissions import IsOwnerOrReadOnly


class VisitList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a grocery visit.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer