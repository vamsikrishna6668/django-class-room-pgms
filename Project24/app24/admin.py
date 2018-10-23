from django.contrib import admin

from .models import Course
from .models import Faculty
from .models import NewClass

admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(NewClass)
