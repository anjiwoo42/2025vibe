import streamlit as st

# 최신 영화 + 감상 플랫폼 링크 포함
MOVIES = {
    "힐링이 필요해요 (감동/드라마)": [
        {"title": "마당을 나온 암탉 (한국)", "link": "https://www.wavve.com/player/movie?movieid=MV_K01_M2022A0002"},
        {"title": "윤희에게 (한국)", "link": "https://watcha.com/contents/mW9p1o7"},
        {"title": "CODA (미국)", "link": "https://tv.apple.com/kr/movie/coda/umc.cmc.3yxfsy2y5v0xz5vjrp8zlqrp6"},
        {"title": "더 웨일 (미국)", "link": "https://www.coupangplay.com/movies/whale-2022"}
    ],
    "웃고 싶어요 (코미디/로맨스)": [
        {"title": "극한직업 (한국)", "link": "https://www.netflix.com/title/81293933"},
        {"title": "정직한 후보 (한국)", "link": "https://www.tving.com/contents/P001548768"},
        {"title": "바비 (미국)", "link": "https://www.coupangplay.com/movies/barbie"},
        {"title": "로스트 시티 (미국)", "link": "https://www.paramountplus.com/movies/the-lost-city/"}
    ],
    "답답한 기분 풀고 싶어요 (액션/사이다)": [
        {"title": "범죄도시 4 (한국)", "link": "https://www.tving.com/contents/P001774126"},
        {"title": "헌트 (한국)", "link": "https://watcha.com/contents/m5b9xZk"},
        {"title": "존 윅 4 (미국)", "link": "https://play.google.com/store/movies/details/존_윅_4?id=UwA-sCgvoNw.P"},
        {"title": "불렛 트레인 (미국)", "link": "https://watcha.com/contents/mW1ldA1"}
    ],
    "마음이 공허해요 (감성/인생)": [
        {"title": "밤의 문이 열린다 (한국)", "link": "https://www.filmmarket.or.kr/movie/detail.asp?movie_seq=21022"},
        {"title": "소울메이트 (한국)", "link": "https://www.netflix.com/kr/title/81788270"},
        {"title": "에브리씽 에브리웨어 올 앳 원스", "link": "https://watcha.com/contents/mOk5XQo"},
        {"title": "애프터썬 (영국)", "link": "https://www.wavve.com/player/movie?movieid=MV_K01_M2023A0114"}
    ]
}

st.set_page_config(page_title="기분 따라 최신 영화 추천", layout="centered")
st.title("🎬 기분 따라 한국 + 해외 영화 추천")

st.markdown("지금 내 기분에 딱 맞는 최신 영화와 감상 사이트 링크까지 한눈에 보기!")

mood = st.selectbox("💭 지금 내 기분은?", list(MOVIES.keys()))

if st.button("🎥 영화 추천받기"):
    st.subheader(f"🎯 '{mood}' 추천 영화")
    for movie in MOVIES[mood]:
        st.markdown(f"- [{movie['title']}]({movie['link']})")

st.markdown("---")
st.caption("💡 OTT 링크는 변동될 수 있어요. 원하는 플랫폼이 있으면 그에 맞춰 더 정리해드릴게요!")
