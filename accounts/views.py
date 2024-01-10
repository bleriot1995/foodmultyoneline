from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import auth, messages

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # creeate the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # creeate the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Your account has been registered successfully!")
            return redirect('registerUser')
        else:
            print("Invalide form")
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/registerUser.html', context)