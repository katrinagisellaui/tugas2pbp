from django import forms
from .models import Task

class TodoList(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Input Judul Task', 'class':'form-control mx-3 my-2'}),
            'description': forms.Textarea(attrs={'placeholder':'Input Judul Task', 'class':'form-control mx-3 my-2'})
        }