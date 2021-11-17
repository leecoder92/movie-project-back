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