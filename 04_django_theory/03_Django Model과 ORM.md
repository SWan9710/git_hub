# Django Model과 ORM

## Form & Data

- 데이터를 보내고 서버에서 데이터를 가져오는 거

- HTML form 을 통해 사용자와 애플리케이션 간의 상호작용

- <mark>가장 기본적으로 클라이언트 - 서버 아키텍처를 사용</mark>
  
  - 클라이언트가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답

- 클라이언트 측에서 MTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법

- 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있음

> ## HTML <form> element

- 데이터가 전송되는 방법을 정의

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당

- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지

> ## HTML form`s attributes

1. action
   
   - <mark>입력 데이터가 전송될 URL을 지정</mark>
   
   - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함
   
   - <mark>만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐</mark>

2. method
   
   - <mark>데이터를 어떻게 보낼 것인지 정의</mark>
   
   - 입력 데이터의 HTTP request method를 지정
   
   - HTML form 데이터는 오직 2가지 방법으로만 전송할 수 있는데 <mark>GET 방식과 POST 방식</mark>

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-09-12-56-image.png)

> ## HTML <input> element

- 사용자로부터 데이터를 입력 받기 위해 사용

- "type" 속성에 따라 동작 방식이 달라진다.
  
  - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별로도 MDN 문서에서 참고하여 사용하도록 함
  
  - type을 지정하지 않은 경우, 기본값은 "text"

- 핵심속성
  
  - name
    
    - form을 통해 데이터를 제출 했을 때 name 속석에 설정된 값을 서버로 전송하고, 서버는 name속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음 
    
    - 서버에 전달하는 파라미터(name은 key, value 는 value)로 매핑하는 것

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-09-26-18-image.png)

> ## HTTP request methonds

- HTTP
  
  - HTML 문서와 같은 리소스(데이터, 자원) 들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
  
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  
  - HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의

- 자원에 대한 행위(수행하고자 하는 동작)를 정의

- 주어진 리소스(자원) 에 수행하길 원하는 행동을 나타냄

- HTTP Methon 예시
  
  - GET, POST, PUT, DELETE (묶어서 CRUD 라고도 부른다. 보통 form 에서는 get, post 를 주로 씀)

> ## GET

- 서버로부터 정보를 조회하는데 사용
  
  - 서버에게 리소스를 요청하기 위해 사용

- 데이터를 가져올 때만 사용

- 데이터를 서버로 전송할 때 Query String Prrameters를 통해 전송
  
  - 데이터는 URL에 포함되어 서버로 보내짐

- 소문자 대문자 상관없는데 명시적 표현을 위해 대문자 권장

> ## Query String Parameters

- 사용자가 입력 데이터를 전달하는 방법 중 하나

- url 주소에 데이터를 파라미터를 통해 넘기는 것

- 이러한 문자열은 &(앰퍼샌드)로 연결된 key=value 쌍으로 구성

- 기본 URL과 물음표(?)로 구분됨

- Query String 이라고도 함

- 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림

- key=value로 필요한 파라미터의 값을 적음

- view 함수안 request 객체에 파라미터값이 담겨옴



> ## Retrieving the data(Server)

- 데이터 가져오기(검색하기)

- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 된다.

- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름

- Django는 trhow가 보낸 데이터를 catch로 가져옴

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-09-40-20-image.png)

> ## action 작성

- throw 페이지에서 form의 action 부분을 마저 작성하고 데이터를 보낸다.

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-09-45-50-image.png)

> ## 데이터 가져오기

- catch 페이지가 잘 응답되어 출력됨을 확인

- 그런데 throw 페이지의 form이 보낸 데이터는 어디에 들어 있을까
  
  - catck 페이지의 url 확인하기
  
  - GET method로 보내고 있기 때문에 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송

- 모든 요청 데이터는 view 함수의 첫번째 인자 request 에 들어있다.
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-09-47-59-image.png)

> ## Request and Response objects

- 요청과 응답 객체 흐름
1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성

2. 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달

3. 마지막으로 view 함수는 HttpResponse object를 반환

> ## Database

- 체계화된 데이터의 모임

- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

> ## DB 기본구조

1. 스키마(Schema)

2. 테이블(Table)

> ## 스키마(Schema)

- 뼈대

- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

> ## 테이블(Table)

- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합

- 관례 라고도 부름
1. 필드(세로)
   
   - 속성, 컬럼

