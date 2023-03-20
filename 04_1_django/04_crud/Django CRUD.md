프로젝트 만들다 실수해서 지워야 할 때

rm -rf crud/

치면된다

# Django CRUD

1. 가상환경설치
   
   - python -m venv venv

2. 가상환경실행
   
   - source venv/Scripts/activate

3. 장고설치
   
   - pip install django==3.2.18

4. ipython설치
   
   - pip install ipython

5. requirments.txt 생성
   
   - freeze > requirments.txt

6. 프로젝트 시작
   
   - django-admin startproject 프로젝트명 .

7. 앱 시작
   
   - python manage.py startapp 앱이름

8. settings 등록
   
   - installed_apps 에 앱이름 등록

9. url 설정
   
   1. 분기해서 url 설정 할거니까 프로젝트의 urls에 분기해줄 url 등록하기
   
   2. path('앱이름/', include('앱이름.urls')) 로 보내기
   
   3. `from django.urls import path, include 작성`
   
   4. 분기해줄 위치인 앱 폴더에 urls.py 생성
   
   5. path 설정해주기
      
      1. 앱이름 뒤에 어떤 방식으로 접근 되었을때 어떻게 반환해줄건지 설정해주기
      
      2. from django.urls import path
      
      3. from . import views
      
      4. app_name = 앱이름
      
      5. urlpatterns = [ (6번작성) ]
      
      6. path('index/', views.index, name='index') 작성

10. base.html 위치 설정
    
    1. 프로젝트 폴더 위치에 공용으로 사용될 부분 만들어 줄거
    
    2. templates 폴더 생성
    
    3. 폴더 안에 base.html 생성
    
    4. settings.py의 TEMPLATES의 DIRS 설정해주기
    
    5. `BASE_DIR / 'templates'`

11. view 설정
    
    1. urls를 통해 들어온 요청을 어떻게 처리할 것인지 설정
    
    2. index(request):
    
    3. return render(request, '앱이름/index.html')
    
    위의 형식이 기본형

12. html 파일 만들기
    
    1. 앱 내에 templates 만든 후 샌드위치 폴더 형태로 templates 안에 앱이름 동일한 폴더 하나 더 만들기
    
    2. 그 폴더 내에 html 파일 만들기
    
    3. base.html 을 통해 공통 부분을 상속받으므로 제일 위에 {% extends 'base.html' %} 작성
    
    4. 상속받는 부분 {% block %} 으로 묶은 부분에 들어갈 내용 작성

대부분 기본 내용을 토대로 응용하는 거임

기본적으로 페이지를 보여주기 까지 완료했다면 사용자가 페이지를 만들게끔 해주어야 함

아직은 구현을 못하기에 admin으로 해줄거

python manage.py createsuperuser

===> 관리자 만든다는거(여러개 만들 수 있음)

admin 

===> 사용될 관리자 아이디

admin@admin.kr

===> 관리자의 이메일 주소 여기서는 예시를 만들기 위해 위처럼 지정

pass1234

===> 관리자 비밀번호

작성할때 커서가 움직이지 않는데 원래 그런거임

admin.py 에 들어가서 내가 만든 앱 등록 해줄거임

from .models import 앱이름

이러면 models.py에도 내가 만든 앱이 등록되어 있어야 함

models.py에 class 앱이름(models.Model): (앱이름 시작은 대문자)

여기에 가져올 것들 등록 해주기

title = models.CharField(max_length=40)

content = models.TextField()

생성시간

created_at = models.DateTimeField(auto_now_add=True)

수정시간

updated_at = models.DateTimeField(auto_now=True)

어드민에 사이트를 등록할거임 내가만든 앱을

==> 그대로 영어로 번역해서 치면 됨

admin.site.register(앱이름)

실행된 서버에 admin 을 입력하여 관리자 페이지로 이동후 로그인 하기

등등등 해줄게 많다 집에서 천천히 하나씩 따라하면서 적어보자
