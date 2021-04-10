# Django Project 



## 프로젝트 간략 소개

**MSA 클라우드 특강 첫번 째 개인 프로젝트**
모놀리틱한 django 웹사이트

**기간** : 21/01/19 ~21/01/28

**웹페이지의 주요 기능** : 해당 서비스는 3가지 카테고리 스포츠, 음식, 공부 를 통해 자신이 가입하고 싶은 모임을 가입해 오픈 카카오톡 방에서 사람들과 소통하거나 정보를 주고 받을 수 있습니다. 가입한 모임은 언제든지 탈퇴가 가능하고 여러 모임에 중복으로 가입할 수 있습니다.





## 환경

- python 3.9.1
- javascript
- django 3.0.5



## Directory Structure

```
\---JoinUs
    +---JoinUs
    +---joinus_app
    |   +---migrations
    |   +---templates
    |       \---joinus_app
    +---media
    |   \---images
    +---member_app
    |   +---migrations
    |   +---templates
    |      \---member_app
    |   
    +---noticeboard_app
    |   +---migrations
    |   +---templates
    |       \---noticeboard_app
    |   
    +---static
    |   +---css
    |   +---image
    |   +---js
    |   \---vendor
    |       +---bootstrap
    |       |   +---css
    |       |   \---js
    |       \---jquery
    \---templates
```

### 각 App 설명

Joinus_App

메인페이지와 회원이 가입한 모임 정보 및 가장 회원이 많은 모임을 보여주는 서비스 역할 

Member_App

회원의 정보를 관리하거나 회원 가입을 하는 서비스 역할

Noticeboard_App

게시판을 생성하거나 수정하는 서비스 역할



##  사용된 기술 



### crud

​	- 회원 관리 

​	- 게시판 생성 

### ajax

​	- 회원 가입 

​			회원 이메일, 닉네임 중복확인

​	- 게시판 

​			게시판 이름  중복확인

​	- 회원 정보 수정 페이지

​			회원 닉네임 수정 시 중복 확인

​			회원 탈퇴 시 비밀번호 확인

