from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import  Tasklist
from .form import TaskForm, ContactForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else: 
        all_tasks = Tasklist.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})
@login_required
def delete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed."))

    return redirect('todolist')
@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))
        return redirect('todolist')
    else: 
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {})
@login_required
def complete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed."))

    return redirect('todolist')
@login_required
def pending_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=False
        task.save()
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed."))

    return redirect('todolist')

def index(request):
    context={
        "welcometext":"Welcome To Index!!",
    }
    return render(request,"Index.html",context)

def contacts(request):
    if(request.method == 'POST'):
        form = ContactForm(request.POST or None)
        if(form.is_valid()):
            subject = "Website Inquiry" 
            body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'email_address', ['shraddhajain3131@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            
            return redirect ("contact_us")
    all_form=ContactForm()
    return render(request, "contacts.html", {'all_form':all_form})

def about(request):
    context={
        "welcometext":"Welcome To About_Us!!",
    }
    return render(request,"about.html",context)
