from urllib import request
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from LoginApp.forms import SignupForm, UserProfileChangeForm, ProPicForm




# Create your views here.

def sign_up(request):
    Registerd = False
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            Registerd = True
    
    dic={'form': form, 'Registerd': Registerd}
    return render(request,'LoginApp/register.html', context=dic)


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request,'LoginApp/login.html', context={'form':form})

@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def UserProfile(request):
    return render(request,'LoginApp/user_profile.html')

@login_required
def ChangeUserProfile(request):
    current_user = request.user
    form = UserProfileChangeForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loginapp:profile'))
    return render(request,'LoginApp/change_profile.html', context={'form':form})



@login_required
def ChangePasss(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, request.POST,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loginapp:profile'))
    return render(request,'LoginApp/change_pass.html', context={'form':form})

    

@login_required
def AddProPic(request):
    form = ProPicForm()
    if request.method == 'POST':
        form = ProPicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj  = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('loginapp:profile'))
    return render(request,'LoginApp/AddProPic.html', context={'form':form})


def ProPicChange(request):
    form = ProPicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProPicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loginapp:profile'))
    return render(request,'LoginApp/AddProPic.html', context={'form':form})
        

               
    
            
            
    
            



    


        
                


                

       
    




