from django.shortcuts import render, redirect

from . import models

# Create your views here.

def index(request):

	courselist = models.Courses.objects.all()
	print courselist

	context = {'course' : courselist}



	return render(request, 'courses_app/index.html', context)


def process(request):
	print "process"
	print request.POST.get('course_name')

	if len(request.POST.get('course_name'))>1:

		print "class submitted"
		course = models.Courses.objects.create(course_name=request.POST.get('course_name'), description = request.POST.get('description'))
	else:
		print "course is empty"

	return redirect('/')


def destroy(request, id):

	print "DESTROY THIS"
	thisclass = models.Courses.objects.get(id = id)

	context={'course' : thisclass}
	print thisclass.course_name
	print "if you didnt see that the query failed"

	return render(request, 'courses_app/destroy.html', context)

def deleting(request, id):
	print "okay deleting this"
	thisclass = models.Courses.objects.get(id = id).delete()
	print "its been done"

	return redirect('/')