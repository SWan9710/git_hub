# Django 구조 이해하기

> Design Patten

- 각기 다른 기능을 가진 다양한 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하고 이를 처리하는 해결책 사이에도 공통점이 있다는 것

- 이러한 유사점을 패턴

- <mark>클라이언트 - 서버 </mark>구조도 디자인 패턴 중 하나

- <mark>자주 사용되는 소프트웨어 구조</mark>를 소수의 뛰어난 엔지니어가 <mark>일반적인 구조화</mark>를 해둔 것

> ## 소프트웨어 디자인 패턴의 목적

- 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시

- 프로그래머가 어플리케이션이나 시스템을 디자인할 때 발생하는 공통된 문제들을 해결하는데 형식화 된 가장 좋은 관행

> ## 소프트웨어 디자인 패턴의 장점

- 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, <mark>커뮤니케이션의 효율성을 높이는 기법</mark>

> ## Django에서의 디자인 패턴

- Django에 적용된 디자인 패턴은 **MTV 패턴** 이다.

- MTV 패턴은 MVC 디자인 패턴을 기반으로 조금 변형된 패턴

> ## MVC 소프트웨어 디자인 패턴

- MVC => Model - View - Controller의 준말

- 데이터 및 논리 제어를 구현하는데 널리 사용되는 디자인 패턴

- 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
1. Model : 데이터와 관련된 로직을 관리

2. View : 레이아웃과 화면을 처리

3. Controller : 명령을 model과 view 부분으로 연결

> ## MVC 소프트웨어 디자인 패턴의 목적

- "관심사 분리"

- 더 나은 업무의 분리와 향상된 관리를 제공

- 각 부분을 독립적으로 개발 => 개발 효율성 및 유지보수가 쉬워짐

- ===> 다수의 멤버로 개발하기 용이하다.

> ## Django에서의 디자인 패턴

- 두 패턴은 서도 크게 다른 점은 없으며 일부 역할에 대해 부르는 이름이 다름

- Model
  
  - MVC 패턴에서 Model의 역할에 해당
  
  - 데이터와 관련된 로직을 관리
  
  - 응용프르그램의 데이터 구조를 정의, 데이터베이스의 기록을 관리

- Template
  
  - 레이아웃과 화면을 처리
  
  - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
  
  - MVC 패턴에서 View의 역할에 해당

- View
  
  - Model & Template과 관련한 로직을 처리해서 응답을 반환
  
  - 클라이언트의 요청에 대해 처리를 분기하는 역할
    
    - 데이터가 필요 ==> model 접근
    
    - 가져온 데이터를 template로 보내 화면을 구성
    
    - 구성된 화면을 클라이언트에게 응답으로 반환
  
  - MVC 패턴에서 Controller의 역할에 해당
  
  <img title="" src="Django 구조 이해하기_assets/ecd117f6e539e7f2e0790279dfdb234577455b8d.png" alt="" width="531">  

template 과 View는 일방향으로 연결되어 있는데 쌍방향으로도 연결 가능

> ## Django Template Language (DTL)

- Django template에서 사용하는 built-in template system
- 조건, 반복, 변수, 치환, 필터 등의 기능을 제공
  - python처럼 일부 프로그래밍 구조(if, for등)을(를) 사용할 수 있지만 이것은 python 코드로 실행되는것이 아님
  - Django 템플릿 시스템은 단순히 python HTML에 포함된 것이 아니니 주의
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것

> ## DTL Syntax

1. Variable ==> 변수
2. Filters ==> 변수가 어떻게 보여지는를 바꿔주는 것 변수를 조작하는건 아님
3. Tags ==> 조건, 반복 등등의 기능을 템플릿 태그로 처리
4. Comments ==> 주석

> ## Variable
> 
> `{{ variable }}`

- 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성되나 밑줄로 시작 X
  - 공백이나 구두점 문자 또한 사용 X
- dot(.)를 사용하여 변수 속성에 접근할 수 있음
- render()의 세번째 인자로 {'key' : value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 된다.

![](Django%20구조%20이해하기_assets/2023-03-15-09-53-19-image.png)

![](Django%20구조%20이해하기_assets/2023-03-15-09-53-34-image.png)

이런형태로 변수를 넘겨서 사용가능하다.

> ## Filters
> 
> `{{ variable|filter }}`

- 표시할 변수를 수정할 때 사용
  
  - ex) name 변수를 모두 소문자로 출력하기
  
  - {{ name|lower }}

- 60개의 built-in template filters를 제공

- chained가 가능하며 일부 필터는 인자를 받기도 한다. {{ name|truncatewords:30 }}

> ## Tags
> 
> `{% tag %}`

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수해

- 일부 태그는 시작과 종료 태그가 필요 `{% if %}{% endif %}`

- 약 24개의 built-in template tags를 제공

![](Django%20구조%20이해하기_assets/2023-03-15-10-11-34-image.png)

> ## Comments
> 
> `{# #}`

- 한줄 주석

- 여러 줄 주석은 `{%comment%} {%endcomment%}`사이에 입력

> ## 템플릿 상속

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

> ## 템플릿 상속에 관련된 태그
> 
> `{% extends '' %}`

- 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림

- <mark>반드시 템플릿 최상단에 작성 되어야 함(즉, 2개 이상 사</mark>용 불가)

`{% block content%} {% endblock cnotent %} `

- 하위 템플릿에서 재지정 할 수 있는 블록을 정의

- 즉, 하위 템플릿이 채울 수 있는 공간

- 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있음

> ## Trailing Slashes

- django의 URL끝에 /가 없다면 자동으로 붙여주는 것

- 기술적인 측면에서 foo.com/bar 와 foo.com/bar/ 는 서로 다른 URL 이다.

> ## Variable routing

- URL 주소를 변수로 사용하는 것을 의미

- 변수값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

- url의 path에 주소값으로 입력될 부분에 <>으로 정의함

- views 함수에 넘겨주는 값으로 따로 정의 해줘야 함

> ## App URL mapping

- 앱이 많아졌을때 urls.py를 각 app 별로 만들어서 분기 처리 하는것

- 서비스를 개발하다 보면 url과 view가 아주 많아 지게 되다보니 하나의 urls.py에서 관리하는 것은 가독성도 떨어지고 프로젝트의 유지 보수에도 좋지않다.

`사용법`

1. app 안에 urls.py 파일 만들기

2. `from django.urls import path` `from . import views`
   
   - from . == > 현재 폴더위 위치를 의미

3. `urlpatterns` 만들어주기

4. `path('index/', views.index)` 작성
