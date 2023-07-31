import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tensorflow as tf
import numpy as np
import pandas as pd

# 타이틀 작업
st.title(':blue[Cats vs Dogs Classification]:cloud:')
new_model = load_model('c:/image/my_vgg_model.h5')
# 이미지 파일 로드
upload_file = st.file_uploader('Upload your file here ! :cat::dog:',type=['png','jpeg','jpg','csv','xlsx'])


if upload_file is not None:
    st.image(upload_file) # 화면에 이미지 출력. 단, 로드 시에만 출력되도록 조건 제어문. 파일이 존재할 경우에만 수행

     # button 누르는 것이 True 일 때 사진 누르면 분류해주는 로직.
     # 버튼이 클릭되면 아래 작업 수행해 
        
if st.button('분류'): # 분류라는 버튼 생성.
    img = load_img(upload_file)
    x = img_to_array(img)
    x = tf.image.resize(x,[150,150])
    x = np.array([x])
    predict = new_model.predict(preprocess_input(x))
    if np.argmax(predict) == 0:
        st.write('고양이')
    else:
        st.write('강아지')
# 클릭 이벤트 수행하지 않았을 때의 메시지        
else:
    st.write('오늘 하루도 행복한 하루 보내세요 :) :heart:')
    
    
# 다중 분류의 경우 위치로 진행! 가장 큰 확률값