- # django

- Framework 이해하기
  
  - 누군가 만들어 놓은 코드를 재사용 하는 것은 이미 익숙한 개발 문화이다.
  
  - 그러한 코드들을 모아 놓은 것, 즉 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것 => 프레임워크

- 장점
  
  - 개발속도가 빨라짐
  
  - 이미 검증된 코드
  
  - 반복작업의 수 감소
  
  - 협업에 용이하다

- 단점
  
  - 선택의 폭이 좁다
  
  - 러닝커브(사용하기 위해 배워야 한다) 가 존재한다.

## 클라이언트와 서버

> 클라이언트 - 서버 구조

- 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작

- 클라이언트와 서버 역시 하나의 컴퓨터이며 이들이 어떻게 상호작용하는지에 대한 간소화된 다이어그램

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2023-03-14-09-16-48-image.png" title="" alt="" width="464">

- 클라이언트
  
  - 웹 사용자의 인터넷에 연결된 장치(예를 들어 wi-fi에 연결된 컴퓨터 또는 모바일)
  
  - chrome 또는 firefox 같은 웹 브라우저
  
  - 서비스를 요청하는 주체

- 서버
  
  - 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
  
  - 요청에 대해 서비스를 응답하는 주체
  
  상호작용 예시
  
  > 우리가 google 홈페이지에 접속할 때
  
  1. 결론적으로 인터넷에 연결된 전세계 어딘가에 있는 구글 컴퓨터에게 google 홈페이지.html 파일을 달라고 요청하는 것
  
  2. 구글 컴퓨터는 우리의 요청을 받고 google홈페이지.html파일을 인터넷을 통해서 우리 컴퓨터에 응답해줌
  
  3. 그렇게 전달받은 google홈페이지.html 파일을 웹 브라우저가 우리가 볼 수 있도록 해석해 주는것

## Django 사용하기

1. 내가 프로젝트를 실행하고자 하는 곳에서 프로젝트 폴더 만들기

2. 파이썬 가상환경 생성 하기
   
   - python -m venv venv

3. 가상환경 활성화 하기
   
   - source venv/Scripts/activate
     
     - 가상환경 끄기
     
     - deactivate

4. 프로젝트 폴더에서 가상환경을 실행했다면 장고 설치하기
   
   - pit install djang==3.2.18

5. 프로젝트 생성
   
   - django-admin startproject (<mark>firstpjt</mark>) >> 노란색은 프로젝트 이름(자유롭게 설정)

6. 서버 실행
   
   - python manage.py runserver >> vscode에서 실행해보자

## Django Application

- 애플리케이션 생성
  
  - python manage.py startapp articles
  
  - 일반적으로 애플리케이션 이름은 복수형으로 작성

- 앱을 사용하기 위해서는 반드시 settings.py > INSTALLED_APPS 에 `'articles',` 라고 작성해 줘야함 애플리케이션 이름을 articles로 작성했기 때문에 articles라고 추가

<mark>항상 애플리케이션 먼저 생성해주고 그 뒤에 INSTALLED_APPS에 추가해줘야함</mark>

## 실행해보기

1. URLs 설정
   
   - ```python
     from articles import views
     
     path('articles/', views.index),
     ```

2. View

```python
from django.http import HttpResponse



def index(request):

  return render(requese, 'articles/index.html')
```
