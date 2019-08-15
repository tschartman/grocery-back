from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import requests
import urllib.request
import time
import json
import re
from bs4 import BeautifulSoup

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

@csrf_exempt
def parse(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'])
        return HttpResponse(parse_image("C:/Users/tschartman/vue/grocery-back/grocery-back/grocery/files/file.png"))

    return HttpResponseForbidden('allowed only via POST')

def handle_uploaded_file(f):
    with open("C:/Users/tschartman/vue/grocery-back/grocery-back/grocery/files/file.png", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def parse_image(url):
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

    # Simple image to string
    receiptArr = pytesseract.image_to_string(Image.open(url))
    #find the index of the amount of items (should be direclty after the word SOLD)
    index = receiptArr.split(' ').index("SOLD") + 1
    coupons = len(re.findall(r"COUPON", receiptArr))
    #try to parse the amount of items as an int
    #coupons are shown directly under so include them 
    items = int(re.findall(r"[0-9]*", receiptArr.split(' ')[index])[0]) + coupons
  
    barcodeArr = re.findall(r"[0-9]{12}", receiptArr)    
    itemsarr = []
    for i in range(0, items):
        url = 'https://www.walmart.com/search/?query=' + barcodeArr[i]
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        data = json.loads(soup.find(id='searchContent').string)
        
        try:
            data = data['searchContent']['preso']['items'][0]
            itemsarr.append({
                        'brand': data['brand'][0], 
                        'name' : data['seeAllName'],
                        'department' : data['department'],
                        'image' : data['imageUrl'],
                        'link' : data['productPageUrl']
                        })
        except IndexError:
            itemsarr.append({
                        'brand': "", 
                        'name' : "",
                        'department' : "",
                        'image' : "",
                        'link' : ""
                        })
    return JsonResponse({'items': itemsarr})