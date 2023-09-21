# git 총정리

- - - — - - - - - - - - - - - - - #내가 만든걸 올릴 떄

깃허브에서 레퍼지토리를 만들고
Git init
Git remote add origin 주소
//Git fetch origin
//Git merge origin/main (git pull origin main으로 한 번에 가능)
Git add .
Git commit -m “message”
Git push origin main
—
이후 추가했을 때
Git add .
Git commit -m “message”
Git push origin main

- - - — - - - - - - - - - - - - - #남이 만든걸 가져와서 시작할 떄
      Git clone 주소
      //cd 폴더명
      —
      이후 추가했을 때
      Git add .
      Git commit -m “message”
      Git push origin main

# clone 된 상태

Git pull origin main
—
이후 추가했을 때
Git add .
Git commit -m “message”
Git push origin main

- - - — - - - - - - - - - - - - -
      Main, New branch가 있을 때
      New 를 main으로 합칠려면
      Main branch에서 git merge new 를 하면 된다.

- - - — - - - - - - - - - - - - -
