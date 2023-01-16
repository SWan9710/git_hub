# Github 설정

git remote add `origin` https://github.com/SWan9710/TIL.git

- 여기서 origin은 인터넷 주소의 별칭

- remote add > 원격 인터넷 주소를 origin으로 부르겠다는 소리

## remote

- 원격 주소 설정에 관한 커맨드 라고 생각하면 될듯
- `add` `닉네임` `도메인` 으로 작성하면 닉네임에 도메인이 들어감
- `rm` `닉네임` 쓰면 닉네임에 들어가 도메인이 제거됨

## push

- 작업한 작업물을 깃허브에 업로드 할때 사용

- git push origin master
  
  > origin주소에 master가 작업한 결과를 업로드 

## Clone

- 작업한 파일을 다른곳에서 최초로 받을 때 사용

- `git clone 깃허브주소`

## pull

- 작업한 파일의 최초가 받아진 상태에서 수정사항을 받을 때 사용

- `git pull origin master`

## Token

- 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

- 내 개인 토큰

## Commit

- 파일을 업로드 하며 수정사항 확인이 쉬움

- 추가로 코드에 코멘트 작성 가능

## git add .

- 현재 작업한 폴더에 있는 모든 변경사항을 working area에 업로드
