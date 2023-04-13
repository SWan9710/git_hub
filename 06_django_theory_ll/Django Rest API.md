# Django Rest API

> 대표 HTTP Request Method

1. GET
   
   - 서버에 리소스의 표현을 요청
   
   - GET 사용하는 요청은 데이터만 검색

2. POST
   
   - 데이터를 지정된 리소스에 제출
   
   - 서버의 상태를 변경

3. PUT
   
   - 요청한 주소의 리소스를 수정
   
   - 전체수정 PUT
   
   - 일부수정 Patch

4. DELETE
   
   - 지정된 리소스를 삭제

> ## 웹에서 리소스 식별

- HTTP 요청의 대상을 리소스 라고 한다

- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음

- 각 리소스는 식별을 위해 URI로 식별됨

> URI

- Uniform Resource Identifier(통합 지원 식별자)

- 인터넷에서 리소스를 식별하는 문자열

- 가장 일반적인 URI는 웹 주소로 알려진 URL

특정 이름공간에서 이름으로 리소스를 식별하는 URI는 URN

![](Django%20Rest%20API_assets/2023-04-13-09-15-34-image.png)

> ## URL 구조
> 
> - 크게 아래사진과 같은 구조를 가짐

![](Django%20Rest%20API_assets/2023-04-13-13-52-54-image.png)

Scheme  (or protocol)

- - 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜
  
  - 기본적으로 HTTPS / HTTP를 요구
  
  - 메일을 열기위한 mailto:
  
  - 파일을 전송하기 위한 ftp :
    
    - 등등 다른 프로토콜도 존재

![](Django%20Rest%20API_assets/2023-04-13-09-19-43-image.png)

- Authority
  
  - Scheme 다음은 문자패턴 :// 으로 구분된 Authority(권한)이 작성됨
  
  - domain과 port를 모두 포함하며 :(콜론) 으로 구분

![](Django%20Rest%20API_assets/2023-04-13-09-19-51-image.png)

- Domain Name
  
  - 요청 중인 웹 서버
  
  - 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능
  
  - 사람이 직접 IP 주소를 외우는건 어렵기 때문에 주로 Domain Name 사용

- Port
  
  - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문
  
  - 포트번호는 서버안의 프로그램들을 구분하는 번호
  
  - HTTP 프로토콜의 표준 포트는 다음과 같고 생략이 가능
    
    - HTTP - 80
    
    - HTTPS - 443

![](Django%20Rest%20API_assets/2023-04-13-09-24-47-image.png)

- Path
  
  - 웹 서버의 리소스 경로
  
  - 초기 실제 파일이 위치한 물리적 위치를 나타냈지만 오늘날은 추상화된 형태의 구조를 표현
  
  - ex) articles/create/ 가 실제 articles 폴더안의 create 폴더 안을 나타내는건 아님

![](Django%20Rest%20API_assets/2023-04-13-09-26-06-image.png)

파라미터와 앵커는 생략

> ### 정리

- URI 자원의 식별자

- <mark>자원의 위치</mark>로 자원을 식별 <mark>URL</mark>

- <mark>고유한 이름</mark>으로 자원을 식별 <mark>URN</mark>

# REST API

> ## API

- Application Programming Interface

- 애플리케이션과 프로그래밍으로 소통하는 방법
  
  - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성

- API를 제공하는 애플리케이션과 다른 소프트웨어는 간단한 약속을 알아야 사용 가능하다.

- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

> ## Web API

- 웹 서버 또는 웹 브라우저를 위한 API

- 여러 open API를 활용하여 웹을 개발하는 것이 대표적인 추세

- 대표적인 open API 서비스 목록
  
  - Youtube API
  
  - Naver Papago API
  
  - Kakao Map API

- API는 다양한 타입의 데이터를 응답
  
  - HTML, XML, JSON 등등

> ## REST

- Representational State Transfer

- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론

- **에이든이 말하는 REST**
  
  - HTTP 프로토콜을 이용하여 각각의 자원의 식별자와 HTTP 메서드를 사용, 제한된 인터페이스를 사용해서 클라이언트와 서버간의 상호작용하는 아키텍쳐를 REST라 한다.

- 자원과 행동을 따로 구분 하자는 아키텍쳐를 REST라 함

