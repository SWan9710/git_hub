# SQL DML 활용 및 CRUD

## Aggregate function (집계함수)

- 여러행의 값들을 하나의 결과로 뽑아내는 것

- 제공하는 함수들
  
  > - avg(), count(), max(), min(), sum()



<mark>전체 유저의 평균 balance를 알고 싶다면?</mark>

- SELECT avg(balance) FROM users;



## GROUP BY

- 특정 그룹으로 묶인 결과를 생성

- 선택된 컬럼 값을 기준으로 데이터(행) 들의 공동 값을 묶어서 결과로 나타냄

- SELECT 문에서 선택적으로 사용가능한 절

- WHERE 절이 포함될 경우 WHERE 절 뒤에 작성

- 각 그룹에 대해 집계 함수를 적용하여 각 그룹에 대한 추가적인 정보 제공가능



## Changing data

- 데이터를 삽입, 수정, 삭제

- INSERT

- UPDATE

- DELETE

### INSERT

> `INSERT INTO table_name(column_1, column_2) VALUES(values1, values2)`
> 
> - table_name 뒤에 column 안써도 insert 작성가능

- 단일행 삽입하기
  
  ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-09-43-53-image.png)

- 컬럼순서 없이 여러행 삽입하기

        ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-09-44-17-image.png)



### UPDATE

> `UPDATE table_name SET column1 = new_value1, column2 = new_value2 WHERE search_condition;`
> 
> WHERE 절의 조건을 사용하여 업데이트할 행을 지정
> 
> WHERE 생략하면 UPDATE문은 테이블의 모든 행에 있는 데이터를 업데이트



- 2번 데이터의 이름을 '김철수한두루미', 주소를 '제주도'로 수정하기

        ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-09-47-34-image.png)

### DELETE

> `DELETE FROM table_name WHERE search_condition;`
> 
> 테이블에서 행을 제거
> 
> DELETE FROM 뒤에 제거할 테이블 이름 지정
> 
> WHERE 절은 선택사항, 생략시 테이블의 모든 행을 삭제
> 
> <mark>DROP TABLE 과는 다른거</mark>



- 테이블에서 행 제거
  
  ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-09-51-59-image.png)



- DELETE 에 조건 넣기
  
  ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-09-52-22-image.png)



- 모든 데이터 삭제하기
  
  ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-09-52-42-image.png)



# 정규형(시험에 최대한 안나온다노)

> 테이블을 나누는 이유
> 
> - 테이블을 나누지 않고 그냥 작성한다면 데이터의 중복이 발생함
> 
> - 또한 삽입, 수정, 삭제가 일어날때 데이터의 유지보수가 어렵고 데이터의 무결성을 유지하기 어렵다
> 
> - 이 모든것을 쉽게하기 위해 테이블을 나누어서 관리하는 것



## 데이터베이스 정규형

- 데이터베이스를 구조화 하는 방법

- 데이터의 중복을 최소화 하고 일관성과 무결성을 보장하기 위함

- 구조를 더 좋게 바꾸는 걸 정규화 라고 한다.



## 제 1 정규형

- 하나의 속성값이 복수형을 가지면안된다

- 하나의 속서에는 값이 하나만 들어가야 한다는 소리
  
  ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-10-16-21-image.png)
  
  이게 안된다는 소리



## 제 2 정규형

- 테이블의 기본키에 종속되지 않는 컬럼은 테이블이 분리 되어야함

- 테이블과 관련 없는 애들은 따로 분리하라는 것

- 테이블의 테마와 관련없는 컬럼은 다른 테이블로 분리하는 것
  
  ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-10-18-17-image.png)



## 제 3 정규형

- 다른 속성에 의조하는(종속)하는 속성을 따로 분리할 것

- 테이블의 PK값을 기준으로 해당 속성이 PK에 종속되나 알아보고 PK에 종속하지 않는 다른 속성을 분리 하는것



# JOIN

![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-11-05-17-image.png)

데이터 형식이 위와 같이 주어질때

- 두개 이상의 테이블에서 데이터를 가져오 결합 하는것

- 테이블 합치기
  
  `SELECT * FROM articles, users;`
  
  ![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-11-05-48-image.png)
  
  aritcles 테이블의 1번 id 일때 users 3개의 데이터 모두 들고오고 반복해서 총 9개의 데이터 나오는거
  
  `>>>`  이렇게 된거를 CROSS JOIN 이라고 함
  
  

## INNER JOIN

![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-11-07-01-image.png)

`SELECT * FROM articles, users WHERE articles.userid = users.rowid;`

`SELECT * FROM articles INNER JOIN users ON users=users.rowid;`

여기서 articles의 userid 와 users의 rowid 가 서로 같은 값 이므로 

해당하는 값이 같을때 테이블을 들고오게 1번처럼 작성해도 되고

2번처럼 INNER JOIN 사용해서 작성해도 된다.



## LEFT JOIN

![](SQL%20DML%20활용%20및%20CRUD_assets/2023-04-06-11-09-14-image.png)

- 왼쪽 테이블의 데이터를 기준으로 오른쪽 데이터를 결합

- 왼쪽테이블의 모든 데이터를 가져오고 오른쪽 데이터의 있는값만 가져오고 없는값은 NULL 처리

`SELECT * FROM articles LEFT JOIN users ON userid = users.rowid;`



## RIGHT JOIN

`SELECT * FROM articles RIGHT JOIN users ON userid = users.rowid;`


