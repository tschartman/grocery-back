from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from visits.models import Visit
from visits.serializers import VisitSerializer

# Create your views here.
@csrf_exempt
def visit_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VisitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def visit_detail(request, pk):
    """
    Retrieve, update or delete a grocery visit.
    """
    try:
        visit = Visit.objects.get(pk=pk)
    except Visit.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VisitSerializer(visit)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VisitSerializer(visit, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        visit.delete()
        return HttpResponse(status=204)