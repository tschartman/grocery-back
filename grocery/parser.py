from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

@csrf_exempt
def parse(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'])
        return HttpResponse('image upload success')

    return HttpResponseForbidden('allowed only via POST')

def handle_uploaded_file(f):
    with open("C:/Users/tschartman/vue/grocery-back/grocery-back/grocery/files/file.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)