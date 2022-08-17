import streamlit as st
import pandas as pd


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

st.markdown(
    f'<h1 style="color:#ffffff;font-size:30px;">{"👕사자동산의 Final Project👕"}</h1>', unsafe_allow_html=True)

# st.set_page_config(
#     page_title="PassionKing",
#     page_icon="👕",
# )

st.sidebar.success("Select a page above.")

st.markdown(
    """
    멋쟁이 사자처럼 AI School 6기 Final-Project **👖👖👖 PassionKing 👖👖👖**의 파이널 프로젝트 결과 홈페이지입니다.
    ## 1.  프로젝트 개요
    ### 1-1 주제: 👒이미지 분류 및 추천 시스템 활용 코디 추천 모델👒
    ### 1-2 주제 선정의 배경 및 이유
        - 이른 아침 눈을 뜨고 나갈 준비를 하면서 어떤 옷을 입지?🤔고민하시는 당신! 
        - 이런 당신을 위한 쉽고 간편한 코디 추천 모델을 추천해드립니다!
        - 오늘 입고 나갈 상의 사진을 찍어서 올리면 딱 맞는 코디를 추천해드립니다.
    ### 1-3. 목적
        - 패션 코디를 보고 옷을 잘 입고 싶으나 자신이 어떤 종류의 옷을 코디 할지 잘 모르는 유저들에게 고민의 시간을 줄여주고 자기 만족감을 올릴 수 있는 데에 목적을 가지고 있다.
    
    ## 2.   데이터셋
        - 무신사 의류 크롤링
        - AI Hub - 패션 상품 및 착용 이미지
        (https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=78)

    ## 3.    가설 설정(예상 결과물)
        - 유저들이 소지하고 있는 옷 사진을 찍어서 Input으로 넣으면 해당 옷이 반영된 코디 사진들을 보여준다. 나아가서 코디 사진에 등장한 잘 어울리는 의상을 구매할 수 있는 쇼핑몰 링크를 추천해준다.
"""
)
