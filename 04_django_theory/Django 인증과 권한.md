# Django 인증과 권한

- 장고 인증시스템

- 필수구성은 settings.py에 이미 포함됨

- INSTALLED_APPS에서 확인 가능하다

django.contrib.auth



- Authentication(인증)
  
  - 신원 확인
  
  - 사용자가 자신이 누구인지 확인하는 것

- Authorization(권한, 허가)
  
  - 권한 부여
  
  - 인증된 사용자가 수행할 수 있는 작업을 결정



## django 인증과 권한 사전 설정

> 1. 두번째 앱 accounts 생성 및 등록
> 
> 2. url 분리 및 매핑



## Custom User Model

> - django에서 User Model을 기본적으로 제공해 주는데 대부분 custom user model로 대체한다
> 
> - 개발자들이 작성하는 일부 프로젝트에서는 장고의 내장 user-model의 요구사항이 적절하지 않을 수 있으므로 대체하여 사용
> 
> - settings.py에 AUTH_USER_MODEL 설정해 주기



## 대체하기

> 1. AbstractUser 상속받는 커스텀 User 클래스 작성
>    
>    - from django.contrib.auth.models import AbstractUser
>    
>    - class User(AbstractUser)
> 
> 2.  settings.py에 AUTH_USER_MODEL = 'accounts.User' 작성
> 
> 3. admin.py에 User 모델 등록
>    
>    - from django.contrib.auth.admin import UserAdmin
>    
>    - from .models import User
>    
>    - admin.site.register(User, UserAdmin)
> 
> **Django 새 프로젝트 시작할 때 기본 User 모델이 충분해도 커스텀 User 모델 설정하는것을 강력하게 추천**
> 
> 커스텀 모델은 기본과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정을 할 수 있기 때문에



## [주의] 프로젝트 중간에 AUTH_USER_MODEL 변경하기

> - 모델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업이 필요
> 
> - ~~~ 뭐가 많은데 결론은 중간 변경 권장 X



# 쿠키

> - HTTP 쿠키는 상태가 있는 세션을 만들도록 해줌
