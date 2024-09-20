from django.shortcuts import render, redirect
from .models import Destination, Person, Tag
from .forms import PersonForm
from django.http import JsonResponse



def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})


def pers(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show_person')
    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form': form})


def show_person(request):
    people = Person.objects.all()
    return render(request, "show_person.html", {'People': people})

def edit_person(request, id):
    person = Person.objects.get(id=id)
    form = PersonForm(instance=person)
    return render(request, 'edit_person.html', {'form': form, 'person': person})


def update_person(request, id):
    person = Person.objects.get(id=id)
    form = PersonForm(request.POST, instance=person)
    if form.is_valid():
        form.save()
        return redirect("/show_person")
    return render(request, 'edit_person.html', {'form': form, 'person': person})

def delete_person(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/show_person")

def get_client_info(request):
    client_info = {
        'ip_address': request.META.get('REMOTE_ADDR'),
        'user_agent': request.META.get('HTTP_USER_AGENT'),
        'host': request.META.get('HTTP_HOST'),
        'referer': request.META.get('HTTP_REFERER'),
        'accept_language': request.META.get('HTTP_ACCEPT_LANGUAGE'),
        'request_method': request.META.get('REQUEST_METHOD'),
        'request_path': request.META.get('PATH_INFO'),
        'query_string': request.META.get('QUERY_STRING'),
        'protocol': request.META.get('wsgi.url_scheme'),
        'cookies': request.COOKIES,
        'session_id': request.session.session_key,
        'system_ip' : request.META.get('HTTP_X_FORWARDED_FOR')
    }
    return JsonResponse(client_info)
