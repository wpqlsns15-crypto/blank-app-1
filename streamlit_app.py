import streamlit as st
import math

st.set_page_config(page_title="도형 둘레 계산기", page_icon="📐", layout="wide")

st.title("📐 도형 둘레 계산기")
st.write("초등학교 수학에서 배우는 다양한 도형의 둘레를 계산해보세요!")

# 도형 선택
shape = st.selectbox(
    "계산하고 싶은 도형을 선택하세요:",
    ["삼각형", "사각형(정사각형)", "사각형(직사각형)", "원형"]
)

st.divider()

# 삼각형
if shape == "삼각형":
    st.subheader("🔺 삼각형의 둘레")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        side_a = st.number_input("변 a의 길이 (cm):", min_value=0.0, value=3.0, step=0.1)
    with col2:
        side_b = st.number_input("변 b의 길이 (cm):", min_value=0.0, value=4.0, step=0.1)
    with col3:
        side_c = st.number_input("변 c의 길이 (cm):", min_value=0.0, value=5.0, step=0.1)
    
    perimeter = side_a + side_b + side_c
    
    st.success(f"**삼각형의 둘레 = {side_a} + {side_b} + {side_c} = {perimeter} cm**")
    st.info("💡 삼각형의 둘레 = 세 변의 길이의 합")

# 정사각형
elif shape == "사각형(정사각형)":
    st.subheader("⬜ 정사각형의 둘레")
    
    side = st.number_input("한 변의 길이 (cm):", min_value=0.0, value=4.0, step=0.1)
    
    perimeter = side * 4
    
    st.success(f"**정사각형의 둘레 = {side} × 4 = {perimeter} cm**")
    st.info("💡 정사각형의 둘레 = 한 변의 길이 × 4")

# 직사각형
elif shape == "사각형(직사각형)":
    st.subheader("▭ 직사각형의 둘레")
    
    col1, col2 = st.columns(2)
    with col1:
        length = st.number_input("가로 (cm):", min_value=0.0, value=6.0, step=0.1)
    with col2:
        width = st.number_input("세로 (cm):", min_value=0.0, value=4.0, step=0.1)
    
    perimeter = (length + width) * 2
    
    st.success(f"**직사각형의 둘레 = ({length} + {width}) × 2 = {perimeter} cm**")
    st.info("💡 직사각형의 둘레 = (가로 + 세로) × 2")

# 원형
elif shape == "원형":
    st.subheader("⭕ 원의 둘레")
    
    radius = st.number_input("반지름 (cm):", min_value=0.0, value=3.0, step=0.1)
    
    perimeter = 2 * math.pi * radius
    
    st.success(f"**원의 둘레 (원주) = 2 × π × {radius} ≈ {perimeter:.2f} cm**")
    st.info("💡 원의 둘레 = 2 × π × 반지름 (π ≈ 3.14)")

st.divider()

# 공식 설명
with st.expander("📚 도형별 둘레 공식"):
    st.markdown("""
    **삼각형**: 둘레 = a + b + c (세 변의 합)
    
    **정사각형**: 둘레 = a × 4 (한 변의 길이 × 4)
    
    **직사각형**: 둘레 = (a + b) × 2 (가로와 세로의 합 × 2)
    
    **원**: 둘레 = 2πr (반지름의 2배 × π)
    """)
