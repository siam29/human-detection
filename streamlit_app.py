# import streamlit as st
# import requests
# from PIL import Image
# from io import BytesIO

# st.title("🚦 Human Detection on Road")

# uploaded_file = st.file_uploader("Upload a road image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Original Image", use_column_width=True)

#     response = requests.post(
#         "http://localhost:8000/detect/",
#         files={"file": uploaded_file.getvalue()}
#     )

#     if response.status_code == 200:
#         result_image = Image.open(BytesIO(response.content))
#         st.image(result_image, caption="Detected Humans", use_column_width=True)
#     else:
#         st.error("Detection failed.")


import time
import requests
from PIL import Image
from io import BytesIO
import streamlit as st

st.title("🚦 Human Detection on Road")

uploaded_file = st.file_uploader("Upload a road image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Original Image", use_column_width=True)

    start = time.time()

    response = requests.post(
        "https://human-detection-1.onrender.com/detect/",
        files={"file": uploaded_file.getvalue()}
    )

    end = time.time()
    st.write("🕒 Detection time:", round(end - start, 4), "seconds")

    if response.status_code == 200:
        result_image = Image.open(BytesIO(response.content))
        st.image(result_image, caption="Detected Humans", use_column_width=True)
    else:
        st.error("Detection failed.")
