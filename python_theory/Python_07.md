# Python Track #6

## 셋(Set)

- Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
  
  - 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
  
  - 순서가 없기 때문에 인덱스를 이용한 접근 불가능

- 수학에서의 집합을 표현한 컨테이너
  
  - 집합 연산이 가능(여집합을 표현하는 연산자는 별도로 존재 X)
  
  - 중복된 값이 존재하지 않음

- 담고 있는 요소를 삽입, 변경, 삭제 가능 -> 가변 자료형(mutable)

### 셋 메서드

![loading-ag-209](C:\Users\SSAFY\Desktop\git_hub\git_hub\python_theory\python_06_assets\�Θ�.PNG)

## 딕셔너리(Dictionary)

- 키-값(key-value) 쌍으로 이뤄진 자료형(3.7부터는 ordered, 이하 버전은 unordered)

- Dictionary의 키(key)
  
  - key는 변경 불가능한 데이터(immutable)만 활용 가능
    
    - string, integer, float, boolean, tuple, range

- 각 키의 값(values)
  
  - 어떠한 형태든 관계없음

### 딕셔너리 메서드

![loading-ag-213](C:\Users\SSAFY\Desktop\git_hub\git_hub\python_theory\python_06_assets\�Θ�1.PNG)

- 뷰 : 반복 가능한 객체

## 얕읕 복사와 깊은 복사(Shallow Copy & Deep Copy)

- 기존 변수 사용 과정에서의 문제점
  
  : 하나의 기억에, 하나의 주소가 필요
  
  -> 100개 저장하려면 주소 100개 필요

- 연속적인 공간에 데이터가 저장되도록 함
  
  -> 맨 처음 기억의 주소만 필요

### 얕은 복사

: 기존 데이터의 주소와 같은 주소를 같도록 복사

### 깊은 복사

: 기존 데이터의 주소와 다른 주소를 같도록 복사

### 복사 방법

- 할당 (Assignment)
  
  : 대입 연산자(`=`) : 객체 참조를 복사

- 얕은 복사 (Shallow Copy)
  : 리스트의 원소가 주소를 참조하는 경우
  
  ```python
  copy_list = original_list
  # 같은 주소를 가짐 : 얕은 복사
  # 다른 주소를 갖게 하려
  # 슬라이싱 or copy.copy
  ```
  
  -> 참조는 복사하지 않음 : 깊은 복사 X

- 깊은 복사 (Deep Copy)
  
  ```python
  import copy
  a = [1, 2, ['a', 'b']
  b = copy.deepcopy(a)
  # 리스트 속 참조와 참조 속의 참조까지 복사
  a=[1, 2, ['a' ,'b']]
  b=a[0:2]+[a[2][:]]
  ```
