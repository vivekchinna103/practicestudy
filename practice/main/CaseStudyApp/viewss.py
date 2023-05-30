from django.http import JsonResponse
from casestudy.cognitivesearch.oDatfilter import oDataFilter
from django.shortcuts import render
from operator import inv
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from CaseStudyApp.models import CaseStudies
from django.core.files.storage import default_storage
from CaseStudyApp.Serializers import CaseStudySerializers
from rest_framework import generics
import json, os
#from casestudy.connectdb import get_all,get_file,get_row,update_data,add_data
#import ssl
#os.environ['REQUESTS_CA_BUNDLE']= r'C:\Users\10710591\AppData\Local\Programs\Python\Python311\Lib\site-packages\certifi\cacert.pem'
@csrf_exempt
def filter_endpoint(request):
    if request.method=="POST":
        body_content = request.body.decode('utf-8')
        body_content=json.loads(body_content)
        vertical = body_content.get('Vertical')
        account = body_content.get('Account')
        service_offering_mapping = body_content.get('ServiceOfferingMapping')
        metadata = body_content.get('MetaData')
        rating = body_content.get('Rating')
        if vertical!=None:
            vertical= str(vertical)
        else:
            vertical=None
        if account!=None:
            account= str(account)
        else: 
            account=None
        if service_offering_mapping!=None:
            service_offering_mapping= str(service_offering_mapping)
        else:
            service_offering_mapping=None
        if metadata!=None:
            metadata= str(metadata)
        else:
            metadata=None
        if rating!=None:
            rating= str(rating)
        else:
            rating=None
    #service_offering_mapping = body_content.get('ServiceOfferingMapping', None)
    #metadata = body_content.get('MetaData', None)
    #rating = body_content.get('Rating', None)
    # Call the oDataFilter function passing the filter parameters
        filtered_data = oDataFilter(account,vertical,service_offering_mapping,metadata,rating)
    # Return the filtered data as a JSON response
        #ssl._create_default_https_context = ssl._create_unverified_context
        return JsonResponse(json.loads(filtered_data),safe=False)
    else:
        return JsonResponse("error :invalid request method",status=405,safe=False)
@csrf_exempt
def get_case_id(request,id):
    if request.method=="GET":
        product=CaseStudies.objects.get(id=id)
        product_serializer= CaseStudySerializers(product)
        return JsonResponse(product_serializer.data,safe=False)
@csrf_exempt
def get_all_cases(request):
    if request.method=="GET":
        product= CaseStudies.objects.all()
        product_serializer= CaseStudySerializers(product,many=True)
        return JsonResponse(product_serializer.data, safe=False)
@csrf_exempt
def newapi(request):
    if request.method=="POST":
        return JsonResponse("MEssage received is " ,safe=False)
