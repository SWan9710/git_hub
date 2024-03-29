# Vue Auth System

> Authentication - 인증, 입증

- 자신이라고 주장하는 사용자가 누구인지 확인하는 행위

- 모든 보안 프로스세의 첫번째 단계

- 401 Unauthorized
  
  - HTTP 표준에서는 미승인을 명확히 하고 있지만 의미상 이 응답은 비인증을 의미한다.

---

> Authorization - 권한 부여, 허가

- 사용자에게 특정 리소스 또는 기능에 대한 엑세스 권한을 부여하는 과정(절차)

- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
  
  - 사용자는 조직에 대한 액세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함

- 서류의 등급, 웹 페이지에서 글을 조회 & 삭제 & 수정 할 수 있는 방법, 제한 구역
  
  - 인증이 되었어도 모든 권한을 부여 받는 것은 아님

- 403 Forbidden
  
  - 서버는 클라이언트가 누구인지 알고 있어서 403 반환

---

> Authentication and Authorization work together

- 회원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생성
  
  - 인증 이후에 권한이 따라오는 경우가 많음

- 단, 모든 인증을 거쳐도 권한이 동일하게 부여 되는 것은 아님
  
  - Django에서 로그인을 했더라도 다른 사람의 글까지 수정 / 삭제가 가능하진 않음

- 세선, 토큰, 제 3자를 활용하는 등의 다양한 인증 방식이 존재

---

> 인증 여부를 확인 하는 방법 - 인증

- BasicAuthentication
  
  - 가장 기본적인 수준의 인증 방식 HTTP 쿠키 이용

- SessionAuthentication
  
  - Django에서 사용했던 session 기반의 인증 시스템
  
  - DRF와 Django의 session 인증 방식은 보안적 측면을 구성하는 방법에 차이가 있다
  
  - 세션을 이용하는 방법

- RemoteUserAuthenticaton
  
  - Django의 Remote user 방식을 사용할 때 활용하는 인증 방식
  
  - OAuth 방식 - 이거 외부에서 인증하는거로 카카오, 페이스북 로그인할때 사용

- TokenAuthentication
  
  - 매우 간단하게 구현 할 수 있음
  
  - 기본적인 보안 기능 제공
  
  - 다양한 외부 패키지가 있음
  
  - 토큰을 이용하는 방식

---

> 토큰과 세션의 차이

- 토큰
  
  - 일종의 통행증을 입장하는 클라이언트(손님)이 통행증과 정보를 들고 게시물에 접근하는 방법
  
  - 가장 유명한 방법이 JWT 방법
  
  - 사용자가 서버에 필요할 때 토큰을 넘기므로 서버에 부하가 덜함

- 토큰의 단점
  
  - 해킹당할 위험이 있음
  
  - 무겁다 - 기본적으로 토큰들고 왔다갔다 하면 네트워크가 무거움 네트워크의 통행량이 세션에 비해 무거움
  
  - 통행증을 한번 발급 하고 나면 더이상의 관리가 안된다. 놀이동산 암표느낌으로 생각하면 됨 통행증 이다보니 이 표를 다른 사람에게 줘 버리면 관리가 안됨
  
  - 기기접속제한 같은거 어려움 왜나면 표를 계속 넘겨줘 버리면 다른 기기에서도 쉽게 접근이 가능하기 때문 그래서 토큰에 유효기간을 설정하는 형식으로 기기관리를함

- 세션
  
  - 서버가 출입명부를 관리하는 느낌임
  
  - 근데 출입하려는 사람의 수가 많다면? 서버에 부하가 많이 걸린다.
  
  - 기기관리 매우 쉬움
    
    - 왜냐면 출입명부에서 삭제해버리면 끝이라서

---

> Dj-REST-Auth

- 회원가입, 인증, 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API end point 제공

- django-rest-auth 라고 이름 똑같은거 있는데 이거 업뎃 더이상 안하니까 dj-rest-auth로 잘 확인하고 써야함
