from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import StudentForm


def index(request):
    students = Student.objects.all()
    return render(request, 'Home/index.html', {'students': students})


def view_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_full_name = form.cleaned_data['fullName']
            new_birthday = form.cleaned_data['birthday']
            new_phone = form.cleaned_data['phone']
            new_email = form.cleaned_data['email']
            new_address = form.cleaned_data['address']

            new_student = Student(
                fullName=new_full_name,
                birthday=new_birthday,
                phone=new_phone,
                email=new_email,
                address=new_address
            )
            new_student.save()
            return render(request, 'Home/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'Home/add.html', {
        'form': StudentForm()
    })


def edit(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'Home/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=student_id)
        form = StudentForm(instance=student)
    return render(request, 'Home/edit.html', {
        'form': form
    })


def delete(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))


def score(request, student_id):
    students = Student.objects.get(pk=student_id)
    subjects = Subject.objects.all()
    grades = Grade.objects.all()
    scores = Score.objects.all()

    context = {'scores': scores}
