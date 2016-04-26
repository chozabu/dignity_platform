from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Person, Cause, Job, JobWorker


def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('dignity_platform/index.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def people(request):
    some_people = Person.objects.order_by('?')[:5]
    template = loader.get_template('dignity_platform/people.html')
    context = {
        'some_people': some_people,
    }
    return HttpResponse(template.render(context, request))

def person(request, person_id):
    person = Person.objects.filter(id=person_id).first()
    template = loader.get_template('dignity_platform/person.html')
    context = {
        'person': person,
    }
    return HttpResponse(template.render(context, request))
