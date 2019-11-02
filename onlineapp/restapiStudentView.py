from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from onlineapp.serializer import *
from onlineapp.models import *
from rest_framework.response import Response

class StudentSerializerView(APIView):

    def get(self,request,*args,**kwargs):
        college = College.objects.get(id=kwargs.get('pk'))

        if not kwargs.get('sk'):
            student = Student.objects.filter(college_id=college.id).all()
            serializer = StudentSerializer(student, many=True)
        else:
            # student = Student.objects.filter(college_id=college.id).get(id=kwargs.get('sk'))
            student = get_object_or_404(Student, id=kwargs.get('sk'))
            serializer = StudentSerializer(student)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        student = StudentDetailsSerializer(data=request.data,context={'college_id':kwargs.get('pk')})
        if student.is_valid():
            student.save()
            return Response(student.data,status=status.HTTP_201_CREATED)

    def delete(self, request, pk, sk, format=None):
        student = get_object_or_404(Student, pk=sk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk,sk, format=None):
        student = get_object_or_404(Student,id=sk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











"""from django.views import View
from pip._vendor.chardet.enums import MachineState
from rest_framework.response import Response
from rest_framework.views import APIView

from onlineapp.models import College,Student,MockTest1
from onlineapp.serializer import StudentSerializer,MockTestSerializer,StudentDetailSerializer


class restapiStudentView(APIView):

    def get(self,request,**kwargs):
        if (request.method == 'GET' and kwargs):
            student = Student.objects.get(college_id=kwargs)
            mocktest = MockTest1.objects.get(student=student)
            serializer = StudentSerializer(student)
            mock_serializer = MockTestSerializer(mocktest)
            serializer.data[0]['mocktest'] = mock_serializer.data
            return Response(serializer.data)
        if(request.method=='POST'):
            pass
        college=College.objects.get(**kwargs)
        students = Student.objects.filter(college=college)
        serializer = StudentSerializer(students, many=True)
        for stu in range(0,len(students)):
            mocktest = MockTest1.objects.get(student=students[stu])
            mock_serializer=MockTestSerializer(mocktest)
            serializer.data[stu]['mocktest'] = mock_serializer.data
        return Response(serializer.data)


    def post(self,request,**kwargs):
        mocktest=MockTestSerializer()"""






