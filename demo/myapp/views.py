from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator


# Create your views here.


def home(request):
	return render(request, 'index.html', {})