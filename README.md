# AI Violence Detection System

A Flask-based web application that detects whether an uploaded video contains violent or non-violent activity using a trained deep learning model.

## 📌 Project Overview

The AI Violence Detection System is designed to analyze video files and classify them as either **Violence** or **Non-Violence**.  
This project uses a trained deep learning model to process video input and display the prediction result along with a confidence score.

It can be useful for learning how video classification systems work using Python, Flask, TensorFlow/Keras, and OpenCV.

---

## ✨ Features

- Upload video files through a web interface
- Detects whether the video is violent or non-violent
- Displays prediction result
- Shows confidence score
- Simple and user-friendly interface
- Flask-based backend
- Deep learning model integration
- Supports local execution

---

## 🛠️ Technologies Used

- Python
- Flask
- TensorFlow
- Keras
- OpenCV
- NumPy
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

```text
AI_Violence_Detection_System
│
├── app.py
├── fix_model.py
├── requirements.txt
├── model_metadata.json
├── violence_detection_model.h5
├── templates/
│   └── index.html
├── input/
│   ├── NV_1000.mp4
│   ├── V_100.mp4
│   └── V_104.mp4
├── uploads/
├── README.md
└── venv/  # Not uploaded to GitHub

⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/your-username/AI_Violence_Detection_System.git
cd AI_Violence_Detection_System
2. Create Virtual Environment

For macOS/Linux:

python3 -m venv venv
source venv/bin/activate

For Windows:

python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application

For macOS/Linux:

PYTHONNOUSERSITE=1 python3 app.py

For Windows:

python app.py
5. Open in Browser

Open this URL in your browser:

http://127.0.0.1:5000
🧪 How to Use
Open the application in the browser.
Upload a video file.
Click on the analyze/detect button.
The system will process the video.
The prediction result will be displayed as:
Violence
Non-Violence
Confidence score will also be shown.
🧠 Model Information

The project uses a trained deep learning model saved as:

violence_detection_model.h5

The model is loaded in the Flask application using TensorFlow/Keras.

If the model file is not included in the repository due to GitHub file size limits, download it separately and place it in the project root directory.

Expected location:

AI_Violence_Detection_System/violence_detection_model.h5
⚠️ Important Notes
Do not upload the venv folder to GitHub.
Make sure violence_detection_model.h5 is present in the project folder.
If you face TensorFlow/Keras model loading issues, run:
python3 fix_model.py

Then run the app again:

PYTHONNOUSERSITE=1 python3 app.py
The warning related to NotOpenSSLWarning can usually be ignored during local development.
📦 Requirements

Main dependencies include:

Flask
TensorFlow
Keras
OpenCV
NumPy
h5py
Pillow

Install all dependencies using:

pip install -r requirements.txt
🚀 Future Improvements
Add real-time CCTV violence detection
Improve model accuracy
Add dashboard for analysis history
Add support for multiple video formats
Add user authentication
Deploy the application online
Add database support for storing results
👩‍💻 Author

Satakshi Rathod

📄 License

This project is created for educational and learning purposes.


Agar GitHub repo ke andar outer folder bhi hai, jaise:

```text
AI_Violence_Detection_System/violence-detection-system/app.py

to README me cd AI_Violence_Detection_System ke baad ye line add kar dena:

cd violence-detection-system
