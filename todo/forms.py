from django import forms
from .models import Todo

class ToDoForm(forms.ModelForm):
    title = forms.CharField(label="タイトル", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "タイトル"}))
    description = forms.CharField(label="詳細", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "詳細"}), 
                                  required=False)
    due_date = forms.DateField(label="期限", widget=forms.DateInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD", "type": "date"}), 
                               required=False)
    class Meta:
        model = Todo
        fields = [
            "title", "description", "due_date"
        ]