2. 레코드(가로)
   
   - 튜플, 행

> ## PK(Primary key)

- 기본키

- 각 레코드의 고유한 값 > 식별자로 사용

- 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값

- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨

> ## 쿼리(Query)

- 데이터를 조회하기 위한 명령어

- 조건에 맞는 데이터를 추출하거나 조작하는 명령어

# Model

- Django는 Model을 통해 데이터에 접근하고 조작

- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함

- 저장된 데이터베이스의 구조

- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑

> ## Model 작성하기

- 새 프로젝트, 앱 작성 및 앱 등록

- model.py 작성
  
  - 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의 하는것
  
  - 모델 클래스 == 테이블 스키마

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-10-11-42-image.png)

- 작성시 CharField는 반드시 max_length가 필요 글자수에 제한이 있음

- 물론 제한을 1000~ 100000 등으로 해도 되는데 데이터가 낭비되므로 비효율적이다.

- TextField 는 문자의 길이 제한 X  

> ## 데이터베이스 스키마

- 지금까지 작성한 models.py는 데잍베이스 스키마를 정의한 것

- 이제 이러한 모델의 변경사항을 실제 데이터베이스에 반영하기 위한 과정이 필요

# Migrations

Django가 모델에 생긴 변화(필드 추가, 수정)을 실제 DB에 반영하는 방법 --> Migrations

> ## Migrations 관련 주요 명령어

1. makemigrations
   
   - 지금 내 모델 상태를 데이터베이스에 반영할 수 있는 하나의 migrations 상태로 만들어 주는것

2. migrate
   
   - 내가만든 migrations 상태의 파일을 실제 데이터베이스에 반영할때 사용하는 명령어
- 사용해보기
  
  - `python manage.py makemigrations`
    
    - 명령어를 실행하였을 때 이때까지의 변화를 0001_initial.py 로 만들어줌
  
  - `python manage.py migrate`
    
    - 모델의 변경사항을 데이터베이스와 동기화

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-10-23-40-image.png)

**이제 이런 형식으로 동작되는 거**

> ## 반드시 기억해야 할 migrations 3단계

1. models.py 변경사항 발생

2. migration 생성
   
   - makemigrations

3. DB반영
   
   - migrate
- models.py 의 변경사항을 migrations 으로 변경하고 반영해도 파이썬으로 작성되어 있는데 DB는 sql 언어만 알아 듣기에 중간에 번역을 담당하는것이 <mark>ORM</mark>

# ORM

- Object-Relational_Mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

- SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어 주는 매개체

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-10-28-01-image.png)

- 단점 -- ORM 만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 있음

# QuerySet API

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-10-34-08-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-10-36-52-image.png)

> ## Database API

- Django가 제공하는 ORM을 사용해 데이터베이스를 조작하는 방법

- Model을 정의하면 데이터를 만들고 읽고 수정하고 지울 수 있는 API를 제공

> ## Database API 구문

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-03-16-10-41-42-image.png)

Queryset API 가 가장 자주 바뀔것

> ## objects manager

- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스

- Django는 기본적으로 모든 Django 모델 클래스에 대해 ojects 라는 Manager 객체를 자동으로 추가함

- 이 Manager를 통해 특정 데이터를 조작 가능

- DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager

> ## Query

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
  
  - 쿼리문을 작성
    
    - -> 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.

- 파이썬으로 코드 작성 => ORM => SQL 변환 => DB전달

- 데이터베이스의 응답 데이터를 ORM이 QuerySet 이라는 자료 형태로 변환되어 우리에게 전달

> ## QuerySet

- 데이터베이스에게서 전달 받은 객체 목록
  
  - 순회가 가능한 데이터, 1개 이상의 데이터를 불러와 사용 가능

- Django ORM을 통해 만들어진 자료형, 필터를 걸거나 정렬등을 수행 가능

- object manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체

- DB가 단일 객체를 반환 할 때는 QuerySet이 아닌 모델Class의 인스턴스로 반환

> ## 데이터 객체를 만드는 3가지 방법

>  첫번째 방법

1. article = Articles()
   
   - 클래스를 통한 인스턴스 생성

2. article.title
   
   - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

3. article.save()
   
   - 인스턴스로 save 메서드 호출

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2023-03-16-10-52-33-image.png" title="" alt="" width="439">
