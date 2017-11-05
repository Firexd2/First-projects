from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .forms import *
import sys

def blog_home(request):
    posts = Post.objects.all()[::-1]
    return render(request, 'blog.html', locals())

def post(request, name_url):
    post = get_object_or_404(Post, name_url=name_url)
    ip_client = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR')).split(',')[-1].strip()
    if not InformationsClient.objects.filter(ip=ip_client, name_url=name_url):
        post.look += 1
        InformationsClient(ip=ip_client, name_url=name_url).save()
        post.save()
    return render(request, 'post.html', locals())

@login_required
def new_post(request):
    new_post_form = NewPost(request.POST or None)
    if request.POST:
        new_post_form = NewPost(request.POST, request.FILES)
        if new_post_form.is_valid():
            new_post_form.save()
            try:
                last_post = Post.objects.latest()
                no_resize = str(last_post.logo).split('.')
                last_post.image_resize = no_resize[0] + '-2.' + no_resize[1]
                last_post.save(update_fields=['image_resize'])
            except: pass
            return redirect('blog_home')
    return render(request, 'new_post.html', locals())

@login_required
def delete_post(request, name_url):
    post = Post.objects.get(name_url=name_url)
    if post.logo:
        os.remove(post.logo.path)
        os.remove(post.logo.path[:-len(post.image_resize)+2] + post.image_resize)
    post.delete()
    return redirect('blog_home')

@login_required
def edit_post(request, name_url):
    post = get_object_or_404(Post, name_url=name_url)
    if request.POST:
        new_post_form = NewPost(request.POST, request.FILES, instance=post)
        if new_post_form.is_valid():
            new_post_form.save()
            try:
                no_resize = str(post.logo).split('.')
                post.image_resize = no_resize[0] + '-2.' + no_resize[1]
                post.save(update_fields=['image_resize'])
            except: pass
            return redirect('post', name_url=post.name_url)
    new_post_form = NewPost(instance=post)
    return render(request, 'edit_post.html', locals())


def filter_to_category(request, category):
    posts = Post.objects.filter(category=category)[::-1]
    return render(request, 'blog.html', locals())


@login_required
def image(request):
    try: images = Image.objects.filter(date=datetime.datetime.now().date())[::-1]
    except: images = None

    new_image_form = NewImage(request.POST or None)
    if request.POST:
        new_image_form = NewImage(request.POST, request.FILES)
        if new_image_form.is_valid():
            new_image_form.save()
            return redirect('image')

    return render(request, 'image.html', locals())
