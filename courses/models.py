from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    longdescription=models.TextField(default='Learning course')
    instructor = models.CharField(max_length=100,default='AI')
    price = models.DecimalField(max_digits=6, decimal_places=2,default=15)
    students = models.ManyToManyField(User, through='Enrollment', related_name='enrolled_courses')
    def __str__(self):
        return self.title

class Material(models.Model):
    course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    # Add fields for other types of materials as needed

class Question(models.Model):
    course = models.ForeignKey(Course, related_name='questions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
