from contextlib import _RedirectStream
from django.shortcuts import render
from Adminpanel.models import adminpanel
from django.http import HttpResponse
from django.contrib import messages


from rest_framework.decorators import api_view
from rest_framework.response import Response
from Adminpanel.serializers import adminserializer

def index(request):
    return render(request,"adminindex.html")


def signin(request):
    return render(request,"signin.html")

    
@api_view(['GET'])
def signup(request):
     if request.method == "POST":
        en=adminpanel(admin_name=request.POST.get('fname'),admin_email=request.POST.get('email'),
        admin_pass=request.POST.get('pass'))
        en.save()  
        messages.success(request, "success")
   

     return render(request,"signup.html")

def signout(request):
   pass


@api_view(['GET'])
def apiOverview(request):
    admin = adminpanel.objects.all()
    serializer = adminserializer(admin,many= True)   
    return Response(serializer.data)
    
    
@api_view(['GET'])
def apidetail(request,pk):
    admin = adminpanel.objects.get(admin_id = pk)
    serializer = adminserializer(admin,many= False)   
    return Response(serializer.data)



@api_view(['POST'])
def admincreate(request):
    serializer = adminserializer(data = request.data)
    if  serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    
@api_view(['POST'])
def adminupdate(request,pk):
    admin = adminpanel.objects.get(admin_id = pk)
    serializer = adminserializer(instance=admin,data = request.data)
    if  serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(['DELETE'])
def admindelete(request,pk):
    admin = adminpanel.objects.get(admin_id = pk)
    admin.delete()
    return Response()