from django import forms
from.models import Todo



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_id','keyword', 'title', 'main_text', 'update_date']
        exclude = ['todo_id', 'update_date']
