from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.
def index(request):

	context = {'courses': Course.objects.all()}
	return render(request, 'courses_app/index.html', context)

def add(request):
	name = request.POST['name']
	d = request.POST['description']

	errors = Course.objects.validate_form(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/')
	else: 
		description = Description.objects.create(description=d)
		Course.objects.create(name=name, description=description)

	return redirect('/')

def show(request, id):

	try:
		c = Comment.objects.filter(course=id)
	except ObjectDoesNotExist:
		c = None


	context = {'course': Course.objects.get(id=id), 'comments': c}
	return render(request, 'courses_app/show.html', context)

def add_comment(request, id):
	name = request.POST['name']
	comment = request.POST['comment']

	errors = Comment.objects.validate_comment_form(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error)
		return redirect('/courses/{}'.format(id))
	else:
		Comment.objects.create(name=name, comment=comment, course=Course.objects.get(id=id))
		return redirect('/courses/{}'.format(id))
	

def confirm_delete(request, id):
	context = {'course': Course.objects.get(id=id)}
	return render(request, 'courses_app/confirm.html', context)

def destroy(request, id):
	c = Course.objects.get(id=id)
	c.delete()

	try:
		c = Comment.objects.filter(course=id)
		c.delete()
	except ObjectDoesNotExist:
		pass

	return redirect('/')
