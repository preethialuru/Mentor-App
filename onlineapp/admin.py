from django.contrib import admin
from .models import College
from .models import Student
from .models import MockTest1
from .models import Teacher

# Register your models here.
admin.site.register(College)
admin.site.register(Student)
admin.site.register(MockTest1)
admin.site.register(Teacher)