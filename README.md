# 프로젝트 계획

11.17 (수) 1일차 진행상황:

- 프로젝트 기획 및 페이지 초안 작성
- ERD 작성
- back, front 프로젝트 및 앱 생성
- 필요한 기초작업 진행중



11.18 (목) 2일차 진행 상황:

- 영화 데이터를 django db에 저장
- Home에 각 영화 정보를 bootstrap card component를 이용해 보여주는 기능 구현
- 로그인기능 구현 및 커뮤니티 게시판 작성 기능 구현(진행 중)



11.19(금) 3일차 계획:

- 로그아웃 기능 구현, 로그인 여부에 따른 토글 기능 추가
- 커뮤니티 CRUD 마무리







### 충돌없이 PUSH 하는 방법!!!!

------------------------------------------

1. ```bash
   git add .
   ```

2. ```bash
   git stash
   ```

   => git서버에 올라온것으로 최신화하기 위하여 작업한 자료를 임시 보관함에 보낸다!!

3. ```bash
   git status
   ```

   => stage, unstage가 된게 있나 확인!!

4. ```bash
   git pull origin master
   ```

   => 작업한 저장소를 최신화 시킴!!

5. ```bash
   git stash pop
   ```

    => 임시 보관함에 넣은 내 작업물을 가져옴!!

6. ```bash
   git add .
   ```

7. ```bash
   git commit -m ' '
   ```

8. ```bash
   git push origin master
   ```

   => 최신화 됐기 때문에 충돌안나고 PUSH 가능!

   

진짜 가끔 commit까지 해서 push 하려는데 그전에 다른사람이 push를 해서 에러가 뜨는경우!!

1. ```bash
   git reset --soft HEAD^
   ```

   => commit 한 상태를 add . 한 상태로 되돌림!! (stash는 commit한 상태에서 사용이 안되기 때문!!)

2. ```bash
   git stash
   ```

   => 위의 2번 과정부터 다시 시작!!