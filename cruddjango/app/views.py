from django.shortcuts import render, redirect
from .models import Student
from .forms import studentInfo

def student(request):
    if request.method == 'POST':
        form = studentInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
           
    else:
        form = studentInfo()
    return render(request,'app/home.html', {'form':form})

def show(request):
    students = Student.objects.all()
    return render(request, "app/show.html", {'students':students})


def edit (request,id):
    student = Student.objects.get(student_id=id)
    return render(request, 'app/edit.html',{'student':student})   

def update(request,id):
    object = Student.objects.get(student_id=id)
    form = studentInfo(request.POST, instance = object)
    if form.is_valid():
        form.save()
        return redirect("show")
    return render (request, 'app/edit.html', {'student':student})

def clear(request,id):
    student = Student.objects.get(student_id=id)
    student.delete()
    return redirect("show")
