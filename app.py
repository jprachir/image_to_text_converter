# setup
import streamlit as st
from transformers import pipeline
import requests
from PIL import Image
from io import BytesIO

# hf_token = "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"
# Load model directly

# load the huggingface model img2txt
im2txt = pipeline("image-to-text")

# streamlit app header
st.title("Image to text converter app")

# user input
uploaded_image = st.file_uploader("upload an image",type=['jpg','png','jpeg'])

if uploaded_image is not None:
    st.image(uploaded_image, caption="uploaded image",use_column_width=True)
    try:
        image = Image.open(uploaded_image)
        image_text = im2txt(image)
        st.subheader("image description")
        st.write(image_text[0]['generated_text'])

    except Exception as e:
        st.error(f'an error occured: {e}')
