import streamlit as st
import pandas as pd

# st.set_page_config(layout="wide")

st.title('👗 My Style Manager')

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://images.unsplash.com/photo-1551232864-3f0890e580d9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3R5bGV8ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60");
             background-size: cover;
             opacity: 0.8
         }}
         .stApp:hover {{
             opacity: 1.0
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# set_bg_hack_url()

# st.sidebar.success("Select a page above.") 페이지 골라주세요 부분

st.markdown(
    """
    Welcome! This page is Likelion Final-Project of passionking
    """
)

st.subheader("Nice to meet You XD")



selected_item = st.radio("여러분이 가진 고민은 무엇인가요?", (
    "패션에 관심은 많은데 스타일링이 어려워요",
    "바쁜 아침에 고민하지 않고 빨리 준비하고 싶어요", 
    "집에 사놓고 어떻게 입어야 할 지 모르겠는 옷들이 많아요"
    )
    )
	
if selected_item == "패션에 관심은 많은데 스타일링이 어려워요":
    st.write("**마스매가 예쁜 코디 사진 추천으로 도와줄게요!**")
elif selected_item == "바쁜 아침에 고민하지 않고 빨리 준비하고 싶어요":
    st.write("**마스매와 함께라면 빠른 출근 준비 완료!**")
elif selected_item == "집에 사놓고 어떻게 입어야 할 지 모르겠는 옷들이 많아요":
    st.write("**마스매로 옷장 속 장롱템의 재발견까지!**")

st.markdown(
"""
### What is My Style Manager?
    마이스타일매니저에서는 직접 촬영한 상품 이미지(상의, 하의, 신발, 모자 등)를 올리면    
    해당 상품에 어울리는 코디를 자동으로 추천해줍니다. 매일 아침 등교, 출근 준비 시간에      
    마스매를 통해 고민없는 빠르고 예쁜 스타일링 추천을 경험해보세요!
"""
)


st.subheader("How To Use?")


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        #### Step1
        """
    )
    st.image("step1.png")

with col2:
    st.markdown(
        """
        #### Step2
        """
    )
    st.image("Step2.png")

with col3:
    st.markdown(
        """
        #### Step3
        """
    )
    st.image("Step3.png")

