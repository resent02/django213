from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, db_index=True)
    price = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})

    def get_like_url(self):
        return reverse('course_like', kwargs={'pk': self.pk})

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.user

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', null=True, blank=True)
    body = models.TextField()
    

    def __str__(self):
        return f"Comments by {self.author} of {self.course}"