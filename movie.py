import streamlit as st

# 최근 5년 내 한국/해외 영화 추천 리스트
MOVIES = {
    "힐링이 필요해요 (감동/드라마)": [
        {"title": "마당을 나온 암탉 (한국, 2021 재개봉)", "imdb": "https://movie.daum.net/moviedb/main?movieId=60296"},
        {"title": "윤희에게 (한국, 2019)", "imdb": "https://movie.daum.net/moviedb/main?movieId=129960"},
        {"title": "CODA (미국, 2021)", "imdb": "https://www.imdb.com/title/tt10366460/"},
        {"title": "더 웨일 (미국, 2022)", "imdb": "https://www.imdb.com/title/tt13833688/"}
    ],
    "웃고 싶어요 (코미디/로맨스)": [
        {"title": "극한직업 (한국, 2019)", "imdb": "https://movie.daum.net/moviedb/main?movieId=121236"},
        {"title": "정직한 후보 (한국, 2020)", "imdb": "https://movie.daum.net/moviedb/main?movieId=134179"},
        {"title": "바비 (미국, 2023)", "imdb": "https://www.imdb.com/title/tt1517268/"},
        {"title": "로스트 시티 (미국, 2022)", "imdb": "https://www.imdb.com/title/tt13320622/"}
    ],
    "답답한 기분 풀고 싶어요 (액션/사이다)": [
        {"title": "범죄도시 4 (한국, 2024)", "imdb": "https://movie.daum.net/moviedb/main?movieId=167471"},
        {"title": "헌트 (한국, 2022)", "imdb": "https://movie.daum.net/moviedb/main?movieId=148741"},
        {"title": "존 윅 4 (미국, 2023)", "imdb": "https://www.imdb.com/title/tt10366206/"},
        {"title": "불렛 트레인 (미국, 2022)", "imdb": "https://www.imdb.com/title/tt12593682/"}
    ],
    "마음이 공허해요 (감성/인생)": [
        {"title": "밤의 문이 열린다 (한국, 2021)", "imdb": "https://movie.daum.net/moviedb/main?movieId=149095"},
        {"title": "소울메이트 (한국, 2023)", "imdb": "https://movie.daum.net/moviedb/main?movieId=153098"},
        {"title": "에브리씽 에브리웨어 올 앳 원스 (미국, 2022)", "imdb": "https://www.imdb.com/title/tt6710474/"},
        {"title": "애프터썬 (영국, 2022)", "imdb": "https://www.imdb.com/title/tt19770238/"}
    ]
}

st.set_page_config(page_title="기분 따라 영화 추천", layout="centered")
st.title("🎬 기분 따라 최신 한국+해외 영화 추천")

st.markdown("지금 내 기분에 딱 맞는 한국 영화와 해외 영화 추천을 받아보세요!")

mood = st.selectbox("💭 지금 내 기분은?", list(MOVIES.keys()))

if st.button("🎥 영화 추천받기"):
    st.subheader(f"🎯 '{mood}' 추천 영화")
    for movie in MOVIES[mood]:
        st.markdown(f"- **{movie['title']}** — [보러가기]({movie['imdb']})")

st.markdown("---")
st.caption("🔄 더 많은 영화가 필요하거나 테마를 추가하고 싶다면 언제든지 말해주세요!")
