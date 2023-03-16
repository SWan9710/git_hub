from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    print(title, content)
    
    # ORM
    # class.manager.queryAPI
    #
    
    return render(request, 'articles/create.html')