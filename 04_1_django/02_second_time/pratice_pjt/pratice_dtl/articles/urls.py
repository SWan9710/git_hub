# articles/urls.py
from django.urls import path
from . import views

# 변수명 app_name은 꼭 지켜야 한다.
app_name = 'articles'

urlpatterns = [
    # URL mapping -> include
    # Naming URL patterns
    path('index/', views.index, name='index'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    path('<int:age>/', views.info, name='info'),
    path('<name>/profile/', views.profile, name='profile'),
    
    # 변수에 값을 저장하는 느낌인데 만약 index 가 main으로 변경되면
    # 모든 경로를 찾아가서 index로 저장된 것을 main으로 변경해줘야 함
    # 그걸 방지하기 위해 name='index'로 불러옴
]
