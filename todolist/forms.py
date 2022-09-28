from django import forms

class TodoList(forms.Form):
    title = forms.CharField(label = 'Judul Task', max_length = 250)
    description = forms.CharField(label = 'Deskripsi Task', max_length = 250)