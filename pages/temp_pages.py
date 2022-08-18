import h5py
import streamlit as st
from PIL import Image
import cv2

hdf = h5py.File("model_dataset0818.h5", 'r')
array = hdf['1008_1008_720_B_B017_B017_000.jpg'][:]
img = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
array2 = cv2.resize(img, (0, 0), fx=1.2, fy=1.2,
                    interpolation=cv2.INTER_LANCZOS4)
img = Image.fromarray(array2)


st.image(img, caption='model')


# def header(url):
#     st.markdown(
#         f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)


# header('notice')
# st.markdown(
#     f'<h1 style="color:#33ff33;font-size:24px;">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)
