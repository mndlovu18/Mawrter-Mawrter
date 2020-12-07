
from django.shortcuts import render, redirect

# Create your views here.
def Home(request):
	if request.POST:
		email = request.POST.get('email', None)
		print(email)
	return render(request, 'index.html', {})	
	
	
	
		