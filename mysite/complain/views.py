from django.shortcuts import render
from .forms import CreateComplainForm
from django.shortcuts import HttpResponse

# Create your views here.

# function views
def create_complain(request):
    new_complain = CreateComplainForm
    if request.method == 'POST':
        new_complain = CreateComplainForm(request.POST)
        if new_complain.is_valid():
            new_complain.save()
            return HttpResponse("Complain registered")
        else:
            return HttpResponse("Incorrect Format")

    return render(request, 'complain/create-complain.html', {'form': CreateComplainForm})
