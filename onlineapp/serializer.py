from onlineapp.models import *
from rest_framework import serializers


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name', 'location', 'acronym','contact')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','dob','email','db_folder','dropped_out','college')

class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('id','problem1','problem2','problem3','problem4')

class StudentDetailsSerializer(serializers.ModelSerializer):
    mocktest1 = MockTestSerializer(read_only=False,many=False)

    class Meta:
        model = Student
        fields = ('id', 'name', 'dob', 'email', 'db_folder', 'dropped_out','mocktest1')

    def create(self,validated_data):
        mock_vals = validated_data.pop('mocktest1')
        mock = MockTest1(**mock_vals)

        student = Student(**validated_data)
        student.college_id =self.context['college_id']
        student.save()

        mock.total = 0
        for i in range(1, 5):
            mock.total += int(mock_vals['problem' + str(i)])
        mock.student = student
        mock.save()
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.email = validated_data.get('created', instance.email)
        instance.db_folder = validated_data.get('db_folder',instance.db_folder)
        instance.dropped_out = validated_data.get('dropped_out',instance.dropped_out)
        return instance



"""from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from onlineapp.models import College,Student,MockTest1


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name', 'location', 'acronym', 'contact')

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','dob','email','db_folder','dropped_out','college_id')

class MockTestSerializer(ModelSerializer):
    class Meta:
        model=MockTest1
        fields = ('id','problem1','problem2','problem3','problem4','total','student_id')

class StudentDetailsSerializer(ModelSerializer):
    mocktest = MockTestSerializer()
    class Meta:
        model = Student
        fields = ('id', 'name', 'dob', 'email', 'db_folder', 'dropped_out', 'college_id','mocktest')
    def create(self,validated_data,cpk):
        mock_data=validated_data.pop('mocktest')
        college = College.objects.get(id=cpk)
        student = Student.objects.create(college,**validated_data)
        mocktest = MockTest1.objects.create(student=student,**mock_data)
        mocktest.save()
        student.save()
        return student"""






