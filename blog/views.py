from django.shortcuts import render, get_object_or_404, redirect, reverse
# from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.utils.http import is_safe_url
from .forms import ParentCommentForm, ChildCommentForm
from .models import Blog, Comment, Reply
from category.models import Category
# Create your views here.


class BlogList(ListView):

    template_name = 'blog/blog.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(BlogList, self).get_context_data(*args, **kwargs)
        context['parent_tags'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Blog.objects.all()  # also can user this function .order_by('-timestrimp')


class BlogDetails(DetailView):

    template_name = 'blog/blog_detail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetails, self).get_context_data(**kwargs)
        context['parent_tags'] = Category.objects.all()
        context['blog_widget'] = Blog.objects.all()[:3]
        context['comments'] = Comment.objects.filter(blog=self.kwargs.get('pk'))
        context['form'] = ParentCommentForm()
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = get_object_or_404(Blog, pk=pk, active=True)
        return instance


class ParentCommentView(BlogDetails, CreateView):
    form_class = ParentCommentForm
    # template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ParentCommentView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print(self.kwargs)
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(ParentCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.kwargs['pk']}, )


def parent_comment(request, pk):
    if request.POST:
        blog = get_object_or_404(Blog, pk=pk)
        form = ParentCommentForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.blog = blog
            instance.save()
            return redirect('blog:blog_detail', pk=pk)
        else:
            print('form not valid')
            return redirect('blog:blog_detail', pk=pk)


def child_comment(request, blog_pk, parent_pk):
    parent = get_object_or_404(Comment, pk=parent_pk)
    form = ChildCommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.parent = parent
        instance.save()
        print("form Save successfully")
        return redirect('blog:blog_detail', pk=Blog.objects.get(pk=blog_pk))
    else:
        print('Form Not Valid')
        return redirect('blog:blog_detail', pk=Blog.objects.get(pk=blog_pk))
