




# music_ai_data

## data_extractor.py
+ 2020년 카카오 아레나 대회 당시 참가자에게 제공되었던 dataset을 excel file로 변환하기
  

<details>
<summary>별도로 추가 데이터 수집</summary>     

                               
requests를 요청한 Buautifulsoup을 이용한 방식으로 데이터 수집
+ **2025.06.05(목) ~ 2025.06.16(월)까지 진행**                                                                              
```dataset파일출처 주식회사 카카오 AI추천플랫폼Team```

+ 2020년 카카오 아레나 대회 당시 참가자에게 제공되었던 데이터셋을 제공받아 진행을 하였으며, 제공받은 데이터셋 이외에
 필요 데이터는 별도로 데이터 수집을 진행하게 되었으며 melon사이트와 bugsmusic을 이용하였습니다.                    
  멜론 링크: [[melon](https://www.melon.com/)] 벅스 링크: [[bugs](https://music.bugs.co.kr/)]

  - 1차적으로 데이터셋의 데이터가 70만개가 되었으며 별도로 수집할 데이터를 골라내는 작업을 먼저 진행한 후에 선별한 데이터에서
   추가적으로 필요한 데이터를 수집하는 방법으로 진행하였습니다.

  - 선별한 데이터는 2017년부터 2020년까지의 데이터만 선별하였으며 총 187,000곡의 데이터를 대상으로 데이터 수집을 진행 하였으며
    최종적으로 수집한 데이터는 **27,500**개의 데이터를 수집하였습니다.

  - 187,000곡의 데이터중 필요데이터가 없는 데이터, 또는 자체적으로 없는 데이터가 다수 포함되어있었으며,
    수집 전 예상 계획 데이터는 2만개를 목표로 하였습니다.( 시간적인 이유때문에 ) 
</details>

<details>
<summary>노래연습장 데이터 수집</summary>     
  
**2025.06.17(화) ~ 2025.06.18(수)까지 진행**                       
```
락휴 노래연습장, 큐 코인 노래연습장, 세븐스타 코인노래연습장, 엔젤스코인 노래연습장, 링코 노래타운등의 웹사이트를 이용한 데이터 수집
```
  - 구글 스프레드시트를 이용하여 좌표변환을 진행 ( **Geocode Awesome Table 활용** )

</details>

___
### 데이터 정제 
+ 1차로 데이터에 중복 제거, 결측치(NaN)제거
+ 2차 데이터 확인후 특수문자 제거
+ 중복 데이터중 데이터 확인을 거쳐 필요데이터는 추가적으로 정제된 데이터와 병합

## insert_data.py

+ 마지막으로 데이터 삽입시 중복제거를 다시한번 하는 방법으로 데이터 삽입
