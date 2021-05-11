from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, CreateUserForm
from django.contrib import messages
from .models import Engineer, Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .filters import TaskFilter
from django.db.models import Sum 


def index(request):
    user_list = Engineer.objects.all()
    
    context = {

        'user_list': user_list


    }
    return render(request, 'index.html', context)


def search_engineer(request):
    if request.method == "POST":
        searched = request.POST['searched']
        engineers = Engineer.objects.filter(name__contains=searched)

        context = {
            'searched': searched,
            'engineers': engineers,
        }

        return render(request, 'search.html', context)
    
    else:
        return render(request, 'search.html', {})


def register(request):
    submitted = False
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin_register?submitted=True')
    else:
        form = CreateUserForm
        if 'submitted' in request.GET:
            submitted = True
    
    context = {

        'form': form,
        'submitted': submitted
    }

    return render(request, 'register.html', context)


def detail(request, user_id):
    user = get_object_or_404(Engineer, pk=user_id)
    current_user = request.user.username
    eng = Engineer.objects.get(pk=user_id)
    attendance_p = eng.task_set.aggregate(Sum('attendance_point'))
    result_p = eng.task_set.aggregate(Sum('result_point'))
    context = {

        'current_user': current_user,
        'user': user,
        'att_p': attendance_p,
        'result_p': result_p

    }

    return render(request, 'detail.html', context)


@login_required(login_url='login')
def add_cr(request):
    submitted = False

    # print(current_user)
    if request.method == "POST":
        form = TaskForm(request.POST, request=request)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_cr?submitted=True')


    else:
        form = TaskForm(request=request)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_cr.html', {'form':form, 'submitted': submitted})


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('add-cr')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)
        
			if user is not None:
				login(request, user)
				return redirect('add-cr')
			else:
		            messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)



def logoutUser(request):
	logout(request)
	return redirect('home')


def updateTask(request, pk, task_id):
    eng = Engineer.objects.get(pk=pk)
    task = eng.task_set.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task, request=request)
    if form.is_valid():
        form.save()
        return redirect('detail', pk)
    context = {

        'form': form,
        'task': task

    }
    return render(request, 'update.html', context)

def deleteTask(request, pk, task_id):
    eng = Engineer.objects.get(pk=pk)
    task = eng.task_set.get(id=task_id)
    # task.delete()
    if request.method == "POST":
        task.delete()
        return redirect("detail", pk)


    context = {

        'item': task

    }

    return render(request, 'delete.html', context)