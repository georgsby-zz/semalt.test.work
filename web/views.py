from django.http import Http404
from django.views.generic import TemplateView

from web.models import Task


class HomeView(TemplateView):
    template_name = 'web/index.html'
    model = Task

    def get_context_data(self, **kwargs):
        try:
            tasks = Task.objects.filter(is_active=True)
        except Task.DoesNotExist:
            raise Http404

        context = super().get_context_data(**kwargs)
        context['tasks'] = tasks
        return context


class TaskSolveView(TemplateView):
    template_name = 'web/task.html'
    model = Task

    def get_context_data(self, **kwargs):
        try:
            tasks = Task.objects.filter(is_active=True)
            task = Task.objects.get(pk=kwargs.get('pk'))
        except Task.DoesNotExist:
            raise Http404

        context = super().get_context_data(**kwargs)
        context['tasks'] = tasks
        context['task'] = task
        return context
