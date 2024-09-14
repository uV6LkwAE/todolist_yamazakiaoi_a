from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
# Create your views here.
from .models import Post
from .forms import PostForm


class ListTodoView(LoginRequiredMixin, ListView):
    template_name = 'todo/todo_list.html'
    model = Post
    context_object_name = 'todos'  # テンプレート内で使用するオブジェクトの名前を指定

    def get_queryset(self):
        status = self.request.GET.get('status')

        if status == 'finished':
            todos = Post.objects.filter(user=self.request.user, status='finished').order_by('date')
        elif status == 'unfinished':
            todos = Post.objects.filter(user=self.request.user, status='unfinished').order_by('date')
        else:
            todos = Post.objects.filter(user=self.request.user).order_by('date')

        return todos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = self.request.GET.get('status', '')
        return context

# class SearchTodoView(ListView):
#     model = Post
#     template_name = 'todo/todo_search.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             return Post.objects.filter(
#                 Q(title__icontains=query) | Q(text__icontains=query)
#             )
#         return Post.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['query'] = self.request.GET.get('q', '')
#         return context

class SearchTodoView(ListView):
    model = Post
    template_name = 'todo/todo_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        # ログイン中のユーザーを取得
        user = self.request.user
        if query:
            # ログイン中のユーザーに関連する投稿のみフィルタ
            return Post.objects.filter(
                (Q(title__icontains=query) | Q(text__icontains=query)) & Q(user=user)
            )
        # ログイン中のユーザーの投稿のみ取得
        return Post.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class DetailTodoView(LoginRequiredMixin,DetailView):
    template_name = 'todo/todo_detail.html'
    model = Post

class CreateTodoView(LoginRequiredMixin,CreateView):
    template_name = 'todo/todo_create.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # ログイン中のユーザーを取得して保存する
        return super().form_valid(form)
    

class DeleteTodoView(LoginRequiredMixin, DeleteView):
    template_name = 'todo/todo_delete.html'
    model = Post
    success_url = reverse_lazy('todo-list')

class UpdateTodoView(LoginRequiredMixin,UpdateView):
    template_name = 'todo/todo_update.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('todo-list')