from django.db import models

class College(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    acronym = models.CharField(max_length=8)
    contact = models.EmailField()

    def __str__(self):
        return self.acronym

class Student(models.Model):
    name = models.CharField(max_length=128)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    db_folder = models.CharField(max_length=50)
    dropped_out = models.BooleanField(default=False)

    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MockTest1(models.Model):
    problem1 = models.IntegerField(default=0)
    problem2 = models.IntegerField(default=0)
    problem3 = models.IntegerField(default=0)
    problem4 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.total

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    college = models.ForeignKey(College, on_delete=models.CASCADE)





