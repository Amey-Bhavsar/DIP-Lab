import streamlit as st
import cv2
import numpy as np
from algorithms.spatial import mean_blur_filter , median_filter , gaussian_blur_filter , laplacian_filter
from algorithms.edge_detection import sobel_edge_detection , prewitt_edge_detection
from algorithms.segmentation import global_thresholding

st.title("DIP Lab")

uploaded_file = st.file_uploader("Upload an image" , type=["jpg" , "jpeg" , "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")
    selected_filter = st.selectbox("Choose a filter", ["Mean Blur", "Median Blur" , "Gaussian Blur" , "Sharpen (Laplacian)" , "Sobel Edge Detection" , "Prewitt Edge Detection" , "Global Thresholding"])
    if selected_filter == "Mean Blur" or selected_filter == "Median Blur" or selected_filter == "Gaussian Blur":
        kernel_size = st.slider("Specify kernel size" , 3 , 15 , 3 , 2)
    if selected_filter == "Gaussian Blur" : 
        sigma = st.slider("Sigma = " , 0.0 , 5.0 , 1.0 , 0.5)
    if selected_filter == "Global Thresholding":
        threshold = st.slider("Threshold" , 0 , 255 , 100 , 1)
    if st.button("Apply Filter") :
        file_bytes = np.frombuffer(uploaded_file.getvalue(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

        if selected_filter == "Mean Blur":
            result = mean_blur_filter(img, kernel_size)
        elif selected_filter == "Median Blur":
            result = median_filter(img, kernel_size)
        elif selected_filter == "Gaussian Blur":
            result = gaussian_blur_filter(img, kernel_size, sigma)
        elif selected_filter == "Sharpen (Laplacian)":
            result = laplacian_filter(img)
        elif selected_filter == "Sobel Edge Detection":
            result = sobel_edge_detection(img)
        elif selected_filter == "Prewitt Edge Detection":
            result = prewitt_edge_detection(img)
        elif selected_filter == "Global Thresholding":
            result = global_thresholding(img, threshold)
        

        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption="Original")
        with col2:
            st.image(result, caption="Filtered Image")

