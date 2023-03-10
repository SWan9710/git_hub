# Tree

- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.
  
  - 노드 중 최상위 노드를 루트라고 한다.
  
  - 노드 - 트리의 원소
  
  - 간선 - 노드를 연결하는 선, 부모 노드와 자식 노드를 연결
  
  - 루트 노드 - 트리의 시작 노드
  
  - 형제 노드 - 같은 부모 노드의 자식 노드들
  
  - 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
  
  - 서브 트리 - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
    
    - 끊고 나면 새로운 트리가 생기는데 그때 또 최상위 노드를 루트라고 함ㅋ
  
  - 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들

- 차수
  
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  
  - 트리의 차수 : 트리에 있는 노드의 차수 중 가장 큰 값
  
  - 단말 노드(리프 노드) : 차수가 0인 노드, 자식 노드가 없는 노드
  
  - 진입차수 : 해당 노드로 들어올 수 있는 차수(부모노드의 수)
  
  - 진출차수 : 본인 노드를 기준으로 나갈 수 있는 노드의 갯수

- 높이
  
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨(상대적인 값)
  
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨

## 이진트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리

- 각 노드가 자식 노드를 최대 2개 까지만 가질 수 있는 트리
  
  - (왼쪽, 오른쪽)

### 이진트리의 특성

- 레벨 i 에서 노드의 최대 갯수는 2^i개

- 높이가  h인 이진 트리가 가질 수 있는 노드의 최소 개수는 h+1개 가 되며, 최대 개수는 2^h+1 - 1 개가 된다

## 포화 이진 트리

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리

- 높이가 h 일때 최대의 노드 개수인( 2^h+1 - 1)의 노드를 가진 이진 트리

- 루트를 1번으로 하여 2^h+1 - 1 까지 정해진 위치에 대한 노드 번호를 가짐

- ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-02-22-09-27-51-image.png)

약속

루트는 1번 왼쪽에서 오른쪽으로 가면서 번호를 붙이고 아래로 내려가고 2가 빠지지 않고 꽉 차 있다.

## 완전 이진 트리

- 높이가 h이고 노드 수가 n개일 때(단, 2^h <= n < 2^h+1 - 1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈자리가 없는 이진 트리

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-02-22-09-39-25-image.png)

## 편향 이진 트리

- 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진트리

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-02-22-09-40-17-image.png)

## 이진트리 순회

- 트리의 각 노드를 중복되지 않게 전부 방문하는 것

- 트리는 비 선형 구조이기 때문에 선형구조에서 괕이 선후 연결 관계를 알 수 없다.

## 3가지 순회방법 (중요)

- 부모노드의 처리 순서에 따라 전위 / 중위 / 후위 로 나누어진다.

- 전위 순회
  
  - 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.
  
  - 1 부모 / 2 왼쪽자식 / 3 오른쪽자식 순서

- 중위 순회
  
  - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.

- 후위 순회
  
  - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.

## 배열을 이용한 이진 트리의 표현

- 노드 번호의 성질
  
  - 노드 번호가 i인 노드의 부모 노드 번호 i // 2
  
  - 노드 번호가 i인 노드의 왼쪽 자식 번호는 i * 2
  
  - 노드 번호가 i인 노드의 오른쪽 자식 번호 i * 2 + 1
  
  - 레벨 n의 노드 번호 시작 번호는  2 ^ n

## 이진 탐색 트리

- 탐색작업을 효율적으로 하기 위한 자료 구조

- 모든 원소를 서로 다른 유일한 키를 갖는다

- 왼쪽 서브트리는 루트노드보다 작고

- 오른쪽 서브트리는 루트노드보다 크다

- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

- 수정사항----------------------------------------------------------------
