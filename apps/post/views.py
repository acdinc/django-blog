from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def post_dashboard(request):

    authenticate_control(request)

    post_list = Post.objects.all()
    query = request.GET.get('q')

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 20)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    template = 'post/dashboard.html'
    context = {
        'posts': posts,
        'nav_dashboard': 'active',
    }

    return render(request, template, context)


def post_index(request):

    post_list = Post.objects.all()
    query = request.GET.get('q')

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    template = 'post/index.html'
    context = {
        'posts': posts,
        'nav_index': 'active',
    }

    return render(request, template, context)


@login_required(login_url='accounts:login')
def post_create(request):

    authenticate_control(request)

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Makale oluşturuldu!')
        return HttpResponseRedirect(post.get_absolute_url())

    template = 'post/form.html'
    context = {
        'form': form,
        'nav_index': 'active',
    }

    return render(request, template, context)


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, 'Yorumunuz eklendi!')
        return HttpResponseRedirect(post.get_absolute_url())

    template = 'post/detail.html'
    context = {
        'post': post,
        'form': form,
        'nav_index': 'active',
    }

    return render(request, template, context)


@login_required(login_url='accounts:login')
def post_update(request, slug):

    authenticate_control(request)

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        messages.success(request, 'Makale güncellendi!')
        return HttpResponseRedirect(post.get_absolute_url())

    template = 'post/form.html'
    context = {
        'form': form,
        'nav_index': 'active',
    }

    return render(request, template, context)


@login_required(login_url='accounts:login')
def post_delete(request, slug):

    authenticate_control(request)

    post = get_object_or_404(Post, slug=slug)
    post.delete()

    return redirect('post:dashboard')


def authenticate_control(request):

    if not request.user.is_authenticated:
        return Http404()