- RESTful 하다 -> REST를 따른다 라는 의미

> ## REST에서 자원을 정의하고 주소를 지정하는 방법

1. 자원의 식별
   
   - URI

2. []()자원의 행위
   
   - HTTP Method

3. 자원의 표현
   
   - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
   
   - JSON 으로 표현된 데이터를 제공
   
   <mark>URI 와 HTTP를 통해서 JSON으로 표현된 데이터만 제공한다</mark>

> ## JSON

- JavaScript의 표기법을 따른 단순 문자열

- 사람이 일고 쓰기 쉽고 기계가 파싱(해석 & 분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입

- 쉽게 변환 가능한 Key - Value 형태의 구조를 갖고 있다.

> ### REST 정리

- 자원을 정의하고 자원에 대한 주소를 지정하는 방법의 모음
1. 자원을 식별 - URI

2. 자원에 대한 행위 - HTTP Method

3. 자원을 표현 - JSON

위 순서를 지키지 않아도 REST 이긴 한데 대부분의 REST API는 위의 방식을 따른다.

> ## HTML 응답

- HTML 문서 한 장을 응답하는 서버

- 기존 작성방식과 동일

urls 작성

![](Django%20Rest%20API_assets/2023-04-13-11-49-29-image.png)

views 작성

![](Django%20Rest%20API_assets/2023-04-13-11-52-00-image.png)

html 작성

![](Django%20Rest%20API_assets/2023-04-13-12-01-50-image.png)

> ## JsonResponse() 사용한 JSON 응답

- 문서 한장(HTML)이 아닌 JSON 데이터 응답해보기

view 수정

장고 내장함수 JsonResponse 임폴트 받아와서 사용

![](Django%20Rest%20API_assets/2023-04-13-12-13-57-image.png)

![](Django%20Rest%20API_assets/2023-04-13-12-13-48-image.png)

1. Article의 모든 객체를 들고와서 articles에 저장

2. json 파일 이용할 거니 articles_json 에 사용할 필드 append 해주기

3. 리스트에 딕셔너리 형태로 추가해주니 Key 와 Value 맞추서 작성

4. return 시 JsonResponse 리턴하고 저장된 context 넘기는 것 처럼 articles_json 파일 넘기

5. JsonResponse로 파일을 넘길때 첫번째 인자값은 딕셔너리 값이어야 하는데 딕셔너리 이외의 값을 넘기려면 safe=False로 설정해야 한다.
   
   - articles_json를 리스트로 받아서 딕셔너리값을 리스트 안에 저장했으니 현재 articles_json은 리스트고 JsonResponse로 넘길때 딕셔너리 값이 아니므로 safe=False로 설정

> ### [참고]

![](Django%20Rest%20API_assets/2023-04-13-12-22-33-image.png)

> ## Django Serializer 을 사용하여 JSON 응답

- Django의 내장 HttpResponse()를 활용하여 JSON 응답하기

HttpResponse 임포트 받아오기

![](Django%20Rest%20API_assets/2023-04-13-12-24-17-image.png)

![](Django%20Rest%20API_assets/2023-04-13-14-30-54-image.png)

> ## Serialization
> 
> - 직렬화
> 
> - 나중에 다시 쉽게 사용할 수 있는 포맷(Json)으로 변환하는 과정



> ## Django REST framework(DRF)

- django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

- DRF의 serializer는 form및 modelform 클래스와 매우 유사하게 작동한다.
  
  1. pip install djangorestframework 다운받기
  
  2. INSTALLED_APPS에 rest_framework 추가하기
  
  3. serializers.py 파일 만들고 안에 class 추가해주기
     
     - class 추가위해 from rest_framework import serializers 받아오기
     
     - 현재 모델도 받아오기
     
     ![](Django%20Rest%20API_assets/2023-04-13-14-35-10-image.png)
     
     - class 정의 -> form 사용방식과 동일한데 modelform 대신 serializer 사용
     
     ![](Django%20Rest%20API_assets/2023-04-13-14-35-50-image.png)
  
  4. views 작성
     
     - [주의] DRF serializers 는 데코레이터가 필수적으로 들어가야한다.
     
     ![](Django%20Rest%20API_assets/2023-04-13-14-36-38-image.png)
