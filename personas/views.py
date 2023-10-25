from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate,login
from .form import CustomUserCreationForm

# Create your views here.

def home(request):
    return render(request,'personas/home.html')

@login_required
def listado(request):
    return render(request,'personas/listado.html')

def register(request):
    data ={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        User_Creation_Form = CustomUserCreationForm(data=request.POST)

        if User_Creation_Form.is_valid():
            User_Creation_Form.save()

            user = authenticate(username=User_Creation_Form.cleaned_data['username'], password=CustomUserCreationForm.cleaned_data['passwordd1'])
            login(request, user)
            return redirect('home')
    
    return render(request,'registration/register.html', data)