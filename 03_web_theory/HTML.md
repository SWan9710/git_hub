# HTML

> 

- 작성방법

```html
<!DOCTYPE html>
<html>
<head> </head>
<body> </body>
</html>
```

형태로 작성이 가장 기본

## <head>

1. `<title> </title>`
   
   - 상단의 타이틀 명을 작성하는 구역

2. `<link> </link>`
   
   - 부트스트랩, css 파일등을 연결하기 위해 head에 작성하는 요소

3. `<style> </style>`
   
   - HTML 파일의 내부참조 스타일을 지정하기 위해 head에 작성하는 요소

모든 요소들은 중첩이 가능하며 오류를 반환하지 않고 레이아웃이 깨진채로 출력되기 때문에 디버깅이 힘들다.

## 속성(Attribute)

- 요소에 들어가는 태그(style, div, a, p, h1 ....)에 사용되는 것

- 속성명, 속성값 으로 구성되고 쌍따움표를 이용하여 작성한다.

## HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성

- id, class, style 등이 있음

## form

> - 사용자의 정보를 제출하기 위한 영역

- action, method 등이 있다 정도만 알면 될듯
  
  - 추가로 method는 GET, POST 등을 사용한다는데 설명해준적 없음

## input - label

> - input 과 label 은 세트로 생각해야 함

- label의 for 값과 input의 id 값은 항상 같아야 한다

- `<input type="" name="" id="">` 순으로 작성된다 순서를 꼭 지킬 필요는 없지만 지키는게 좋음

#### HTML 문서 만들때 참고하기

> - 영역을 나눠서 작성하는게 좋다.
> 
> - 크게 header / section / footer 등으로 나누기도 하고 전체의 영역을 하나의 container로 묶어서 작성하기도 한다

# CSS

> - 스타일을 지정하기 위한 언어
> 
> - <mark>선택자</mark> 를 통해 스타일을 지정할 HTML 요소 선택
> 
> - 중괄호 안에서는 속성과 값으로 하나의 쌍으로 이루어진 선언을 진행한다.

## CSS의 정의방법

> - 인라인
>   
>   - HTML 태그에 직접 style 속성을 지정
> 
> - 내부참조
>   
>   - head 태그 내에 style을 지정
> 
> - 외부참조
>   
>   - 외부에 css 파일을 따로 만들고 link를 통해 파일을 불러옴

## 선택자

> - `* {}` : 전체 선택자
> 
> - `h1 {} / h2 {} ...` : 요소 선택자
> 
> - `.green {}` : 클래스 선택자
> 
> - `#red {}` : 아이디 선택자
> 
> - `.box > p {}` : 자식 결합자
> 
> - `.box p {}` : 자손 결합자

자식 결합자와 자손 결합자의 차이

예를 들어 

```html
<div><p>안녕<span>하세요</span>ㅎㅎ</p></div>
```

이렇게 작성된 파일이 있을때

div의 자식은 p 이고 p의 자식이 span임

div 안에 p 가 있는데 p 안에 span이 있는 형태이므로 span은 div의 자손에 해당한다.

그래서 스타일을 지정할때 span에 스타일을 지정하고 싶으면 div span {} 또는 p > span {} 으로 작성해야 함

## CSS 우선순위(중요!!!)

> - 인라인 > id > class, 속성 > 요소 순서
> 
> - 그런데 !importatn 를 작성해버리면 우선순위를 끌어 올릴 수 있음 그러다 스타일이 겹처거나 혼돈이 올 수 있으니 작성에 유의해야 함
> 
> 또한 스타일을 지정할 때 태그의 요소로 클래스를 지정할때 클래스를 여러개를 지정 했다고 해도 <mark>외부참조 css 파일이나 head의 내부참조 style의 작성 순서에 따라</mark> 스타일이 지정 된다. <mark>(위에서 아래로)</mark>

## CSS 상속

> - 상속을 통해 부모 요소의 속성을 자식에게 상속

text 관련 요소들만 상속되고 box model 관련 요소들은 상속되지 않는다.

## CSS 원칙

> - 모든 요소는 네모(box model) 이고 위에서 아래로, 왼쪽에서 오른쪽으로 쌓인다.
> 
> - display에 따라 크기와 배치가 달라진다.

## Box model

> - 모든 HTML 요소는 box 형태로 되어있고 하나의 box 는 4개의 영역으로 이루어짐
> 1. content
>    
>    - 글이나 이미지 등 요소의 실제 내용
> 
> 2. padding
>    
>    - 테두리 안쪽의 내부 여백, <mark>이미지는 padding 까지 적용된다.</mark>
> 
> 3. border
>    
>    - 테두리 영역
> 
> 4. margin
>    
>    - 테두리 바깥의 외부 여백, 배경색 지정 X

## Box model 구성(margin, padding, border)

> - margin
>   
>   - 상하좌우를 기억하자
>   
>   - `margin : 10px;` ==> 4부분 모두 10px
>   
>   - `margin : 10px 20px;` ==> 상하로 10 / 좌우로 20
>   
>   - `margin : 10px 20px 30px;` ==> 위로 10 / 좌우로 20 / 아래로 30
>   
>   - `margin: 10px 20px 30px 40px;` ==> 위에서 부터 시계방향으로 스타일 적용 위 / 오른쪽 / 아래 / 왼쪽 순서

## Box-sizing

> - 기본적으로 box-sizing 은 contetn 영역으로 지정되어 있음
> 
> - 하지만 우리 눈에 보이는건 border 까지임
> 
> - 보통 box-sizing 을 border-box 로 설정해서 사용함

