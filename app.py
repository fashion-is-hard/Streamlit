
import os
import streamlit as st
from PIL import Image
import numpy as np
import cv2
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
from PIL import Image
import random

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

'''with open('model_3.pickle', 'rb') as f:
    
    model_3 = pickle.load(f)'''

def main():

    st.title('저고리 유물 시대 예측 프로그램')
    st.write('2024-2 융합소프트웨어프로젝트 | 2045013 의류산업학과 김세희')
    st.info('왼쪽 메뉴에서 유물 이미지를 업로드 해주세요.', icon='📢')

    with st.sidebar:
        uploaded_img= st.file_uploader("유물 이미지를 업로드해주세요.", type=['jpg','jpeg','png'], accept_multiple_files=True)
        process = st.button("예측 실행")
    if process:
        if not uploaded_img:
            st.warning("이미지를 한 개 이상 업로드해주세요!")
        else:
            for img in uploaded_img:
                img=Image.open(img)
                img2=np.array(img)
                img2=cv2.resize(img2,(180,180))
                img_4d=img2.reshape((1, 180, 180, 3))
                prediction = random.arange(0,3)
                label=['조선시대', '일제강점기', '광복이후']
                st.subheader("추정 결과 [%s] 입니다." %label[prediction)
                st.image(img, width=500)


if __name__ == '__main__':
    main()
