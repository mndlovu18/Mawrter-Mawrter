
from django.shortcuts import render, redirect

# Create your views here.
def Home(request):
	if request.POST:
		email = request.POST.get('email', None)
		return redirect('Login')
		print(email)
	return render(request, 'index.html', {})	

def Login(request):
	return render(request, 'success_login.html ')

def Mentor(request):
	return render(request, 'mentor1.html')

def Mentor_continued(request):
	return render(request, 'mentor2.html')

def Mentee(request):
	return render(request, 'mentee1.html')

def Mentee_continued(request):
	return render(request, 'mentee2.html')

def Thank_you(request):
	return render(request, 'thank_you.html')

def About(request):
	return render(request, 'about.html')
	
	
		