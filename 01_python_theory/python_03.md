# python_03

## 함수

> - ### 분해
>   
>   - 기능을 분해하고 재사용 가능하게 만든다
>   
>   - 전체 스크립트 기준으로 특정 로직으로 함수를 분해해서 사용한다.
> 
> - ### 추상화
>   
>   - 복잡한 내용을 모르더라도 사용할 수 있도록(스마트폰) 재사용서와 가독성, 생산성
>   
>   - 내부 구조를 변경할게 아니라면 몰라도 무방
>     
>     - 스마트폰의 원리를 잘 몰라도 우리는 잘 사용할 수 있음

## 함수 기초

> ### 함수의 종류
> 
> 1. **내장함수**
>    
>    - 파이썬에 기본적으로 포함된 함수
> 
> 2. **외장함수**
>    
>    - import 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
> 
> 3. **사용자 정의 함수**
>    
>    - 직접 사용자가 만드는 함수
> 
> ### 함수의 정의
> 
> - 특정한 기능을 하는 코드의 조각(묶음)
> 
> - 특정 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 간편히 사용
>   
>   - 선언과 호출define & call
>   
>   - 입력(input)
>   
>   - 문서화(docstring)
>   
>   - 범위(scope)
>   
>   - 결과값(output)

<함수의 기본 구조>

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-01-18-09-25-06-image.png)

`def 식별자(파라미터)`

`     (설명)       `

`결과값`

구조로 이루어짐

> ### 선언과 호출
> 
> - 함수의 선언은 def 키워드를 활용
> 
> - 들여쓰기를 통해 실행될 코드블록을 작성
>   
>   - docstring는 함수 앞에 선택적으로 작성 가능
> 
> - 함수는 parameter를 넘겨줄 수 있음
> 
> - 함수 동작 후 return을 통해 결괏값을 전달함
> 
> - 함수명() 으로 호출하여 사용
>   
>   - parameter가 있는 경우 함수명(값1, 값2)로 호출
> 
> - `함수명() > 전부다 함수`
> 
> - 함수는 호출되면 코드를 실행하고 return값을 반환하며 종료
> 
> ### 함수의 결과값
> 
> - void function
>   
>   - 명시적인 return값이 없는 경우, none를 반환하고 종료
>   
>   - 밖으로 값을 반환하는게 없음
> 
> - value returning function
>   
>   - 함수 실행 후, return문을 통해 값 반환
>   
>   - `return을 하게 되면, 값 반환 후 함수가 바로 종료`
>   
>   - return값 이후에 로직을 더 작성해도 return값을 만나면 로직이 종료되고 값이 반환되어 함수가 종료된다.
> 
> ### pritn vs return
> 
> - print를 사용하면 호출될 때마다 값이 출력됨
> 
> - 데이터의 처리를 위해서는 return 사용
> 
> <img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2023-01-18-09-36-59-image.png" alt="" width="703">
> 
> ### 두 개 이상의 값 반환
> 
> - 튜플을 활용하여 두개 이상의 값 반환
> 
> - 튜플은 immutable 값이라서 튜플로 반환
> 
> - ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-01-18-09-39-57-image.png)
> 
> - 리스트 값으로 반환 하려면 return [x-y, x*y] 형식으로 반환가능
> 
> - 리스트, 딕셔너리 같은 컨테이너를 활용하면 된다.
> 
> ### 함수의 입력
> 
> - parameter : 함수를 정의할 때 사용
> 
> - argument : 함수를 호출 할 때, 넣어주는 값
>   
>   - 함수의 parameter을 통해 전달되는 값
>   
>   - 필수 / 선택 으로 나누어 진다
> 
> - positional argument
>   
>   - 기본적으로 함수 호출 시 argument는 위치에 따라 함수 내에 전달됨
> 
> - keyword argument
>   
>   - 직접 변수의 이름으로 특정 argument를 전달할 수 있음
>   
>   - 키워드 알규먼트는 항상 포지셔널 알규먼트 뒤에온다
>   
>   - 즉 복잡한 애들은 항상 뒤에서 나와야 한다.
>   
>   - ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-01-18-09-46-07-image.png)
> 
> - default argument values
>   
>   - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
>   
>   - 함수를 정의 할때부터 파라미터에 특정값을 넣어주는 것
>   
>   - 마찬가지로 함수 정의할때 복잡한게 뒤로 가야함
>   
>   - 정의된 것 보다 더 적은 개수의 argument들로 호출될 수 있음
>   
>   - 기본값이 지정된 파라미터에는 호출시 알규먼트에 값을 안넣어도 호출시 기본값이 들어가서 나옴

## python의 범위(scope)

> - name space(이 식별자는 이값이구나 하고 잠시 저장하는 공간, 이름을 기억하는 공간)
>   
>   - 같은 이름이 여러곳에 존재할 수 있다.
>   
>   - built-in name space : 내장된 공간(print, sum, dict,,,,)
>   
>   - global name space : 프로그램 로직이 실행될 때 생성되는 공간
>   
>   - enclosed name space : 함수안에 다른 함수가 들어있을때 바깥쪽에 있는 함수의 name space
>   
>   - local name space : 어떤 함수를 실행할때 함수 안쪽에 생성되는 공간
> 
> - scope
>   
>   - 변수의 제한범위
>   
>   - 찾고자 하는 함수의 프로그램상의 제한범위
>   
>   - 찾는 순서가 L > E > G > B(작은곳에서 큰곳으로 감)
>   
>   - 모든곳을 다 돌아도 값이 없으면 error를 반환
>   
>   ```python
>   def func():
>       a = 20
>       print('lacal', a) # local 20
>   func()
>   print('global',a) #NameError : name 'a' is not defined
>   ```
> 
> - 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
> 
> - ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-01-18-10-16-19-image.png)
> 
> - 파란색 > local scope
> 
> - 빨간색 > global scope
> 
> - scope
>   
>   - global scope : 함수 어디에서든 참조 가능한 공간
>   
>   - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능
> 
> - variable
>   
>   - global variable : global scope에 정의된 변수
>   
>   - local variable : local scope에 정의된 변수
> 
> ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-01-18-10-28-19-image.png)
> 
> x의 참조시점이 글로벌임 why? > l>e>g>b 순으로 x의 값을 찾는데 l과e에 없음
> 
> g에 x값이 있으므로 글로벌로 반환됨
> 
> 만약 값이 enclosing 에 있다면 인클로징 값이 반환됨
> 
> local에 값이 있다면 로컬값이 반환됨
> 
> ### 변수 수명주기
> 
> - built-in scope
>   
>   - 파이썬이 실행된 이후부터 영원히 유지
> 
> - global scope
>   
>   - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날때까지 유지
> 
> - local scope
>   
>   - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
> 
> 로컬 스코프 공간에서 글로벌 값을 호출하고 싶을때
> 
> 함수 안에서 `global 변수명` 을 선언해주면 변수 값을 로컬이 아닌 글로벌에서 찾아옴
> 
> 범위 설정시 글로벌 말고 다른 구역을 찾고 싶을때는
> 
> `nonlocal` 설정 > local을 감싸고 있는 첫번째 함수를 가져옴 >> 인클로징에 있는 함수값 가져옴
> 
> ### 함수의 범위 주의
> 
> - 함수 내에서 필요한 상위 변수는 argument로 넘겨서 사용할 것
> 
> - 함수로 값을 바꾸고자 한다면 항상 argument로 넘겨서 사용할 것
