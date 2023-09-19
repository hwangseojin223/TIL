# Git

> 코드 관리 도구(Source Code Management Tool, SCM)

- 코드 관리도구
- 코드 협업도구
- 코드 배포도구

## 1. 코드 관리 도구로서의 Git

- 버전 관리 도구(Version Control System, VCS): 버전을 통해 코드를 관리하는 도구
- 분산형 버전 관리 도구(Distributed VCS): 분산된 형태로 버전을 통해 코드를 관리하는 도구

## 2. Git Commands

> Git은 폴더/디렉토리 단위로 프로젝트/저장소/코드를 관리한다.

### 2.1 git init

> Git 프로젝트 시작

```
$git init
Initialized empty Git repository in /Users/hwangseojin/intro/.git/
-> 비워있는 Git 저장소/프로젝트를 시작함(.git)
-> ls -a로 확인 가능
```

1. `.git` 폴더 생성
2. `(master)` 또는 `(main)` 프롬프트 (브랜치 이름) (Mac 표시 x)

### 2.2 Git 프로젝트 관리를 중단 : '.git' 폴더 삭제

- `rm -r .git`

### 2.3 git status

> Git 상태 출력

#### (1) 최초상태(Git init 직후)

```
On branch main -> main이라는 branch에 있음

No commits yet -> commit 아직 없음

nothing to commit (create/copy files and use "git add" to track) -> commit 할 것도 없음 (추적하려면 파일을 만들고 git add를 사용해)
```

#### (2) 파일 추가 직후

```
On branch main -> 위와 동일

No commits yet -> 위와 동일

Untracked files: -> 추적되지 않은 파일이 있음
  (use "git add <file>..." to include in what will be committed)
	a.txt
    -> a.txt 파일이 있는데, commit될 것에 포함시키려면 git add [파일명]을 사용해
nothing added to commit but untracked files present (use "git add" to track)
-> commit 할 것이 없어 그런데 추적되지 않은 파일들은 있어(git add 사용해라)
```

#### (3) 'git add' 직후

```
On branch main -> 위와 동일

No commits yet -> 위와 동일

Changes to be committed: -> commit할 변화가 있음
  (use "git rm --cached <file>..." to unstage)
	new file:   a.txt
    -> unstage 하고 싶으면 git rm... 써 (add 하기 직전으로 )
```

#### (4) 'git commit' 직후

```
On branch main
nothing to commit, working tree clean
```

### 2.4 git add [파일/폴더]

> commit을 위한 stage

- `git add .` : 현재 폴더의 모든 변경 사항 stage

- `git rm --cached [파일/폴더]` : unstage

### 2.5 git commit -m "커밋 메시지"

> Message와 함께 버저닝(Versioning) == 커밋(Commit)

#### (1) 처음으로 commit할 경우

```
Author identity unknown -> Error

git config --global user.email "user@gmail.com"
git config --global user.name "username"
-> 실행해야함
```

### 2.6 git log

> 현재까지의 commit을 출력

```
Author: Seojin Hwang <hsj6421@naver.com>
Date:   Tue Sep 19 15:47:15 2023 +0900

    Add c.txt

commit 9ed7229336dfbdf5d91ec150aed38fcc0c3f9ddf
Author: Seojin Hwang <hsj6421@naver.com>
Date:   Tue Sep 19 15:41:52 2023 +0900

    Add b.txt

commit 99d02ce3106a4689c673a1beb504fde9014c1390
Author: Seojin Hwang <hsj6421@naver.com>
Date:   Tue Sep 19 15:36:23 2023 +0900

    First commit
```

- `git log --oneline` : 한줄로 출력

  ```
  39f7d95 (HEAD -> main) Add c.txt
  9ed7229 Add b.txt
  99d02ce First commit
  ```

### 2.7 git remote

#### git remote add [저장소이름] [저장소주소]

> git에게 원격저장소(remote) 추가(add)를 명령
