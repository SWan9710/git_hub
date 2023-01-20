# Git

> ## Git이란
> 
> - 분산 버전 관리 프로그램
> 
> - 코드의 히스토리(버전)을 관리하는 도구
> 
> - 개발되어온 과정 파악 가능
> 
> - 이전 버전과의 변경 사항 비교 및 분석

**버전** : 컴퓨터 소프트웨어의 특정 상태

**관리** : 어떤 일의 사무, 시설이나 물건의 유지 및 개량

**프로그램** : 컴퓨터에서 실행될 때 특정 작업을 수행하는 일련의 명령어들의 모음

### Git 기반의 서비스 GitHub, GitLab > 원격저장소

# Git 기본기

> ## repository

특정 디렉토리를 버전 관리하는 저장소

- `git init` 명령어로 로컬 저장소를 생성

- `.git` 디렉토리에 **버전 관리에 필요한 모든 것**이 들어있음

## README.md 생성하기

> 새 폴더를 만들고 README.md 파일을 생성
> 
> 이 파일을 버전 관리하며 Git을 사용
> 
>  특정 버전으로 남긴다 = "커밋(Commit)한다"

- Working Directory : 내가 작업하고 있는 실제 디렉토리

- Staging Area : 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

- Repository : 커밋들이 저장되는 곳

## Git log 남기기

> - 모든 파일을 수정 완료하면 Git bash 에서 해당 폴더로 접속
>   
>   1. cd desktop/startcamp
>   
>   2. git add "파일명"
>   
>   3. git commit -m "메시지"
>   
>   4. git status 작성해서 working tree clean 화면 확인하기
>   
>   5. git log 작성해서 로그 확인하기

## Git 명령어

> - `git init`
> 
> - `git add`
> 
> - `git commit -m "메시지"`
> 
> - `git log `
>   
>   - `git log --oneline`
>   
>   - `git log --oneline --graph`
> 
> - `git status`
> 
> - `mkdir`
> 
> - `touch`

## git commit을 실수 했을때

> - commit 을 쓸때는 -m을 붙혀서 메시지를 남겨야 하는데 실수로 그냥 commit 했을때
> 1. `insert`키 누르기
> 
> 2. 메시지 남기기
> 
> 3. `esc` 누르기
> 
> 4. `:wq` 눌러서 나가기
> 
> 5. modified
