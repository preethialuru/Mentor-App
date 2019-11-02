from django.contrib.auth.models import User
from django.views import View
from onlineapp.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django import forms
from django.shortcuts import render, redirect
from onlineapp.forms.colleges import *
from onlineapp.forms.Auth import *
from django.urls import resolve
from django.http import *


def my_first_view(request):
    return HttpResponse("my first response\n")

class CollegeView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        if kwargs:
            college = College.objects.get(**kwargs)
            students = Student.objects.filter(college=college).order_by("-mocktest1__total")
            return render(request, template_name="college_details.html",
                          context={'college': college, 'students': students, 'title': 'All Colleges | MentorApp'})
        colleges=College.objects.all()
        return render(request,template_name="colleges.html",context={'jails':colleges,'user_permissions':request.user.get_all_permissions(),
                                                                     'title':'All Colleges | MentorApp'})

class AddCollegeView(LoginRequiredMixin,View):
  #  login_url='/login/'
    def get(self,request,*args,**kwargs):
        if resolve(request.path_info).url_name == 'edit_college':
            college=College.objects.get(id=kwargs.get('pk'))
            form=AddCollege(instance=college)
            return render(request,template_name='form.html',context={'form1':form})
        if resolve(request.path_info).url_name == 'delete_college':
            College.objects.get(id=kwargs.get('pk')).delete()
            return redirect('/onlineapp/colleges')
        form = AddCollege()
        return render(request,template_name="form.html",context={'form1':form,'title':'Add College | MentorApp',
                                                                 'user_permissions':request.user.get_all_permissions(),})
    def post(self,request,**kwargs):
        if resolve(request.path_info).url_name == 'edit_college':
            college=College.objects.get(**kwargs)
            form = AddCollege(request.POST,instance=college)
            if form.is_valid():
                form.save()
            return redirect('/onlineapp/colleges')
        form=AddCollege(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/onlineapp/colleges')
        return render(request,template_name='onlineapp/colleges.html',context={'form':form,'user_permissions':request.user.get_all_permissions(),
                                                                               'title':'Add College | Mentor App'})

class AddStudentView(LoginRequiredMixin,View):
   # login_url = 'login/'
    def get(self,request,**kwargs):
        if resolve(request.path_info).url_name == 'edit_student':
            college=College.objects.get(id=kwargs.get('pk1'))
            student=Student.objects.filter(college=college).get(id=kwargs.get('pk2'))
            mocktest=MockTest1.objects.get(student=student)
            student_form=AddStudent(instance=student)
            mocktest_form=MockTest(instance=mocktest)
            return render(request,template_name='studentform.html',context={'form1':student_form,'form2':mocktest_form,
                                                                            'user_permissions':request.user.get_all_permissions(),})
        if resolve(request.path_info).url_name == 'delete_student':
            college=College.objects.get(id=kwargs.get('pk1'))
            student=Student.objects.filter(college=college).get(id=kwargs.get('pk2'))
            student.delete()
            mocktest=MockTest1.objects.get(student=student)
            mocktest.delete()
            return redirect('college_details_acr',college.acronym)
        student_form=AddStudent()
        mocktest_form=MockTest()
        return render(request, template_name="studentform.html", context={'form1': student_form,'form2':mocktest_form,
                                                    'title': 'Add Student | MentorApp','user_permissions':request.user.get_all_permissions(),})
    def post(self,request,**kwargs):
        if resolve(request.path_info).url_name == 'edit_student':
            college=College.objects.get(id=kwargs.get('pk1'))
            student=Student.objects.filter(college=college).get(id=kwargs.get('pk2'))
            mocktest=MockTest1.objects.get(student=student)
            student_form=AddStudent(request.POST,instance=student)
            mocktest_form=MockTest(request.POST,instance=mocktest)
            if student_form.is_valid():
                student = student_form.save(commit=False)
                student.college = college
                student.save()
                if mocktest_form.is_valid():
                    mocktest = mocktest_form.save(commit=False)
                    mocktest.total = int(request.POST['problem1']) + int(request.POST['problem2']) + int(request.POST['problem3'])\
                                     + int(request.POST['problem4'])
                    mocktest.student = student
                    mocktest.save()
            return redirect('college_details_acr',college.acronym)

        college = College.objects.get(**kwargs)
        student_form = AddStudent(request.POST)
        mocktest_form = MockTest(request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college=college
            student.save()
            if mocktest_form.is_valid():
                mocktest=mocktest_form.save(commit=False)
                mocktest.total=int(request.POST['problem1'])+int(request.POST['problem2'])+int(request.POST['problem3'])\
                               +int(request.POST['problem4'])
                mocktest.student = student
                mocktest.save()
        return redirect('college_details_acr',college.acronym)

def logout_user(request):
    logout(request)
    return redirect('login')

class LoginController(View):
    def get(self,request,**kwargs):
        if request.user.is_authenticated:
            return redirect('colleges_html')
        form=LoginForm()
        return render(request,
                      template_name="login.html",
                      context={'form':form,'user_permissions':request.user.get_all_permissions(),})
    def post(self,request,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect('colleges_html')
            else:
                messages.error(request,'Wrong Credentials')
                return render(request,
                              template_name='login.html',
                              context={'form':form,
                                       'user_permissions':request.user.get_all_permissions()})

class SignUpController(View):
    def get(self,request,**kwargs):
        form=SignUpForm()
        return render(request,
                      template_name="signup.html",
                      context={'form': form,'user_permissions':request.user.get_all_permissions()})
    def post(self,request,**kwargs):
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect('colleges_html')
        return redirect('signup')