from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from django.http import HttpResponse

def home(request):
    return render (request, "polls/home.html")

def about(request):
    return render(request , "polls/about.html")

def contact(request):
    return render(request, 'polls/contact.html')

def register(request):
    if request.method =='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Welcome account created sucessfully")
            return redirect('login')
        else:
            messages.error(request, 'sorry there was an error in registration.')
    else:
        form = UserCreationForm()
    return render(request, 'polls/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Login the user
            return redirect('home')  # Redirect to a page after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Stay on login page in case of failure
    else:
        form = AuthenticationForm()  # Use the AuthenticationForm for login
        return render(request, 'polls/login.html', {'form': form})

