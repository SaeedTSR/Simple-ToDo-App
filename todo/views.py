from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from accounts.models import CustomUser


class TodoList(LoginRequiredMixin, ListView):
    context_object_name = 'tasks'

    def get_queryset(self):
        task = Task.objects.filter(user=self.request.user)
        return task

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(email=self.request.user)
        email = str(user.email)
        x = email.find('@')
        data['username'] = email[:x]
        return data

class TodoCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'status', 'due_date']
    success_url = reverse_lazy('todo:list')
    template_name = 'todo/task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoEdit(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'status', 'due_date']
    success_url = reverse_lazy('todo:list')


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('todo:list')
