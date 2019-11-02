from django.test import TestCase

# Create your tests here.
def fun():
    from onlineapp.models import College
    College.objects.all()

fun()