# 💡 프로젝트 소개 
## 주요 기능
![Badge](https://img.shields.io/badge/python.svg?style=flat-round)
+ AI기반 음악을 추천해주는 기능으로써  장르,노래,가수,가사내용을 입력하면 관련 음악과 정보를 제공해줌                                    
+ 정보제공과 함께 youtube API를 활용한 링크추천, 좀더 자세한 정보를 위한 음악사이트링크도 함께 제공해줌                                     
+ 사용자 편의성을 위해 노래연습장의 위치정보도 함께 제공해줌 

## DB
+ 로그인과 유저정보는 별개로 나누어 보안에 대한 취약점을 보완
+ 음악정보는 정규화를 통해 찾으려는 정보를 한번에 불러오고 중복을 최소화 하기에 중점을 두었음

## data
+ 음악 데이터는 주식회사 카카오 AI추천플랫폼Team에서 제공해준 음악dataset파일을 이용하여 데이터를 삽입 하였으며,                        
  추가로 필요한 데이터는 음악사이트를 통해 수집하였습니다.
+ 노래연습장 데이터는 몇개의 브랜드를 추려 필요한 데이터를 수집하였습니다.
  - 링코, 락휴, 세븐스타, 엔젤스코인등 웹사이트를 이용

### python package 
```
conda env create -f environment.yml
pip install -r requirements.txt
```

## 개발환경
  - Python 3.8.0
  - docker desktop
  - MySQL Workbench
  - Google Sheets

 ## License
 **코드 사용시 연락 주시고 사용해주시면 감사하겠습니다**
