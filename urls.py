from django.contrib import admin
from django.urls import path

urlpattern = [
	url('admin/', admin.site.urls),
	url('', include('learning_logs.urls')),
]