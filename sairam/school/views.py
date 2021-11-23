from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import programs
from django.template import loader

def courses(request):
    ac =[1,2,3,44,5,6,7,8,9,10]
    template=loader.get_template("school/template/school/programs.html")
    context={
        "ac": ac,
    }
    return HttpResponse(template.render(context, request))

def details(request,course_id):
    return HttpResponse('<h2>those are the course details</h2>')
    """ects.get(pk =course_id)

    except programs.DoesNotExist:
           raise Http404("course dosenot exist")

    return render(request,"/school/details.html",{'course': course})''''''try:
        course=programs.obj"""

# Create your views here.
