import streamlit as st
import cv2
import numpy as np
from algorithms.spatial import mean_blur_filter, median_filter, gaussian_blur_filter, laplacian_filter
from algorithms.edge_detection import sobel_edge_detection, prewitt_edge_detection
from algorithms.segmentation import global_thresholding
from algorithms.color_utils import apply_to_color

st.title("DIP Lab")
descriptions = {
    "Mean Blur": "Averages each pixel with its neighbors to smooth the image and reduce noise.",
    "Median Blur": "Replaces each pixel with the median of its neighborhood — great for removing salt-and-pepper noise while preserving edges.",
    "Gaussian Blur": "Applies a weighted average based on a bell-curve distribution, giving smoother, more natural blurring than a simple mean.",
    "Sharpen (Laplacian)": "Enhances edges by detecting rapid intensity changes and adding them back to the original image.",
    "Sobel Edge Detection": "Detects edges by computing horizontal and vertical intensity gradients and combining their magnitude.",
    "Prewitt Edge Detection": "Similar to Sobel, detects edges using horizontal and vertical gradient kernels with equal weighting.",
    "Global Thresholding": "Converts the image to pure black and white by comparing every pixel against a fixed brightness threshold."
}

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")

    selected_filter = st.sidebar.selectbox("Choose a filter", list(descriptions.keys()))

    st.sidebar.markdown(f"**Description:** {descriptions[selected_filter]}")

    color_supported = selected_filter in ["Mean Blur", "Median Blur", "Gaussian Blur", "Sharpen (Laplacian)"]

    use_color = False
    if color_supported:
        use_color = st.sidebar.checkbox("Process in color")

    if selected_filter == "Mean Blur" or selected_filter == "Median Blur" or selected_filter == "Gaussian Blur":
        kernel_size = st.sidebar.slider("Specify kernel size", 3, 15, 3, 2)
    if selected_filter == "Gaussian Blur":
        sigma = st.sidebar.slider("Sigma = ", 0.0, 5.0, 1.0, 0.5)
    if selected_filter == "Global Thresholding":
        threshold = st.sidebar.slider("Threshold", 0, 255, 100, 1)

    if st.sidebar.button("Apply Filter"):
        file_bytes = np.frombuffer(uploaded_file.getvalue(), np.uint8)

        if use_color:
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
            
        if img is None:
            st.error("Could not read this file as an image. Please upload a valid JPG or PNG.")
            st.stop()

        with st.spinner("Applying filter..."):
            if selected_filter == "Mean Blur":
                result = apply_to_color(mean_blur_filter, img, kernel_size) if use_color else mean_blur_filter(img, kernel_size)
            elif selected_filter == "Median Blur":
                result = apply_to_color(median_filter, img, kernel_size) if use_color else median_filter(img, kernel_size)
            elif selected_filter == "Gaussian Blur":
                result = apply_to_color(gaussian_blur_filter, img, kernel_size, sigma) if use_color else gaussian_blur_filter(img, kernel_size, sigma)
            elif selected_filter == "Sharpen (Laplacian)":
                result = apply_to_color(laplacian_filter, img) if use_color else laplacian_filter(img)
            elif selected_filter == "Sobel Edge Detection":
                result = sobel_edge_detection(img)
            elif selected_filter == "Prewitt Edge Detection":
                result = prewitt_edge_detection(img)
            elif selected_filter == "Global Thresholding":
                result = global_thresholding(img, threshold)
            
        if use_color:
            encode_img = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
        else:
            encode_img = result
        success, encode_image = cv2.imencode(".jpg", encode_img)

        st.download_button(
            label="Download Filtered Image",
            data=encode_img.tobytes(),
            file_name="filtered_image.jpg",
            mime="image/jpeg"
        )
          

        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption="Original")
        with col2:
            st.image(result, caption="Filtered Image")