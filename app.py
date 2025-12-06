import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("1.keras")

model = load_model()

# Class names
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Preprocess function
def preprocess_image(image):
    img = image.resize((256, 256))       # Adjust based on your training size
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# --- UI DESIGN ---

st.set_page_config(page_title="Potato Disease Detector", layout="centered")

st.markdown("""
    <h1 style="text-align:center;">🥔 Potato Leaf Disease Detection</h1>
    <p style="text-align:center; color: #444;">
        Upload an image or use your camera to detect potato plant health.
    </p>
""", unsafe_allow_html=True)

option = st.selectbox("Choose Input Method", ["Upload Image", "Use Camera"])


# --- IMAGE UPLOAD ---
uploaded_image = None

if option == "Upload Image":
    uploaded_image = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)


# --- CAMERA INPUT ---
elif option == "Use Camera":
    cam_image = st.camera_input("Capture an image")

    if cam_image:
        image = Image.open(cam_image)
        st.image(image, caption="Captured Image", use_container_width=True)
        uploaded_image = cam_image  # Treat as uploaded


# --- PREDICTION BUTTON ---
if uploaded_image:
    if st.button("🔍 Analyze Image"):
        with st.spinner("Analyzing..."):
            img = Image.open(uploaded_image)
            processed = preprocess_image(img)
            preds = model.predict(processed)
            class_id = np.argmax(preds)
            confidence = preds[0][class_id]

        st.success(f"### 🩺 Result: **{CLASS_NAMES[class_id]}**")
        st.info(f"Confidence: **{confidence:.2%}**")

        # Color-coded box
        if CLASS_NAMES[class_id] == "Healthy":
            color = "#2ecc71"
        elif CLASS_NAMES[class_id] == "Early Blight":
            color = "#f39c12"
        else:
            color = "#e74c3c"

        st.markdown(
            f"""
            <div style='padding:15px; border-radius:10px; text-align:center; 
            background-color:{color}; color:white; font-weight:bold; font-size:20px;'>
                {CLASS_NAMES[class_id]}
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.markdown(
    "<p style='text-align:center; margin-top:40px; color:#999;'>© 2025 Potato Disease Classifier</p>",
    unsafe_allow_html=True
)
