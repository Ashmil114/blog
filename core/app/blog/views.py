from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import tb_post
from app.authentication.models import tb_user
from django.http import Http404
from .forms import post_form, category_form
from django.contrib import messages


@login_required
def home(request):
    if request.user is not None:
        if request.user.is_superuser:
            return redirect("login")
        else:
            posts = tb_post.objects.all().order_by("-created")

    return render(request, "home.html", {"posts": posts})


@login_required
def post_detail(request, pk):

    try:
        post = get_object_or_404(tb_post, pk=pk)
    except Http404:
        return render(request, "404.html", status=404)

    return render(request, "post_detail.html", {"post": post})


@login_required
def about(request):

    return render(request, "about.html", {"form": post_form})


@login_required
def post(request):
    user = tb_user.objects.get(user=request.user)
    posts = user.get_posts()
    return render(request, "posts.html", {"posts": posts})


@login_required
def add_category(request):
    if request.method == "GET":
        cate_form = category_form(request.GET)
        if cate_form.is_valid():
            cate_form.save()
            messages.success(request, "Category created successfully")
            return redirect("add_post")
        else:
            messages.error(request, "Error creating category")
    else:
        cate_form = category_form()
    form = post_form()
    return render(request, "add_new_post.html", {"form": form, "cate_form": cate_form})


@login_required
def add_post(request):
    if request.method == "POST":
        form = post_form(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            user = user = tb_user.objects.get(user=request.user)
            post.owner = user
            post.save()
            messages.success(request, "Post created successfully")
            return redirect("home")
    else:
        form = post_form()
    # cate_form = category_form()
    return render(
        request, "add_new_post.html", {"form": form, "cate_form": category_form()}
    )


@login_required
def edit_post(request, pk):
    post = get_object_or_404(tb_post, id=pk)

    if request.method == "POST":
        form = post_form(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully")
            return redirect("home")
    else:
        form = post_form(instance=post)

    return render(request, "edit_post.html", {"form": form})


@login_required
def delete_post(request, pk):

    post = tb_post.objects.get(id=pk)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("home")
