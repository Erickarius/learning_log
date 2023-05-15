from django.shortcuts import render

from .models import Topic
from .forms import TopicForm

def index(request):
	"""Strona główna dla aplikacji Learning Log."""
	return render(request, 'learning_logs/index.html')

def topics(request):
	"""Wyświetlanie wszystkich tematów."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	"""Wyświetla pojedynczy temat i wszystkie powiązane z nim wpisy."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
	"""Dodaj nowy temat."""
	if request.method != 'POST':
		#Nie przekazano żadnych danych, należy utworzyć pusty formularz.
		form = TopicForm()
	else:
		#Przekazano dane za pomocą żądnia POST, należy je przetworzyć
		form = TopicForm()
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topics')

	#Wyświetlenie pustego formularza.
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)