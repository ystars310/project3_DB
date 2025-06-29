import os, json, ijson
import pandas as pd

"""
제공받은 json 파일을 읽어와 excel 파일 형태로 변환하는 코드
"""

output_folder = './export'
input_json_path = './source/meta.json'
output_excel_path = os.path.join(output_folder, 'meta.xlsx')

os.makedirs(output_folder, exist_ok=True)  

rows = []
with open(input_json_path, 'r', encoding='utf-8') as f_json:
    parser = ijson.items(f_json, 'item')
   
    for song in parser:
        row = {
            '_id': song.get('_id', ''),
            'album_id': song.get('album_id', ''),
            'artist_id': ', '.join(str(item) for item in song.get('artist_id', [])),
            'artist_name': ', '.join(str(item) for item in song.get('artist_name', [])),
            'song_name': song.get('song_name', ''),
            'song_gn_gnr': ', '.join(str(item) for item in song.get('song_gn_gnr', [])),
            'song_gn_dtl_gnr': ', '.join(str(item) for item in song.get('song_gn_dtl_gnr', [])),
            'issue_date': song.get('issue_date', '')
        }
        rows.append(row)
df = pd.DataFrame(rows)
df.to_excel(output_excel_path, index=False)

print(f"변환 완료! excel 파일 위치: {output_excel_path}")
