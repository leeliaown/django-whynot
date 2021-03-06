from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, CreateUserForm, CreateEngineerForm
from django.contrib import messages
from .models import Engineer, Task
from .filters import TaskFilter
from django.db.models import Sum 
import datetime


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
        

@login_required(login_url='login')
def engineer_register(request):
    submitted = False
    form = CreateEngineerForm()

    if request.method == "POST":
        form = CreateEngineerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/engineer_register?submitted=True')
    else:
        form = CreateEngineerForm
        if 'submitted' in request.GET:
            submitted = True
    
    context = {

        'form': form,
        'submitted': submitted
    }

    return render(request, 'engineer_register.html', context)

@login_required(login_url='login')
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
    # eng_count = eng.objects.count()
    caption_text = ""

    if request.GET.get('s1') == '13':
        # print('user clicked summary')
        year = datetime.date.today().year
        query_set = user.task_set.filter(cr_date__range=[f"{year}-01-01", f"{year}-03-31"])
        myFilter = TaskFilter(request.GET, queryset=query_set)
        task_date = myFilter.qs
        caption_text = "1-3?????????"

    elif request.GET.get('s2') == '46':
        year = datetime.date.today().year
        query_set = user.task_set.filter(cr_date__range=[f"{year}-04-01", f"{year}-06-30"])
        myFilter = TaskFilter(request.GET, queryset=query_set)
        task_date = myFilter.qs
        caption_text = "4-6?????????"
    
    elif request.GET.get('s3') == '79':
        year = datetime.date.today().year
        query_set = user.task_set.filter(cr_date__range=[f"{year}-07-01", f"{year}-09-30"])
        myFilter = TaskFilter(request.GET, queryset=query_set)
        task_date = myFilter.qs
        caption_text = "7-9?????????"

    elif request.GET.get('s4') == '1012':
        year = datetime.date.today().year
        query_set = user.task_set.filter(cr_date__range=[f"{year}-10-01", f"{year}-12-31"])
        myFilter = TaskFilter(request.GET, queryset=query_set)
        task_date = myFilter.qs
        caption_text = "10-12?????????"


    else:
    #create a filter
        task_date = user.task_set.all()
        myFilter = TaskFilter(request.GET, queryset=task_date)
        task_date = myFilter.qs


    #add counting 
    attendance_p = task_date.aggregate(Sum('attendance_point'))
    result_p = task_date.aggregate(Sum('result_point'))
    rollback_p = task_date.aggregate(Sum('rollback_point'))

    total_p = 0


    for k1, v1 in attendance_p.items():
        for k2, v2 in result_p.items():
            for k3, v3 in rollback_p.items():
                if attendance_p[k1] and result_p[k2] and rollback_p[k3] is not None:
                    total_p = attendance_p[k1]+result_p[k2]+rollback_p[k3]

                else:
                    attendance_p[k1] = 0
                    result_p[k2] = 0
                    rollback_p[k3] = 0


    # total_p = attendance_p+result_p+rollback_p
    context = {

        'current_user': current_user,
        'user': user,
        'att_p': attendance_p,
        'result_p': result_p,
        'myFilter': myFilter,
        'task_date': task_date,
        'caption_text':caption_text,
        'rollback_p': rollback_p,
        'total_p': total_p,
       

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
				return redirect('home')
			else:
		            messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)



def logoutUser(request):
	logout(request)
	return redirect('home')


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteTask(request, pk, task_id):
    eng = Engineer.objects.get(pk=pk)
    task = eng.task_set.get(id=task_id)
    # task.delete()
    if request.method == "POST":
        task.delete()
        return redirect("detail", pk)


    context = {

        'item': task,
        'eng': eng,
    }

    return render(request, 'delete.html', context)