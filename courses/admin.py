from django.contrib import admin
from .models import Course, Material

admin.site.register(Course)
admin.site.register(Material) # register for admin control to upload courses and materials

