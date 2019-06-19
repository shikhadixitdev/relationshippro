from django.db import models


class Student(models.Model):
    sname = models.CharField(max_length=100)
    sloc = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.sname


class Courses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.ForeignKey, null=-1)
    cname = models.CharField(max_length=100)
    cfee = models.IntegerField()

    def __str__(self):
        return self.cname


class Employee(models.Model):
    empname = models.CharField(max_length=100)
    emploc = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.empname


class Products(models.Model):
    employee = models.ManyToManyField(Employee)
    pname = models.CharField(max_length=100)
    pcost = models.IntegerField()

    def __str__(self):
        return self.pname


# Create your models here.
