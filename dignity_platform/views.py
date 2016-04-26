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

def jobs(request):
    some_jobs = Job.objects.order_by('?')[:5]
    template = loader.get_template('dignity_platform/jobs.html')
    context = {
        'some_jobs': some_jobs,
    }
    return HttpResponse(template.render(context, request))

def job(request, job_id):
    job = Job.objects.filter(id=job_id).first()
    template = loader.get_template('dignity_platform/job.html')
    context = {
        'job': job,
    }
    return HttpResponse(template.render(context, request))



def causes(request):
    some_causes = Cause.objects.order_by('?')[:5]
    template = loader.get_template('dignity_platform/causes.html')
    context = {
        'some_causes': some_causes,
    }
    return HttpResponse(template.render(context, request))

def cause(request, cause_id):
    cause = Cause.objects.filter(id=cause_id).first()
    template = loader.get_template('dignity_platform/cause.html')
    context = {
        'cause': cause,
    }
    return HttpResponse(template.render(context, request))
