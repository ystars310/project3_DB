import pandas as pd
from sqlalchemy import create_engine, text

song = pd.read_excel("./csv/or/20250616/single_album_date.xlsx")  # 노래 데이터
song = song.iloc[:,1:]          #첫 번째 열 (인덱스나 불필요한 열)제거  

song['genre_main'] = song['genre_main'].str.split('|')        # 장르 | << 분류 쪼개기
song = song.explode('genre_main').reset_index(drop=True)        # 여러 장르로 행 분리
song["genre_main"].value_counts()       # 장르별 개수 확인

# genre table 
genre_extract_df = song[["genre_main"]].drop_duplicates().reset_index(drop=True).reset_index()  # 중복제거 인덱스값 지정
genre_extract_df.columns = ["new_genre_id","genre_name"]                                       
song = song.merge(genre_extract_df, left_on="genre_main",right_on="genre_name", how="left")    
song[["genre_id"]] = song[["new_genre_id"]]                                                    
song = song.drop("new_genre_id",axis=1)                                                                                                           
genre_extract_df.columns = ["genre_id","genre_name"]                                           
# song table            # 데이터 삽입
song_extract_df = song[["song_id","song_name","lyric"]].copy()                               
song_extract_df.columns = ["song_id","song_name","song_lyrics"]                               
song_extract_df = song_extract_df.drop_duplicates().reset_index(drop=True)                   

# artist table          # 데이터 삽입
artist_extract_df = song[["artist_id","artist_name"]].copy()                                  
artist_extract_df = artist_extract_df.drop_duplicates().reset_index(drop=True)         

# album table           # 데이터 삽입
album_extract_df = song[["album_id","album_date"]].copy()                                 
album_extract_df.columns = ["album_id","album_years"]                                      
album_extract_df = album_extract_df.drop_duplicates().reset_index(drop=True)            

# music table           # 데이터 삽입 ( 관계테이블 )
music_extract_df = song[
    ["song_id","artist_id","album_id","genre_id"]                                             
    ].copy().drop_duplicates().reset_index(drop=True)

# karaoke table         # 데이터 삽입
location_df = pd.read_excel("./csv/or/20250616/karaoke_lat_long_set_float_type.xlsx")           # 노래방 데이터       
location_df = location_df.iloc[1:,:]                                                          
karaoke_df = location_df[["브랜드","지점명","주소","Latitude","Longitude"]].copy()               # 필요한 컬럼만 복사
karaoke_df = karaoke_df.drop_duplicates().reset_index(drop=True)                          
karaoke_df.columns = [f"karaoke_{i}" for i in ["name","store","location","lat","long"]]         # DB 컬럼 이름 확인및 변경
##
# insert                # DB 연결 설정 ( MySQL, root 계정, 비밀번호 ,포트 , DB명)
db_info = f"mysql+pymysql://root:root@localhost:3100/music_ai_2"
engine = create_engine(db_info, connect_args={})

# 장르를 기준으로 각 테이블에 데이터 삽입
# 장르
genre_extract_df.to_sql(
        "genre",                        # 테이블 이름   
        con=engine,                     # 연결된 DB엔진
        if_exists="append",             # 기존 테이블에 데이터 추가
        index=False              
        ) 

# 노래
song_extract_df.to_sql(
        "song",
        con=engine,
        if_exists="append",
        index=False
        ) 

# 가수
artist_extract_df.to_sql(
        "artist",
        con=engine,
        if_exists="append",
        index=False
        ) 

# 앨범
album_extract_df.to_sql(
        "album",
        con=engine,
        if_exists="append",
        index=False
        ) 

# 뮤직
music_extract_df.to_sql(
        "music",
        con=engine,
        if_exists="append",
        index=False
        )

# 가라오케
karaoke_df.to_sql(
        "karaoke",
        con=engine,
        if_exists="append",
        index=False
        )
