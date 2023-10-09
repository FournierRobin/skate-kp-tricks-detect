# app.py
import streamlit as st
import sys
import os

try:
    from ultralytics import YOLO
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "ultralytics"])
    from ultralytics import YOLO


# Load a model
model = YOLO('runs/pose/train/weights/best.pt')  # load a custom model

st.title("Skateboard Detection and Keypoint Recognition")

uploaded_file = st.file_uploader("Choose an image...", type="png")

if uploaded_file is not None:
    # Save the uploaded image to a temporary file
    if not os.path.exists('temp'):
        os.makedirs('temp')

    temp_file_path = os.path.join("temp", "temp_uploaded_file.png")
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    image = st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Result")

    # Predict with the model
    results = model(temp_file_path, save=True)  # predict on an uploaded image

    # Display the result
    # Assuming results contains a path to the saved image with predictions
    if results:  # if results is a path string
        st.image("runs/pose/predict4/temp_uploaded_file.png", caption='Processed Image.', use_column_width=True)
    else:
        st.write("Could not process the image. Please try again.")

    # Clean up by removing the temporary image
    os.remove(temp_file_path)
