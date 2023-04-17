# git undoing

1. git restore
- 워킹 디렉토리에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
- restore로 파일을 되돌리면 해당 내용을 복원할 수 없음

1. git restore --staged 파일이름
  - root - commit이 있는 경우 사용하는 방식

2. git rm --cached 파일이름
  - Staging Area에 반영된 파일을 워킹디렉토리로 되돌리기
  - 워킹디렉토리에서 작업한 파일을 git add로 올렸을때 파일의 수정사항이 발생해서
  - 수정사항 까지 반영한 후 다시 add 하고 싶을때 add 취소하는 명령어

3. git commit --amend
  - 커밋을 완료한 파일을 staging Area로 되돌리기
  - 빔 상태로 들어와서 i 혹은 insert 입력하면 수정 가능상태로 바뀜
  - 빔 상태에서 수정후 :wq 입력하면 종료됨

# git reset

- git reset [옵션] {커밋 ID}
  
  - 커밋 ID 확인하기
  - git log --oneline 찍었을때 commit 멘트 앞에 나오는 16진수의 난수가 커밋 ID

- soft
  
  - 해당 커밋으로 되돌아가고 되돌아간 커밋 이후의 파일들은 stageing Area로 되돌려 놓음
  - 워킹 디렉토리에서 스테이지 에이리어로 돌아감

- mixed
  
  - git reset 옵션의 기본값
  - 기본값이니 옵션에 값을 안넣고 실행하면 mixed 실행됨
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후의 파일들은 워킹 디렉토리로 돌려놓음
  - 이걸 제일 많이 쓸거 같음

- hard
  
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후의 파일들은 모두 워킹 디렉토리에서 삭제

# git revert

- git revert {커밋 ID}
  - 빔상태로 넘어가는데 과거를 없던일로 만든다는 커밋을 새로 남김
  - 커밋 메시지는 기본적으로 revert {커밋내용} 으로 수정됨
  - 이 상태에서 다시 esc 로 나가서 :wq 써서 종료해주면 정상적으로 커밋이 남게된다.

## git reset vs git revert

> reset - 커밋 내역을 삭제
> revert - 새로운 커밋 생성
> 
> - github를 이용해 협업을 할때 커밋 내역의 차이로 인한 충돌 방지 가능

# git branch

- 브랜치는 독립 공간을 형성하기 때문에 원본에 대해 안전하다.
- 하나의 작업은 하나의 브랜치로 나누어 진행하므로 체계적인 개발이 가능하다.

## branch

1. 생성
   
   - git branch {브랜치 이름}

2. 작업공간 이동하기
   
   - git switch {브랜치 이름}
   - 작업 후 다시 master로 이동

## 작업결과물 합치기

1. fast - forward
  - git merge {브랜치 이름}

  `>>>` fast-forward master에서는 작업이 이루어 지지 않고 dev 라는 브랜치에서만 작업이 이루어 졌으므로 상관이 없음

**가장많이 사용될 merge 방법**
2. 3 - way - merge

  - master 와 dev 브랜치 둘다 작업이 일어난 경우
  - git merge {브랜치 이름}
  
  > 빔 창으로 넘어간 후 새로운 commit 을 남기고 master의 헤드를 땡겨서 둘다 합쳐줌
  > 빔 창에서는 i / esc / :wq 순서로 정상종료 해서 commit 남겨주기
3. merge conflict
  - merge 할때 같은 부분을 수정해서 충돌이 일어난 경우
  - git merge dev 하면 수정된 파일이 같이 띄워짐
  - ex) md 파일일 때 작업자가 직접 사용할 부분을 수정해주면 된다.
  - 그때 bash 창은 master|merge 라고 써져 있는데 이때 수정을 완료하면 git add 파일명
  - git commit -m 새로운 커밋 남기기 하면 정상적으로 수정후 작업이 완료된다.
  - 브랜치 파일에도 수정사항을 적용하려면 switch로 이동후 merge 해주면 됨