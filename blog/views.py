from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, TemplateView, DeleteView
from blog.forms import BlogForm
from blog.models import Blog
from mail_app.models import *
from mail_app.forms import *


# Create your views here
# .blog_list.html

# def get_queryset(self):
#     # Women.objects.all()[:5] ///////////////////////////////////////////////////////////////////////////////////////////////
#
#     # Такжепорядок(напротивоположный) можно менять с помощью метода reverse():
#     # Women.objects.all().reverse()


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'post_list'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # queryset = queryset.filter(is_published=True)
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     """КЭШирование для вывода версий"""
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['versions'] = get_cashed_versions_for_product(self.object.pk)
    #     return context_data

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['bloga3'] = Blog.objects.all()[:3]
        context_data['blog_last_3_date'] = Blog.objects.filter(sign_of_publication=True).order_by('-date_of_create')[:3]

        return context_data
