from django.shortcuts import render, redirect
from app1.models import Students
from app1.forms import StudentForm
# Create your views here.

def home(request):
    return render(request, 'title.html')

def student_list(request):
    data=Students.objects.all()
    context={'data':data}
    return render(request, 'home.html', context)

def student_form(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm()
        context={'form':form}
    return render(request, 'student_form.html', context)        

def update_Student(request,name):
    student=Students.objects.get(first_name=name)
    form=StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm(instance=student)
        context={'form':form}
    return render(request, 'student_form.html', context)

def delete_Student(request,name):
    student=Students.objects.get(first_name=name)
    student.delete()
    return redirect('student_list')