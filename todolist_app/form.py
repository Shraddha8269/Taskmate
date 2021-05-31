from django import forms
from todolist_app.models import Tasklist
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task','done']

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
	
	class Meta:
		model = User
		fields =['first_name','last_name','email_address','message']