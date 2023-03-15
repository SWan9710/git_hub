from django.shortcuts import render

# Create your views here.
def index(request):
    
    info = {
        'name' : 'swan',
        'age' : 21,
    }

    return render(request, 'myapp/home.html', {'info':info})