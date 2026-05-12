import os
import cv2
import numpy as np
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import MobileNetV2

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load Models
SEQ_MODEL_PATH = 'violence_detection_model.h5'
seq_model = load_model(SEQ_MODEL_PATH)
feature_extractor = MobileNetV2(include_top=False, weights='imagenet', input_shape=(96, 96, 3), pooling='avg')

def process_video_to_features(video_path, target_frames=10):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    skip = max(int(total_frames / target_frames), 1)
    frames = []
    for i in range(target_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * skip)
        ret, frame = cap.read()
        if not ret: break
        frame = cv2.resize(frame, (96, 96))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame / 255.0 
        frames.append(frame)
    cap.release()
    while len(frames) < target_frames:
        frames.append(np.zeros((96, 96, 3)))
    features = feature_extractor.predict(np.array(frames))
    return np.expand_dims(features, axis=0)

def predict_violence(video_path):
    sequence_features = process_video_to_features(video_path)
    predictions = seq_model.predict(sequence_features)[0]
    classes = ["NonViolence", "Violence"]
    idx = np.argmax(predictions)
    return classes[idx], float(predictions[idx]) * 100

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            try:
                label, confidence = predict_violence(filepath)
                return render_template('index.html', 
                                       prediction=label, 
                                       confidence=f"{confidence:.2f}%", 
                                       video_url=filename)
            except Exception as e:
                return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)