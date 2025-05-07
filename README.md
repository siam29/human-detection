# human-detection
This project detects humans in road images using classical computer vision (Haar Cascade) or optionally deep learning (YOLOv8). It features:

- A FastAPI backend to upload and process images

- A Streamlit frontend to interact with the app

- Free deployment using Render and Streamlit Cloud

## Project Structure

```
human-detection/
│
├── fastapi_app.py         # FastAPI backend
├── streamlit_app.py       # Streamlit frontend
├── model.py               # Human detection logic
├── requirements.txt       # Python dependencies
├── render.yaml            # Render deployment config
├── uploaded_images/       # Temp folder for uploads
├── output.jpg             # Output image result
└── README.md              # This file
```

## Set up this project
### Clone the Repository
`
git clone https://github.com/siam29/human-detection.git
`
`
cd human-detection
`
### Create Virtual Environment
`
python -m venv env
`
`
source env/bin/activate
`
###  Install Requirements
`
pip install -r requirements.txt
`
### Run FastAPI App
`
uvicorn fastapi_app:app --reload
`
Visit: http://127.0.0.1:8000/docs 

### Run Streamlit Frontend
Open another terminal and go to main directory
`
cd human-detection
`
`
streamlit run streamlit_app.py
`