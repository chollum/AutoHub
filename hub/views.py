from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hub/index.html')

def doors(request):
    return render(request, 'hub/doors.html')

def lights(request):
    return render(request, 'hub/lights.html')

def data(request):
    return render(request, 'hub/data.html', {})

def test(request):
    return render(request, 'hub/test.html')

def chat(request):
    return render(request, 'hub/chat.html')
