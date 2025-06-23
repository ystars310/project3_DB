# schema 구조


### RDBM (관계형 데이터베이스 방식)

+ 본래의 데이터에서 genre의 분류가 복잡하게 되어있고 종류가 많아서 genre를 고려하여 정규화작업을 진행
+ music table이 관계 테이블 역할
+ login은 회원아이디와 비밀번호만으로 로그인을 할수 있고 이외 정보는 user table로 테이블 분산
+ 편의성을 위해 노래연습장의 위치 정보를 알아볼수 있는 테이블을 별도로 생성

#





# ERD
<img 
src="https://github.com/user-attachments/assets/1e19ec62-7b22-4840-b81b-dd6320400315"
width="700px"
height="400px"
title="px 100"
alt="ERD"></img><br/>



## data_in.py

+ 1차로 데이터에 중복 제거, 결측치(NaN)제거
+ 2차 데이터 확인후 특수문자 제거
+ 중복 데이터중 데이터 확인을 거쳐 필요데이터는 추가적으로 정제된데이터와 병합
+ 마지막으로 데이터 삽입시 중복제거를 다시한번 하는 방법으로 데이터 삽입
