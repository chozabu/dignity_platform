from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Person, Cause, Job, JobWorker, CauseSupporter

from django.contrib.auth.forms import UserCreationForm
import django
from . import forms


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
    if request.method == 'POST':
        uf = forms.ServiceForm(request.POST)
        if uf.is_valid():
            service = uf.save(commit=False)
            service.person = request.user
            service.save()
            return django.http.HttpResponseRedirect("/people/"+str(request.user.id))
        else:
            print("invalid", uf.errors)
        uf = forms.SupportingForm(request.POST)
        if uf.is_valid():
            service = uf.save(commit=False)
            service.person = request.user
            service.save()
            u = request.user
            CauseSupporter.objects.balance_user_support(u, u.self_support)
            return django.http.HttpResponseRedirect("/people/"+str(request.user.id))
        else:
            print("invalid", uf.errors)
    person = Person.objects.filter(id=person_id).first()
    template = loader.get_template('dignity_platform/person.html')
    context = {
        'person': person,
        'supporting_amount': 100-person.self_support*100
    }
    if request.user.is_authenticated():
        context['services_form'] = forms.ServiceForm
        context['supporting_form'] = forms.SupportingForm
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


def register(request):
    if request.method == 'POST':
        uf = forms.UserForm(request.POST, prefix='user')
        if uf.is_valid():
            user = uf.save()
            return django.http.HttpResponseRedirect("/")
    else:
        uf = forms.UserForm(prefix='user')
    return django.shortcuts.render_to_response('register.html',
                                               dict(userform=uf),
                                               context_instance=django.template.RequestContext(request))


def remove_service(request, person_id = None, service_id= None):
    if request.method == 'POST':
        if request.user.is_authenticated():
            print(service_id)
            service = JobWorker.objects.filter(person=request.user, id=service_id)
            service.delete()
    return django.http.HttpResponseRedirect("/people/" + str(request.user.id))


def remove_support(request, person_id = None, support_id= None):
    if request.method == 'POST':
        if request.user.is_authenticated():
            print(support_id)
            service = CauseSupporter.objects.filter(person=request.user, id=support_id)
            service.delete()
            u = request.user
            CauseSupporter.objects.balance_user_support(u, u.self_support)
    return django.http.HttpResponseRedirect("/people/" + str(request.user.id))
