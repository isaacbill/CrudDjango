from django.shortcuts import render, redirect

from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdtaeRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Records
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

#Create a recorcd
@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()
    if request.method =='POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
    
    context = {'form' : form}
    return render(request, 'crudapp/create-record.html', context= context)





#user logout
def user_logout(request):
    
    auth.logout(request)
    return redirect('login')

