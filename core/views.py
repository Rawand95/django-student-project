from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm


# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit= False)
            instance.user = request.user
            instance.save()
            return redirect('home')

    else:
        form = StudentForm()


        students = Student.objects.filter(user=request.user)

    context = {
    'form': form,
    'students': students
    }
    return render(request, 'core/index.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('home')


def update_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = StudentForm(instance=student)

    return render(request, 'core/update.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')



