def pre_processing(soup, lyric_div):
    for comment in lyric_div.find_all(
        string=lambda text: isinstance(text, type(soup.Comment))):
        comment.extract()

    # <br> 태그를 줄바꿈으로 변환
    for br in lyric_div.find_all("br"):
        br.replace_with("\n")

    # 전체 텍스트 추출 및 앞뒤 공백 제거
    lyrics = lyric_div.get_text(separator="\n").strip()

    # 여러 줄바꿈을 하나로 정리 (선택사항)
    lyrics = re.sub(r'\n+', '\n', lyrics)
    return lyric_div
