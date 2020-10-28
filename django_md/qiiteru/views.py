# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostAddForm

# Create your views here.
def index(request):
   posts = Post.objects.all().order_by('-created_at')
   return render(request, 'qiiteru/index.html', {'posts': posts})

def detail(request, post_id):
   post = get_object_or_404(Post, id=post_id)
   return render(request, 'qiiteru/detail.html', {'post': post})

def add(request):
   if request.method == "POST":
      form = PostAddForm(request.POST, request.FILES)
      if form.is_valid():
         post = form.save(commit=False)
         post.user = request.user
         post.save()
         return redirect('qiiteru:index')
   else:
      form = PostAddForm()
   return render(request, 'qiiteru/add.html', {'form': form})
