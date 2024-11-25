import streamlit as st
st.write('Hello world!')

import streamlit as st
st.header('st.button')

if st.button('say hello'):
    st.write('why hello there')
else:
    st.write('goodbye')

st.header('st.slider')
st.subheader('Slider')
age = st.slider('당신의 나이는?', 0, 130, 25)
st.write('나는', age, '살입니다.')

option = st.selectbox(
    '가장 좋아하는 색상은 무엇인가요?',
    ('파랑','빨강','초록'))

option = st.multiselect(
    '가장 좋아하는 색상은 무엇인가요',
    ['초록','노랑','빨강','파랑'],
    ['노랑', '빨강'])

icecream = st.checkbox('아이스크림')
coffee = st.checkbox('커피')
cola = st.checkbox('콜라')
