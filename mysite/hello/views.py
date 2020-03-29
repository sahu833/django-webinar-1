from django.shortcuts import render


# Create your views here.

def hello_world(request):
    return render(request, template_name="hello/hello.html")
