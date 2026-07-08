import pathlib

import streamlit as st

# ---- 페이지 기본 설정 ----
st.set_page_config(
    page_title="RegulFit(레귤핏) | 화장품 처방전 국가별 규제 검토",
    page_icon="🧪",
    layout="wide",
)

# Streamlit 기본 여백/헤더를 최소화해서 원본 HTML 디자인이 그대로 보이도록 함
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        header[data-testid="stHeader"] {
            background: transparent;
        }
        iframe {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- RegulFit.html 로드 ----
HTML_PATH = pathlib.Path(__file__).parent / "RegulFit.html"
html_content = HTML_PATH.read_text(encoding="utf-8")

# height="content"로 두면 실제 렌더링된 HTML 높이에 맞춰 iframe이 자동으로 조정됨
st.iframe(html_content, height="content")
