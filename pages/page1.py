import streamlit as st
from PIL import Image, ImageOps

image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
if image_file is not None:
    # st.image(plt.imread(image_file))
    image = Image.open(image_file)
    st.image(image, caption='clothes')
