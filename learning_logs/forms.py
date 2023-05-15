from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		field = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attr={'cols': 80})}