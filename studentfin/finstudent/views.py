from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from finstudent.models import Student, SubjectMarks 


# Create your views here.
def welcome(request):
  return HttpResponse('<h1>Welcome</h1>')

def studentdetails(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'finstudent/welcome.html', {'student': student})