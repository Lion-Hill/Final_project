import streamlit as st
import pandas as pd
from PIL import Image, ImageOps
from rembg import remove
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
import h5py


def write_heading(head_number, color, size, string):
    return st.markdown(f'<{head_number} style="color:{color};font-size:{size}px;">{string}</h1>', unsafe_allow_html=True)


def img_read(file):
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def image_preprocessing():
    threshold = 3

    non_back_img = remove(image)

    mask = cv2.cvtColor(np.array(non_back_img), cv2.COLOR_BGR2GRAY)
    mask = np.expand_dims(mask, axis=2)

    results = np.array(non_back_img) | 255 * (mask < threshold)
    results = np.array(results[:, :, :3], dtype='uint8')
    return results


def load_model():
    encoder = keras.models.load_model('model/Encoder_0818/')
    decoder = keras.models.load_model('model/Decoder_0818/')
    model = keras.models.load_model('model/ConvAE_0818/')

    return encoder, decoder, model


def AVGpooling(raw_feature):
    result = []
    for i in range(raw_feature.shape[0]):
        row = []
        for j in range(raw_feature.shape[-1]):
            row.append(raw_feature[i, :, :, j].mean())
        result.append(row)
    return np.array(result)


def img_crop(img):
    imgR = 128
    imgC = 128
    img = cv2.resize(img, (imgR, imgC), cv2.INTER_LINEAR)
    return img


def get_latent_feature():
    df = pd.read_csv('feature_csv/latent_feature_0818.csv')
    comp = df.drop('label', axis=1)
    label = df['label']
    comp = comp.astype('float32')
    return comp, label, df


def get_wearing_info():
    fashion_df = pd.read_csv('feature_csv/uni_wearing.csv')
    fashion_df.fillna(0, inplace=True)
    fashion_df.iloc[:, 1:] = fashion_df.iloc[:, 1:].astype(int)

    return fashion_df


def Fashion_coordination(top10_result, fashion_df):
    result_df = []
    for item in top10_result:
        ele_df = pd.DataFrame(columns=fashion_df.columns)
        for col in fashion_df.columns:
            ele = fashion_df[fashion_df[col] == item]
            ele_df = pd.concat([ele_df, ele])
        result_df.append(ele_df)
    return result_df


def recommend_fashion():
    input_image = image_preprocessing()
    encoder, decoder, model = load_model()

    input_image = img_crop(input_image)

    input_emb = encoder.predict(np.reshape(input_image, (1, 128, 128, 3)))
    input_comp = AVGpooling(input_emb)

    comp, label, df = get_latent_feature()

    # st.write(input_comp)
    # st.write(comp)

    sample_cosine_sim = cosine_similarity(input_comp, comp)
    # st.write(sample_cosine_sim)

    # sample_cosine_sim = 1/euclidean_distances(input_comp, comp)

    df_cosine = pd.DataFrame(
        sample_cosine_sim.T, index=df.index, columns=['sample'])
    top10_idx_cosine = df_cosine['sample'].nlargest(10).index
    top10_label_cosine = label[top10_idx_cosine].values
    # st.write(df_cosine['sample'].nlargest(10))

    fashion_df = get_wearing_info()
    top10_result_cosine = list(map(lambda x: int(x[:7]), top10_label_cosine))

    recomm_df = Fashion_coordination(top10_result_cosine, fashion_df)
    # st.write(recomm_df)
    recomm_total = pd.concat(recomm_df, axis=0)
    recomm_total.reset_index(drop=True)

    wearing_list = [recomm_total.iloc[i, 0] for i in range(9)]

    return wearing_list


write_heading('h1', '#000000', '42', '코디 추천 페이지')
write_heading('h6', '#000000', '25', '당신의 옷 사진을 넣어주세요')

image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])


if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption='your clothes')
    if st.button('Recommend your fashion'):
        wearing_list = recommend_fashion()

        hdf = h5py.File("model_dataset0818.h5", 'r')

        img_array_list = []
        for i in wearing_list:
            img_array = hdf[i][:]
            img_RGB = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
            img_array_list.append(img_RGB)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""#### 1st fashion""")
            img1 = Image.fromarray(img_array_list[0])
            st.image(img1, caption='1st fashion')

        with col2:
            st.markdown("""#### 2nd fashion""")
            img2 = Image.fromarray(img_array_list[1])
            st.image(img2, caption='2nd fashion')

        with col3:
            st.markdown("""#### 3rd fashion""")
            img3 = Image.fromarray(img_array_list[2])
            st.image(img3, caption='3rd fashion')

        col4, col5, col6 = st.columns(3)

        with col4:
            st.markdown("""#### 4th fashion""")
            img4 = Image.fromarray(img_array_list[3])
            st.image(img4, caption='4th fashion')

        with col5:
            st.markdown("""#### 5th fashion""")
            img5 = Image.fromarray(img_array_list[4])
            st.image(img5, caption='5th fashion')

        with col6:
            st.markdown("""#### 6th fashion""")
            img6 = Image.fromarray(img_array_list[5])
            st.image(img6, caption='6th fashion')

        col7, col8, col9 = st.columns(3)

        with col7:
            st.markdown("""#### 7th fashion""")
            img7 = Image.fromarray(img_array_list[6])
            st.image(img7, caption='7th fashion')

        with col8:
            st.markdown("""#### 8th fashion""")
            img8 = Image.fromarray(img_array_list[7])
            st.image(img8, caption='8th fashion')

        with col9:
            st.markdown("""#### 9th fashion""")
            img9 = Image.fromarray(img_array_list[8])
            st.image(img9, caption='9th fashion')
