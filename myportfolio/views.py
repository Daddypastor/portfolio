from django.shortcuts import render
from .models import Project, Contact

def home(request):
	projects = Project.objects.all()
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)			

	return render(request, 'index.html', {'projects':projects})

