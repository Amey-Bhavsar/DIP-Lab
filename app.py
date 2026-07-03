import streamlit as st

st.title("DIP Lab")

uploaded_file = st.file_uploader("Upload an image" , type=["jpg" , "jpeg" , "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")

    