from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def signup(request):
    form = forms.SignUPform()
    if request.method == "POST":
        form = forms.SignUPform(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponse("User Created Successfully...")
    return render(request, 'authApp/signup.html', {'form': form})