## CSS Display

> - 인라인 / 블록 요소
> 
> - `display : block;`
>   
>   - 한 줄 전체를 차지하는 영역
>   
>   - 블록 요소 안에 인라인이 들어갈 수 있음
>   
>   - 한줄 전체를 차지하니 줄바꿈이 일어남
> 
> - `display : inline;`
>   
>   - content 만큼 차지하는 영역
>   
>   - content가 길면 줄바꿈이 일어나겠지 하지만 기본적으로는 줄바꿈이 일어나지 않음
>   
>   - width, height, margin-top, margin-bottom 속성 지정 불가
> 
> - 인라인-블록요소 / none 요소
> 
> - `display : inline-block`
>   
>   - 인라인 처럼 한줄표시가능, block처럼 width, height, margin 속성 지정 가능
> 
> - `display : none`
>   
>   - 해당 요소를 화면에 표시 안하고 공간도 차지 안함
>   
>   - 비슷한게 `visibility : hidden;` 이 있는데 공간은 차지하는데 표시는 안함

## CSS position

> - 문서 상에서 요소의 위치를 지정
> 
> - static(기본값)
> 
> - relative
>   
>   - 상대 위치 
>   
>   - 자기 자신의 static 위치를 기준으로 이동
>   
>   - 자기 위치를 버리지 않고 이동해서 relative 스타일 지정하면 다음 요소도 그 다음에 표시됨
> 
> - absolute
>   
>   - 절대 위치
>   
>   - 자기 위치를 버리고 다음위치로 가는거라 absolute로 스타일을 지정하면 다음 요소가 원래 있던 자리로 들어감
> 
> - fixed
>   
>   - 고정 위치
>   
>   - 네비바 생각하면 됨
> 
> - sticky
>   
>   - 몰라도 될듯
>   
>   - 그냥 화면이 내리다 임계점에 도달하면 그때 화면에 고정 된다는데 스크롤에 따라 포지션이 static > fixed로 바뀐다 뿐
>   
>   - 그니까 화면이 이제 바뀌면서 아래로 내려가야 하면 그때는 포지션이 고정되서 계속 화면에 비친다는 거임
>   
>   - 기존의 자신의 영역을 가지고 있기 때문에 fixed와 다르게 공간을 차지한다 우리 네비바 만들때 네비바 만들고 또 이미지나 문자 넣을때 네비바 밑으로 들어가는데 sticky는 안들어감 왜냐면 자신의 영역을 가지고 있기 때문임

## CSS 레이아웃

> - float
>   
>   - 말 그대로 둥실둥실 띄운다는 거
>   
>   - `float : left;`
>   
>   - `float : right;` 
>   
>   - 이게 absolute처럼 자기 위치를 버리고 위로 둥실 띄워버리는 거라 내용이 겹쳐서 표시 될 수 도 있다.
>   
>   - `clear:both;` 써서 공간을 없앤 뒤에 써야 겹치지 않고 작성 가능
> 
> - flex box
>   
>   - `display : flex`
>   
>   - 배치설정
>     
>     - `flex-direction`
>       
>       - 이거 flex-row, flex-column 이거임 어려운거 아님
>     
>     - `flex-wrap`
>       
>       - 이건 그냥 줄넘김 말하는거
>     
>     - 두개 한번에 쓸라면 flex-flow 쓰고 순서대로 direction 이랑 wrap 써주면 댐
>     
>     - `flex-flow : row nowrap;`
>   
>   - 공간나누기
>     
>     - `justify-content`
>       
>       - 자주쓰는거 이거 가로기준으로 정렬 해주는거 근데 위에 flex-direction으로 정렬을 column을 하면 세로로 정렬하니까 세로정렬이 되어버림 써보면 이해됨
>     
>     - `align-content`
>       
>       - 이거는 세로기준으로 정렬 해주는거
>     
>     - flex 속성의 items / self 로 나뉘는데 items가 컨테이너에 적용되는거고 적용된 속성에 따로 스타일 지정하려면 self로 적용해줘야 함

# Bootstrap

> - CDN
>   
>   - 컨텐츠를 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에서 데이터를 제공하는 시스템
> 
> - 1 rem 은 16px 

부트스트랩을 쓰는 가장 큰 이유가 반응형 웹 구현이 편리해서 쓰는거

반응형 웹?

- 모니터 화면별로 창을 띄웠을때 나타나는 모양이 다른데 그걸 일일이 지정안하고 부트스트랩 쓰면 편하다 이말임

## Grid

> - column 실제 컨텐츠가 담기는 부분
> 
> - gutter column 사이의 공간
> 
> - container column을 담고있는 공간

- 12 개 column 과 6개의 grid breakpoint 있음

전체를 container로 묶고 row로 한번더 공간을 나눈뒤에 그 공간에 들어갈 col을 넣어줌

넣어줄때 grid breakpoint 를 걸어줄 수 있음

- column 이 12개 이므로 사이즈를 조절해서 넣을 수 있음

```html
<div class="container">
  <div class="row">
    <div class="box col-9">col-9</div>
    <div class="box col-4">col-4</div>
    <div class="box col-3">col-3</div>
  </div>
</div>
```

이렇게 작성하면 12개의 길이 중 첫번째 col-9가 12칸중 9칸을 차지하고 뒤에오는 col-4는 칸이 모자라서 다음줄에 작성되고 그 옆에 col-3 이 작성 됨
