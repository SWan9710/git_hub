from django.shortcuts import render

# Create your views here.
# view 함수는 한가지 특이한 점이 있다.
# 첫번째 인자는 반드시 request를 받도록 되어있다.
def index(request):
    # app_name/templates/app_name/
    # articles/templates/articles/index.html
    # pages/templates/pages/index.html
    context = {
        'num' : 30
        }
    return render(request, 'articles/index.html', context)