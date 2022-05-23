import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

from django.contrib.auth import login
from django.contrib import messages

from .forms import PostForm
from .forms import EditForm

from django.urls import reverse
from django.template import loader


# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:20]
    categories_list = Category.objects.all()[:5]
    context = {
        'post_list': post_list,
        'categories_list': categories_list,
    }
    return render(request, 'blog/index.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("blog:index")
        messages.error(request, "Unsuccessful registration.")
    form = NewUserForm()
    return render(request=request, template_name="blog/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("blog:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="blog/login.html", context={"login_form": form})


def create_post(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('blog:index')

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = user
        obj.author = author
        obj.pub_date = datetime.datetime.now()

        obj.save()
        form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "blog/create_post.html", context)


def edit_post(request, post_id=None):
    user = request.user
    if id:
        post = get_object_or_404(Post, pk=post_id)
        if post.author != request.user:
            return HttpResponseForbidden()
    else:
        post = Post(author=request.user)
    form = EditForm(request.POST or None, request.FILES or None, instance=post)
    if request.POST and form.is_valid():
        obj = form.save(commit=False)
        author = user
        obj.author = author
        obj.pub_date = datetime.datetime.now()
        obj.save()
        redirect_url = reverse("blog:index")
        return redirect(redirect_url)
    context = {
        "form": form,
    }
    return render(request, "blog/edit_post.html", context)


def delete_post(request, post_id=None):
    user = request.user
    if id:
        post = get_object_or_404(Post, pk=post_id)
        if post.author != request.user:
            return HttpResponseForbidden()
        else:
            post = get_object_or_404(Post, id=post_id)

            if request.POST:
                obj = post.delete()

                redirect_url = reverse("blog:index")
                return redirect(redirect_url)
        context = {
            "object": post,
        }
        return render(request, "blog/delete_post.html", context)
