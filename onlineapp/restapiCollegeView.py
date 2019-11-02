from rest_framework.decorators import api_view, renderer_classes,authentication_classes,permission_classes
from onlineapp.models import College
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from onlineapp.serializer import CollegeSerializer

@api_view(['GET','POST'])
#@authentication_classes((SessionAuthentication,BasicAuthentication,TokenAuthentication))
#@permission_classes((IsAuthenticated,))
#@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def api_college_view(request,*args,**kwargs):
    if(request.method=='GET'):
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges,many=True)
        return Response(serializer.data)
    elif(request.method=='POST'):
        serializer = CollegeSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_CREATED)

@api_view(['GET','DELETE','PUT'])
#@authentication_classes((SessionAuthentication, BasicAuthentication,TokenAuthentication))
#@permission_classes((IsAuthenticated,))
def api_college_detail_view(request,*args,**kwargs):
    if (request.method == 'GET'):
        if (kwargs):
            college = College.objects.get(**kwargs)
            serializer = CollegeSerializer(college)
            return Response(serializer.data)
    elif(request.method=='DELETE'):
        College.objects.get(**kwargs).delete()
        return Response("College Deleted")
    elif(request.method=='PUT'):
        college = College.objects.get(**kwargs)
        serializer = CollegeSerializer(college,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
        return Response("College Updated")




