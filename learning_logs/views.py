from django.shortcuts import render

def index(request):
	"""Strona główna dla aplikacji Learning Log."""
	return render(request, 'templates/learning_logs/index.html')