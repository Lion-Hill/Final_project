import streamlit as st
from PIL import Image, ImageOps
from rembg import remove


def write_heading(head_number, color, size, string):
    return st.markdown(f'<{head_number} style="color:{color};font-size:{size}px;">{string}</h1>', unsafe_allow_html=True)

def recommend_fashion():
    non_back_img = remove(image)
    st.image(non_back_img)


write_heading('h1', '#000000', '42', '코디 추천 페이지')
write_heading('h6', '#000000', '25', '당신의 옷 사진을 넣어주세요')

image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])


if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption='your clothes')
    st.button('Recommend your fashion', on_click=recommend_fashion)

