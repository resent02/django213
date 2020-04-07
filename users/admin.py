from django.contrib import admin
from .models import Course,  Student, User, Comment
# Register your models here.

admin.site.register(Course)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Comment)


