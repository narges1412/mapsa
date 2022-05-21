
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_, logout as logout_
from django.urls import reverse_lazy
from app.forms import AddCategoryForm,AddTodoForm,LoginForm,ProfileForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
# Create your views here.
def login_or_register(request):
    return render(request , "index.html",{}) 

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "register.html", context)

def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "login-register.html", context)



class UserEditView(generic.UpdateView):
    form_class=ProfileForm
    template_name="profile.html"
    success_url= reverse_lazy('home')
    def get_object(self):
        return self.request.user
    



class AddCategory(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = AddCategoryForm()
        context = {'form':form}
        return render(request,'todo.html', context)
    
    def post(self, request, *args, **kwargs):
           
        form = AddCategoryForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('profile')


class AddToDo(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = AddTodoForm()
        context = {'form':form}
        return render(request,'todo-add.html', context)
    
    def post(self, request, *args, **kwargs):
        print("this1")
        form = AddTodoForm(request.POST)
        print("this2")
        form.instance.user = request.user
        print("this3")
        if form.is_valid():
            print("this4")
            form.save()
            return redirect('profile')
        
#ANATHER AHOW ALL
class ShowAllView(ListView):
    template_name='alltodo.html'
    model = Todo
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def update_todo(request,pk):
    todo_obj=get_object_or_404(Todo,id=pk)
    form=AddTodoForm(instance=todo_obj)
    if request.method =='POST':
        form=AddTodoForm(request.POST, instance=todo_obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={"form":form} 
    return render(request, 'update.html',context)
    



























# @login_required(login_url='login')
# def profile(request):
#     if request.method == "GET":
#         user=get_object_or_404(Profile,username=request.user.username)
#         print
#         img=user.img
#         username=user.username
#         first_name=user.first_name
#         last_name=user.last_name
#         age=user.age
#         form=ProfileForm()
#         # print(user)
        
#         context = {
#         "img": img, 
#         "username": username,
#         "first_name": first_name,
#         "form":form
#         }
#     return render(request, "profile.html", context)

