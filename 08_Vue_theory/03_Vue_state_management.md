# Vue State Management

> 상태관리

- 상태란?
  
  - 현재에 대한 정보
  
  - 현재 App이 가지고 있는 Data로 표현할 수 있음

- 여러개의 component를 조합해서 하나의 App을 만들고 있음

- 각 component는 독립적이기 때문에 각각의 상태를 가진다.

- 하지만 결국 이런 component들이 모여서 하나의 App을 구성할 예정
  
  즉, 여러 개의 component가 같은 상태를 유지할 필요가 있음
  
  => 상태관리가 필요하다

한명(하나)이 관리하면 상태관리가 편하다

Vuex 는 이런 상태를 하나로 몰아서 관리

---

> props와 emit을 

- props와 emit을 이용하여 각각 상태를 관리하고 있었다

- 각 컴포넌트는 독립적으로 데이터를 관리 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음

- 데이터의 흐름을 직관적으로 파악 가능

- 그러나 컴포넌트의 중첩이 깊어지면 데이터 전달이 쉽지 않다.

---

> Centralized Store(인공위성)

- 중앙 저장소에 데이터를 모아서 상태 관리

- 각 컴포넌트는 중앙 저장소의 데이터를 사용

- 컴포넌트의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음

- 중앙 저장소의 데이터가 변경되면 각각의 컴포넌트는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함

- 바뀐 데이터에 반응하여 다른 컴포넌트역시 바뀜

- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 편하다

---

## Vuex

> state

- vue 인스턴스의 data에 해당

- 중앙에서 관리하는 모든 상태 정보

- 개별 컴포넌트는 state에서 데이터를 가져와서 사용
  
  - 개별 컴포넌트가 관리하던 data를 중앙저장소에서 관리하게 됨

- state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 컴포넌트도 자동으로 다시 렌더링
  
  `$store.state로 state 데이터에 접근`

보통 중앙저장소에서 데이터를 관리하고 상황에 따라 개별로 데이터를 관리할때도 있다.

---

> Mutations & Actions

- vue component의 methods 역할이 vuex에서는 아래와 같이 분화됨

- Mutations
  
  - state를 변경

- Actions
  
  - state 변경을 제외한 나머지 로직

---

> Mutations

- <mark>실제로 state를 변경하는 유일한 방법</mark>

- 호출되는 핸들러 함수는 반드시 동기적 이어야 한다.
  
  - 비동기호출 axios X

- 보통 전체를 대문자로 작성

- 첫 번째 인자로 state를 받으며, 

- component 혹은 Actions에서 commit() 메서드로 호출됨

---

> Actions

- 비동기 작업을 포함할 수 있다

- context 객체를 인자로 받으며 store.js의 모든 요소와 메서드에 접근할 수 있음

- state를 직접 변경할 수 있지만 하지 않아야 함

- component에서 dispatch() 메서드에 의해 호출됨

---

> Getters

- vue 의 computed에 해당

- state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음

- getters의 결과는 캐시(cache) 되며, 종속된 값이 변경된 경우에만 재계산 됨

- 계산된 값은 state에 영향을 미치지 않음

- 첫번째 인자로 state, 두번째 인자로 getters 받음

---

> 데이터의 흐름(조작)

1. component 에서 dispatch로 actions 호출

2. state 변경시 actions에서 commit으로 mutations 호출

3. nutations에서 state 변경

> 데이터의 흐름(사용)

1. state에서 getters 호출

2. getters에서 component 호출


