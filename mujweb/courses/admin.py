from django.contrib import admin

from .models import Course, Teacher 
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Course)

