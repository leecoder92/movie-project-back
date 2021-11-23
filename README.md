# Final Project

## 구성원 및 역할

- 이종준(팀장): 커뮤니티 기능 구현
- 이승규: 회원인증 기능 구현
- 공통: 영화추천 기능 구현, UI/UX 향상





## 프로젝트 목표

- 넷플릭스를 오마주하여 UI/UX를 비슷하게 구성
- 요구사항에 충실하게, 필요한 기능만 간단명료하게 구현





## 영화 추천방식

- 영화 자체 평점과 회원들이 직접 작성한 평점을 비교, 회원이 직접 작성한 평점이 더 높으면 추천

- 로그인한 사람이 평점을 4점 이상으로 남긴 영화들의 장르를 모아서 비슷한 장르의 영화를 평점순으로 추천





## 프로젝트 계획

11.17 (수) 1일차 진행 상황:

- 프로젝트 기획 및 페이지 초안 작성
- ERD 작성
- back, front 프로젝트 및 앱 생성
- 필요한 기초작업 수행



11.18 (목) 2일차 진행 상황:

- 영화 데이터를 django db에 저장
- Home에 각 영화 정보를 bootstrap card component를 이용해 보여주는 기능 구현
- 로그인기능 구현 및 커뮤니티 게시판 작성 기능 구현



11.19(금) 3일차 진행 상황:

- 로그아웃 기능 구현, 로그인 여부에 따른 토글 기능 추가 완료 => 회원인증 기능 구현 완료
- 커뮤니티 CRUD 기능 구현 완료



11.22(월) 4일차 진행 상황:

- 커뮤니티 댓글 기능 구현 - 완료
- 영화 세부정보 페이지 기능 구현 - 완료



11.23(화) 5일차 진행 상황:

- 영화추천 기능 구현 - 완료
- 서비스 디자인 완성도 높이기



11.24(수) 6일차 계획:

- UI/UX 향상
- 프로젝트 마무리



11.25(목) 7일차 계획:

- 프로젝트 발표 준비
- 지속적인 피드백 및 프로젝트 완성도 높이기





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