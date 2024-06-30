from django.contrib import admin
from finstudent.models import Student, SubjectMarks
from finstudent.views import studentdetails

# Register your models here.

class studentadmin(admin.ModelAdmin):
  list_display = ('id','name', 'age', 'email', 'city')

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'language_1', 'language_2', 'acting', 'dance')


admin.site.register(Student, studentadmin)
admin.site.register(SubjectMarks, SubjectMarksAdmin)


