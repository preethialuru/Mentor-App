from django.shortcuts import render
from django.http import HttpResponse
from .models import College
from .models import Student
# Create your views here.

def hello_world(request):
    print(request.headers)
    return HttpResponse("hello world")

def html(request):
    html = "<html><body>This is HTML</body></html>"
    return HttpResponse(html)

def getCollegeName(request):
    college = College.objects.values('name')
    #html = "<html><body><table border=1>"
    #for i in college:
    #    html+="<tr><td>"+i['name']+"</td></tr>"
    #html+="</table></body></html>"
    return HttpResponse(render(request,'home.html'))


def get_details(request,num):
    college=College.objects.get(id=num)
    students=Student.objects.filter(college=college)
    return render(request,'colleges.html',{'students':students})

def css(request):
    return render(request,'main.html')
def addData(request):
    return render(request,'form.html')

def formSubmit(request):
    print("form success")
    college_name = request.POST['college_name']
    acronym = request.POST['acronym']
    location = request.POST['location']
    contact = request.POST['contact']
    college = College(name=college_name,acronym=acronym,location=location,contact=contact)
    college.save()
    return render(request, 'form.html')