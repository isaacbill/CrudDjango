from django.shortcuts import render, redirect

from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Records

from django.contrib import messages
#home page
def home(request):

    return render(request,'crudapp/index.html')

#register  a user

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':

        form =CreateUserForm(request.POST)
        
        if form.is_valid():

            form.save()
            messages.success(request,'Account created successfully!')
            return redirect('login')
        
    context ={ 'form':form}
    return render (request, 'crudapp/register.html', context= context)


#login user

def login(request):
    form = LoginForm()
    if request.method == 'POST':

        form= LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')
    context ={'form' :form}
    return render(request, 'crudapp/login.html', context = context)


@login_required(login_url='login')
def dashboard(request):
    my_records = Records.objects.all()
    context = {'records': my_records}
    return render(request, 'crudapp/dashboard.html', context=context)

#Create a record
@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()
    if request.method =='POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'record was created successfully!')
            return redirect('dashboard')
    
    context = {'form' : form}
    return render(request, 'crudapp/create-record.html', context= context)

#update a record

@login_required(login_url='login')
def update_record(request,pk):

    record = Records.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)
    if request.method =='POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            messages.success(request,'Record updated successfully!')

            return redirect('dashboard')
    
    context = {'form' : form}
    return render(request, 'crudapp/update-record.html', context= context)

#read or view singular record

@login_required(login_url='login')
def singular_record(request,pk):
    
    all_records = Records.objects.get(id=pk)

    context = {'record' :all_records}

    return render (request, 'crudapp/view-record.html', context=context)

#delete a record
@login_required(login_url='login')
def delete_record(request,pk):

    record = Records.objects.get(id=pk)

    record.delete()
    messages.success(request,'Record deleted successfully!')
    return redirect('dashboard')

#user logout
def user_logout(request):
    
    auth.logout(request)
    messages.success(request,'Logout success!')
    return redirect('login')

