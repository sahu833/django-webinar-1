from django.shortcuts import render
from .models import Complain
from .forms import ComplainForm
from django.shortcuts import HttpResponse
from django.views.generic import ListView, CreateView


# Create your views here.


# Functional Views
def create_complaint(request):
    if request.method == 'GET':
        return render(request, "complaints/complaint-form.html", {'create_form': ComplainForm})
    if request.method == 'POST':
        entry = ComplainForm(request.POST)
        print(request.POST)
        print(entry)
        if entry.is_valid():
            entry.save()
            return HttpResponse("Complain Created")
        else:
            return HttpResponse("Incorrect entry!")


def list_complaint(request):
    complains = Complain.objects.all()
    return render(request, "complaints/complaint-list.html", {'complains': complains})


# Class Based Views
# class ComplainCreate(view)
class ComplainList(ListView):
    model = Complain
    template_name = 'complaints/complaint-list.html'


class CreateComplainView(CreateView):
    model = Complain
    template_name = 'complaints/complaint-form.html'
    fields = '__all__'


