
#  🎧사용자 감정 기반 음악 추천 서비스

본 프로젝트는 **사용자의 감정을 고려**하여 노래를 추천해주는 서비스입니다.                                           
사용자가 입력한 채팅 정보를 직접 수집한 2만 여건의 노래의 가사를 기반으로 생성한 벡터 스토어를 통해 분석하여 적합한 노래를 추천합니다.

![Badge](https://img.shields.io/badge/python-3.8-1177AA.svg?style=flat-round)
[![MySQL](https://img.shields.io/badge/MySQL-1572B6?logo=mysql&logoColor=fff)](#)
[![Docker](https://img.shields.io/badge/Docker-1572B6?logo=docker&logoColor=fff)](#)
[![GoogleSheets](https://img.shields.io/badge/GoogleSheets-339933?logo=GoogleSheets&logoColor=fff)](#)


![시연](./DB/프로젝트시현영상.gif)

## 💡 개발 배경 및 목적
  
음악은 사람들의 감정을 표현하고 위로하는 중요한 수단입니다.      
하지만 내 감정 상태나 기분을 반영해 노래를 추천 하는 AI 서비스는 없었기에,          
지친 현대인을 위로할 수 있는 맞춤형 노래 추천 서비스를 개발하고자 시작하게 되었습니다.                       
사용자의 감정에 맞춘 맞춤형 음악 추천을 통해 개인화된 스트리밍 서비스를 제공합니다.

## ⚙️ 서비스 핵심 기능

**[주요기능]**

+ 사용자의 감정을 입력하면 그 감정에 맞는 노래를 추천
+ 사용자가 좋아하는 아티스트나 음악을 입력하면 해당 정보를 고려하여 맞춤 추천

**[부가 기능]**

+ 추천 노래에 대한 YouTube 영상 스트리밍 지원
+ 멜론 링크를 통한 앨범 수록 정보 등 추가 정보 제공
+ 노래연습장 위치 정보 제공으로 사용자 편의성 증대

## 📆 개발 과정
+ 개발 기간은 5월 26일부터 6월 27일까지 진행
+ 요구사항 정의서 및 요구사항 명세서 작성 후 개발 수행
+ 개발 과정은 애자일 방법론과 프로토타입 모델을 적용하였으며, 오전/오후 스크럼 회의를 통해 납기일을 준수하였음

# 🛠 데이터 수집 및 데이터 베이스 구현

자료는 노래 정보, 노래방 정보를 수집하였으며, 노래 자료는 2020년 카카오 아레나 대회 당시 참가자에게 제공되었던 70만건의 데이터셋을                                
제공받아 2만 7천 건을 활용하여 진행하였으며, 추가적으로 필요한 데이터는 크롤링을 활용하여 수집 하였음                       

<details>
<summary>🎵 데이터 수집 자세히 보기</summary>        
  
 - (주) 카카오 AI추천 플렛폼에서 제공 받은 dataset을 활용                            
  
  **[노래 정보 자료]**

+ 가사 정보 미제공으로 melon 사이트에서 가사 자료 수집
+ 정재 과정을 통해 최종적으로 **2만 건**의 자료 추출

   **[노래방 위치 정보 자료]**


+ 노래방 위치 정보를 제공하기 위해 5개 사이트에서 주소 정보 수집( 600건의 정보를 수집 )
+ 정재 과정을 통해 최종적으로 **570건**의 자료 추출

+ 수집된 주소 정보를 위/경도로 변환(Geocode Awesome Table 활용)


Requests, Selenium, Beautifulsoup 패키지 활용(scripts/crawling/karaoke_locations.py 참고)


+ [락휴](https://www.rockq.co.kr/franchise/list?area=&area2=&area2&text=&page=1), [큐코인](http://qcbang.co.kr/store/store_info.php),
  [세븐스타](https://www.7starcoin.co.kr), [엔젤스코인](https://www.angelscoin.co.kr/child/sub/spot/?ptype=&page=1&code=spot), [링코](https://rinkotown.co.kr/sub/store.html)
    
</details>

## 💾 데이터 정제 및 테이블 설계

+ 데이터 중복 및 결측치 제거
+ 데이터 특수 문자 제거
+ 데이터베이스 정규화(BCNF)를 진행
+ 보안을 고려하여 유저 정보는 별도의 테이블로 분리

![ERD](https://github.com/user-attachments/assets/1f401fef-1461-4b28-ab76-d651327c04b0)

 
## installation

데이터 베이스는 docker 를 통해 구동 가능하며, 데이터 수집 정재는 아래 python 패키지 설치 후 구동 가능합니다.

## 📦 DataBase 구동

``` bash
git clone https:/https://github.com/ystars310/project3_DB
cd db
```

``` bash
# .env 생성 -> 비밀번호 설정
docker-compose up -d

# develop 사용자 생성
CREATE USER 'develop'@'%' IDENTIFIED BY 'your_secure_password';
GRANT SELECT ON music.* TO 'develop'@'%';
FLUSH PRIVILEGES;
# 유저 목록 조회
SELECT User, Host FROM mysql.user;
```

## 📦 Python package

```bash
conda env create -f environment.yml
pip install -r requirements.txt
```
## ©️License
본 프로젝트의 코드는 비상업적 용도로 자유롭게 사용하실 수 있습니다.
상업적 이용이나 수정, 재배포 시에는 사전 연락을 부탁드립니다.

문의는 이메일(example@example.com)로 해주시기 바랍니다.

## 📖 Reference

데이터 출처 : (주) 카카오 AI추천플랫폼Team

## 👨‍💻👩‍💻 Collaborator

개발담당 : 장선호(Frontend 담당), 김유현(Backend 담당)
비개발담당 : 장연철, 윤준서
