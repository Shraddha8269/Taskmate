from django import forms
from todolist_app.models import Tasklist,Contact
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task','done']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'