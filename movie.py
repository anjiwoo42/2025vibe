# app.py
import streamlit as st

# 샘플 영화 데이터
MOVIES = {
    "편안한 드라마": [
        {"title": "죽은 시인의 사회", "imdb": "https://www.imdb.com/title/tt0097165/"},
        {"title": "리틀 미스 선샤인", "imdb": "https://www.imdb.com/title/tt0449059/"}
    ],
    "희망을 주는 가족영화": [
        {"title": "인사이드 아웃", "imdb": "https://www.imdb.com/title/tt2096673/"},
        {"title": "코코", "imdb": "https://www.imdb.com/title/tt2380307/"}
    ],
    "스트레스 해소 액션": [
        {"title": "매드 맥스: 분노의 도로", "imdb": "https://www.imdb.com/title/tt1392190/"},
        {"title": "조커", "imdb": "https://www.imdb.com/title/tt7286456/"}
    ],
    "코미디/로맨스": [
        {"title": "500일의 썸머", "imdb": "https://www.imdb.com/title/tt1092026/"},
        {"title": "브루클린의 멋진 인생", "imdb": "https://www.imdb.com/title/tt2582846/"}
    ]
}

st.set_page_config(page_title="기분별 영화 추천 앱", layout="centered")
st.title("🌈 기분별 영화 추천")

st.write("마음이 답답하거나 화가 날 때, 기분에 따라 추천 영화를 골라보세요.")

genre = st.selectbox("지금 이런 기분이신가요?", list(MOVIES.keys()))

if st.button("추천 받기"):
    st.subheader(f"✅ '{genre}' 추천 영화 목록")
    movies = MOVIES.get(genre, [])
    for mv in movies:
        st.markdown(f"- **{mv['title']}** — [IMDb 링크]({mv['imdb']})")

st.write("---")
st.write("📌 추가하고 싶은 영화가 있다면 알려주세요! 의견을 반영해서 업데이트할게요.")
