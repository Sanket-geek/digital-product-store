from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'store/index.html')
    # return HttpResponse("Hello world")

def about(request):
    return HttpResponse("About page")

def contact_us(request):
    return HttpResponse("Contact us")

def test(request):
    return render(request, 'store/test.html')

