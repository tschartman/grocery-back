from visits.models import Visit
from visits.serializers import VisitSerializer
from rest_framework import generics


class VisitList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a grocery visit.
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer