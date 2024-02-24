from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterationForm
from django.contrib import messages
#home view
def home_view(request):
    return render(request, "loghome/home.html")


def aboutus_view(request):
    return render(request, "loghome/about.html")

def register_view(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created {username}")
            return redirect("home")
    else:
        form = UserRegisterationForm()
    return render(request, "loghome/register.html", {'form':form})

