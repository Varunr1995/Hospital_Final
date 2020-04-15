from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.forms import modelformset_factory
from django.http import JsonResponse, HttpResponseRedirect

from .models import main_content, appointmentmodel
from .forms import appointment

# Create your views here.


def homepage(request):
    return render(request, "mainpage.html")


def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def elements(request):
    return render(request, "elements.html")


def news(request):
    return render(request, "news.html")


# ----------- APPOINTMENT REQUEST FORM (FORMS)-------------------- #

"""
def appointmentform(request):
    if request.method == "POST":
        form = appointment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            print(form.cleaned_data.get("name"))
            print(form.cleaned_data.get("gender"))
            print(form.cleaned_data.get("age"))
            print(form.cleaned_data.get("phone_number"))
            print(form.cleaned_data.get("country"))
            print(form.cleaned_data.get("department"))
            print(form.cleaned_data.get("reports"))

    form = appointment
    return render(request, "appointment.html", {"form": form})

"""
def appointmentform(request):
    if request.method == "POST":
        form = appointment(request.POST)
        if form.is_valid():
            obj = appointmentmodel()
            obj.name = form.cleaned_data['name']
            obj.gender = form.cleaned_data['gender']
            obj.age = form.cleaned_data['age']
            obj.phone_number = form.cleaned_data['phone_number']
            obj.email_id = form.cleaned_data['email_id']
            obj.country = form.cleaned_data['country']
            obj.department = form.cleaned_data['department']
            obj.reports = form.cleaned_data['reports']
            obj.save()
            return JsonResponse(obj)
        return HttpResponseRedirect('')

    form = appointment
    return render(request, "appointment.html", {"form": form})


# ----------- UPDATE THAT CAN BE DONE DYNAMICALLY -------------------- #
def maindescription(request):
    descs = main_content.objects.all()
    return render(request, "mainpage.html", {"descs": descs})
