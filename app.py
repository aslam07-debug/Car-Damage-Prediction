import streamlit as st
from model_helper import predict
st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img_path = "temp_path.jpg"

    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        prediction = predict(uploaded_file)
        st.info(f'Predicted Class : {prediction}')