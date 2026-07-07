import base64
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

# 국기 이미지는 iframe에 문자열로 주입되므로 상대경로 대신 base64 데이터 URI로 치환
ASSETS_DIR = pathlib.Path(__file__).parent / "assets"


def _to_data_uri(filename: str, mime: str) -> str:
    data = (ASSETS_DIR / filename).read_bytes()
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


html_content = html_content.replace("__FLAG_KR_DATA_URI__", _to_data_uri("flag-kr.png", "image/png"))
html_content = html_content.replace("__FLAG_CN_DATA_URI__", _to_data_uri("flag-cn.jpg", "image/jpeg"))

# 내용이 길고 동적으로 늘어날 수 있으므로 넉넉한 높이 + 내부 스크롤 허용
st.iframe(html_content, height=2400)
