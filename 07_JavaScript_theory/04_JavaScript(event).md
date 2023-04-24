# 04_JavaScript(event)

## event

- HTML요소에서 발생하는 모든 상황

- 클릭, 키보드 키 입력, 브라우저닫기, 데이터제출, 텍스트 복사 .... 등등이 있다.

---

> Event object

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

- 이벤트가 발생했을 때 생성되는 객체

- Event 발생
  
  - 마우스 클릭, 키보드 누르기 등 사용자 행동으로 발생할 수 도 있고
  
  - 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있다.

- DOM 요소는 Event를 받고('수신)

- 받은 Event를 '처리' 할 수 있음
  
  - Event 처리는 주로 addEventListener() 메서드를 통해 처리
  
  - 다양한 html에 부착하여 처리한다.

---

> Event handler

- 일반적인 JavaScript Function을 정의하여 사용

- 웹 페이지에서 발생하는 Event에 대해 반응하여 동작하는 함수를 지칭

- 이벤트가 발생하면 Event handler 함수가 호출되며, Event객체를 매개 변수로 전달 받음

- 대상에 특정 Event가 발생하면, 할 일을 등록하자
  
  `EventTarget.addEventListener(type, handler function)`
  
  - 지정한 Event가 대상에 전달될 때 마다 호출할 함수를 설정
  
  - Event를 지원하는 모든 객체(Element, Document, Window등)를 대상(EventTarget)으로 지정 가능
  
  - type
    
    - 반응 할 Event 유형을 나타내는 대소문자 구분 문자열
    
    - 대표 이벤트
      
      - input, click, submit ...
  
  - handler function
    
    - 지정된 타입의 Event를 수신할 객체
    
    - JavaScript function 객체(콜백 함수)여야 함
    
    - 콜백 함수는 발생한 Event의 데이터를 가진 Event객체를 유일한 매개변수로 받음

---

> button Event

- 버튼을 클릭하면 특정 변수 값 변경하기
  
  1. button 선택
     
     `const button = document.querySelector('#btn')`
  
  2. button에 Event 추가
     
     `button.addEventListener('click', function (event) { 함수작성 }`
  
      2-1 `함수작성` 부분
  
  - 함수로 실행할 부분 작성 >> 특정 변수 값 변경하기
    
    1. 함수밖에 특정 변수 선언    
       
       `let count = 0`
    
    2. 함수 안에서 변수값 변경하기
       
       `count += 1`
    
    3. 변경 후 작성할 부분 가져오기
       
       `const counter = document.querySelector('#counter')`
       
       `counter.innerText = count`

```javascript
let count = 0
const button = document.querySelector('#btn')
button.addEventListener('click', function (event) {
    count += 1
    const counter = document.querySelector('#counter')
    counter.innerText = count
}
```

---

> input Event

```javascript
const textInput = document.querySelector('#text-input') // input 선택
textInput.addEventListener('input', function (event) {
    const pTag = document.querySelector('p')
    pTag.innerText = event.target.value    // 이벤트 대상의 값 받아서 pTag에 작
}
```
