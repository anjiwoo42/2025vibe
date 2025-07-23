import streamlit as st
MOVIES =  {
        "웃고 싶어요 (코미디/로맨스)": [
        {"title": "극한직업 (한국, 2019)", "link": "https://www.netflix.com/title/81293933"},
        {"title": "정직한 후보 (한국, 2020)", "link": "https://www.tving.com/contents/P001548768"},
        {"title": "연애 빠진 로맨스 (한국, 2021)", "link": "https://www.wavve.com/player/movie?movieid=MV_K01_M2021A0009"},
        {"title": "너의 이름은. (일본, 재개봉)", "link": "https://watcha.com/contents/mdRdk5Y"}
    ],
    "힐링이 필요해요 (감동/드라마)": [
        {"title": "윤희에게 (한국, 2019)", "link": "https://watcha.com/contents/mW9p1o7"},
        {"title": "소울메이트 (한국, 2023)", "link": "https://www.netflix.com/kr/title/81788270"},
        {"title": "스즈메의 문단속 (일본, 2023)", "link": "https://www.netflix.com/title/81716838"},
        {"title": "너의 이름은. (일본, 재개봉)", "link": "https://watcha.com/contents/mdRdk5Y"}
    ],
    "답답한 기분 풀고 싶어요 (액션/사이다)": [
        {"title": "범죄도시 4 (한국, 2024)", "link": "https://www.tving.com/contents/P001774126"},
        {"title": "헌트 (한국, 2022)", "link": "https://watcha.com/contents/m5b9xZk"},
        {"title": "극장판 주술회전 0 (일본, 2022)", "link": "https://www.netflix.com/title/81715869"},
        {"title": "명탐정 코난: 흑철의 어영 (일본, 2023)", "link": "https://watcha.com/contents/mW93m9P"}
    ],
        
     "마음이 공허해요 (감성/인생)": [
        {"title": "남매의 여름밤 (한국, 2020)", "link": "https://www.wavve.com/player/movie?movieid=MV_K01_M2020A0003"},
        {"title": "밤의 문이 열린다 (한국, 2021)", "link": "https://www.filmmarket.or.kr/movie/detail.asp?movie_seq=21022"},
        {"title": "너와 파도를 탈 수 있다면 (일본, 2020)", "link": "https://watcha.com/contents/mOkb1Rd"},
        {"title": "수에비움: 나와 그녀와 그녀의 세계 (일본, 2023)", "link": "https://www.wavve.com/player/movie?movieid=MV_K02_M2023A0117"}
    ],
    "상영중 한국 영화 (극장)": [
        {"title": "야당 (한국, 2025)", 
         "link": "https://www.cgv.co.kr/movies/detail-view/?midx=10000000"},  
        {"title": "악마가 이사왔다 (한국, 2025)", 
         "link": "https://www.cgv.co.kr/movies/detail-view/?midx=10000001"}
]
}
st.set_page_config(page_title="🎥 한국·일본 영화 추천", layout="centered")
st.title("🎬 기분 따라 고르는 한국 + 애니메이션 영화")

st.markdown("극장에서 개봉한 **한국 실사 영화**와 **일본 애니메이션**만 모아 기분 따라 추천해드려요!")

mood = st.selectbox("💭 지금 내 기분은?", list(MOVIES.keys()))

if st.button("🎥 영화 추천받기"):
    st.subheader(f"🎯 '{mood}' 추천 영화")
    for movie in MOVIES[mood]:
        st.markdown(f"- [{movie['title']}]({movie['link']})")

st.markdown("---")
st.caption("📌 OTT 링크는 변동될 수 있어요. 넷플릭스, 왓챠, 웨이브, 티빙 위주로 링크를 제공했습니다.")
