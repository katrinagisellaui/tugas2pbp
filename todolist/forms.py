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

    # title = forms.CharField(label='Judul Task:', widget=forms.TextInput(attrs={'placeholder': 'Judul Task Baru', 'class':'form-control mx-3 my-2'}))
    # description = forms.CharField(label="Deskripsi Task:", widget=forms.Textarea(attrs={'placeholder': 'Deskripsi Task Baru', 'class':'form-control mx-3 my-2'}))
    