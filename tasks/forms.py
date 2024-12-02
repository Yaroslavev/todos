from django import forms
from tasks.models import Todo

class CreateTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

