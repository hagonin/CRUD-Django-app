from django.contrib import admin

from .models import Grade, Student, Subject, Score

admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Score)
