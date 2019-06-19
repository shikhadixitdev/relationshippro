from django.contrib import admin
from .models import Student, Courses, Employee, Products


class AdminStudent(admin.ModelAdmin):
    list_display = ['sname', 'sloc', 'email']


class AdminCourses(admin.ModelAdmin):
    list_display = ['cname', 'cfee']


class AdminEmployee(admin.ModelAdmin):
    list_display = ['empname', 'emploc', 'email']


class AdminProducts(admin.ModelAdmin):
    list_display = ['pname', 'pcost'

                    ]


admin.site.register(Student, AdminStudent)
admin.site.register(Courses, AdminCourses)
admin.site.register(Employee, AdminEmployee)
admin.site.register(Products, AdminProducts)

# Register your models here.
