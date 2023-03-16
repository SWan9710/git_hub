"""pratice_dtl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # index 경로로 요청이 들어왔을때, articles.views.py 의 index 함수를 넘겨준다.
    # path('index/', views.index)
    
    #######
    # app이 여러개가 될때 같은 변수명을 사용하기 위해 as를 여런번 사용하는건 비효율적 따라서
    
    # articled app이 가지고 있는 요청 경로는 
    # articles/urls.py를 참고하여서 처리하여라
    # include('app_name.urls)
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls'))
    
]
