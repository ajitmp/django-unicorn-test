# todo.py

from django_unicorn.components import UnicornView
from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(min_length=2, max_length=20, required=True)

class TodoView(UnicornView):
    task = ""
    tasks = []

    def add(self):
        if self.is_valid():
            self.tasks.append(self.task)
            self.task = ""