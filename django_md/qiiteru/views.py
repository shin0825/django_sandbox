# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post, Tag

# Create your views here.
def index(request):
   posts = Post.objects.all().order_by('-created_at')
   return render(request, 'qiiteru/index.html', {'posts': posts})
