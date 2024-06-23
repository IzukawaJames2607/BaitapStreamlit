import streamlit as st

st.title("Playground")
st.text_area('Input prompt', '')
st.button('Submit')
st.slider('Temperature', min_value=0.00, max_value=2.00, value=1.00)
st.slider('Top P', min_value=0.00, max_value=1.00, value=1.00)
st.slider('Maximum length', min_value=1, max_value=4000, value=1)
st.checkbox('Show probabilities')
st.code("""print('Hello world!')""", language='python',line_numbers=True)
