from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Blogs, Category,UserProfile
from .forms import BlogsForm, RegisterForm, LoginForm
from django.db.models import Q 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import  login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    search_post = request.GET.get('search')
    if search_post:
        list = Blogs.objects.filter(Q(name__icontains=search_post) & Q(content__icontains=search_post))
    else:
    # If not searched, return default posts
        list = Blogs.objects.all().order_by("-created")       
    return render(request, "index.html", {'dataset': list})

        #list = Blogs.objects.all()
        #return render(request, "index.html", {'dataset': list})

def userprofile(request):
    pro = UserProfile.objects.all()
    return render(request, 'profile.html', {'prof': pro})
    
def dashboard(request):
    return render(request, 'dashboard.html')
@login_required
def add(request):
    if request.method == 'GET':
        form = BlogsForm()
        return render(request, 'addblog.html', {'form':form})
    else:
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            saveblog = form.save()
            messages.success(request, 'ສຳເລັດ')
            return redirect('addblog')

def detail_view(request, id):
    context = Blogs.objects.get(id = id)
    return render(request, "detail_view.html", {'data':context})

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'ທ່ານສະໝັກສະມາຊິກ.')
            login(request, user)
            return redirect('registerpage')
        else:
            return render(request, 'register.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,'ທ່ານ ໄດ້ອອກຈາກລະບົບແລ້ວ.')
    return redirect('/')        

def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'ຍິນດີຕ້ອນຮັບ: {username.title()}')
                return redirect('/')
        
        # either form not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})

def edit_post(request, id):
    form = get_object_or_404(Blogs, id=id)
    if request.method == 'GET':
        form = {'form': BlogsForm(instance=form), 'id': id}
        return render(request,'edit.html',form)
    
    elif request.method == 'POST':
        form = BlogsForm(request.POST, request.FILES, instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'ອັບເດດສພເລັດ')
            return redirect('/')
        else:
            messages.error(request, 'ກະລູນາກວດ')
            return render(request,'edit.html',{'form':form})