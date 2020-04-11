from django.shortcuts import render
from .forms import CreateComplainForm
from django.shortcuts import HttpResponse
from django.views.generic import CreateView, ListView
from .models import Complain
# Create your views here.

#function views
def create_complain(request):
  new_complain = CreateComplainForm
  if request.method == 'POST':
    new_complain = CreateComplainForm(request.POST)
    if new_complain.is_valid():
      new_complain.save()
      return HttpResponse("Complain Registered")
    return HttpResponse("Incorrect Format")

  return render(request, 'complain\create-complain.html', {'form': CreateComplainForm})
#No need of forms.py if we use class
class CreateComplainView(CreateView):
  model = Complain
  template_name = 'complain\create-complain.html'
  fields = '__all__'


class ListComplainView(ListView):
  model = Complain
  template_name = 'complain\list-complain.html'
