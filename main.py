import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title('๐ My Style Manager')


def line_break():
    return st.markdown("<br/>", unsafe_allow_html=True)

# st.sidebar.success("Select a page above.") ํ์ด์ง ๊ณจ๋ผ์ฃผ์ธ์ ๋ถ๋ถ


st.markdown(
    """
    Welcome! This page is Likelion Final-Project of passionking
    """
)

st.subheader("Nice to meet You XD")


selected_item = st.radio("์ฌ๋ฌ๋ถ์ด ๊ฐ์ง ๊ณ ๋ฏผ์ ๋ฌด์์ธ๊ฐ์?", (
    "ํจ์์ ๊ด์ฌ์ ๋ง์๋ฐ ์คํ์ผ๋ง์ด ์ด๋ ค์์",
    "๋ฐ์ ์์นจ์ ๊ณ ๋ฏผํ์ง ์๊ณ  ๋นจ๋ฆฌ ์ค๋นํ๊ณ  ์ถ์ด์",
    "์ง์ ์ฌ๋๊ณ  ์ด๋ป๊ฒ ์์ด์ผ ํ  ์ง ๋ชจ๋ฅด๊ฒ ๋ ์ท๋ค์ด ๋ง์์"
)
)

if selected_item == "ํจ์์ ๊ด์ฌ์ ๋ง์๋ฐ ์คํ์ผ๋ง์ด ์ด๋ ค์์":
    st.write("**๋ง์ค๋งค๊ฐ ์์ ์ฝ๋ ์ฌ์ง ์ถ์ฒ์ผ๋ก ๋์์ค๊ฒ์!**")
elif selected_item == "๋ฐ์ ์์นจ์ ๊ณ ๋ฏผํ์ง ์๊ณ  ๋นจ๋ฆฌ ์ค๋นํ๊ณ  ์ถ์ด์":
    st.write("**๋ง์ค๋งค์ ํจ๊ป๋ผ๋ฉด ๋น ๋ฅธ ์ถ๊ทผ ์ค๋น ์๋ฃ!**")
elif selected_item == "์ง์ ์ฌ๋๊ณ  ์ด๋ป๊ฒ ์์ด์ผ ํ  ์ง ๋ชจ๋ฅด๊ฒ ๋ ์ท๋ค์ด ๋ง์์":
    st.write("**๋ง์ค๋งค๋ก ์ท์ฅ ์ ์ฅ๋กฑํ์ ์ฌ๋ฐ๊ฒฌ๊น์ง!**")

line_break()
line_break()
st.markdown(
    """
### What is My Style Manager?
    ๋ง์ด์คํ์ผ๋งค๋์ ์์๋ ์ง์  ์ดฌ์ํ ์ํ ์ด๋ฏธ์ง(์์, ํ์, ์ ๋ฐ, ๋ชจ์ ๋ฑ)๋ฅผ ์ฌ๋ฆฌ๋ฉด    
    ํด๋น ์ํ์ ์ด์ธ๋ฆฌ๋ ์ฝ๋๋ฅผ ์๋์ผ๋ก ์ถ์ฒํด์ค๋๋ค. ๋งค์ผ ์์นจ ๋ฑ๊ต, ์ถ๊ทผ ์ค๋น ์๊ฐ์      
    ๋ง์ค๋งค๋ฅผ ํตํด ๊ณ ๋ฏผ์๋ ๋น ๋ฅด๊ณ  ์์ ์คํ์ผ๋ง ์ถ์ฒ์ ๊ฒฝํํด๋ณด์ธ์!
"""
)

line_break()
line_break()
st.subheader("How To Use?")


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        #### Step1
        """
    )
    st.image("images/step1.jpg")

with col2:
    st.markdown(
        """
        #### Step2
        """
    )
    st.image("images/step2.jpg")

with col3:
    st.markdown(
        """
        #### Step3
        """
    )
    st.image("images/step3.jpg")
