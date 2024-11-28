from flask import Flask, render_template, request, redirect, url_for
import os
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)

# Load the YOLOv8 model (use a pretrained model or your own trained model)
model = YOLO('best.pt')  # You can use 'yolov8n.pt', 'yolov8s.pt', or any other pretrained YOLOv8 model

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user doesn't select a file
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Run the YOLO model on the uploaded image
            result_image, occupied_count, empty_count = detect_objects(filepath)

            # Save the result image (with bounding boxes)
            result_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_' + filename)
            cv2.imwrite(result_image_path, result_image)
            result_image_url = 'static/uploads/' + 'result_' + filename

            filepath = filepath.replace('\\', '/')

            return render_template('index.html', 
                                   filename=filepath, 
                                   result_image_url=result_image_url,
                                   occupied_count=occupied_count, 
                                   empty_count=empty_count)

    return render_template('index.html', filename=None, occupied_count=0, empty_count=0)

def detect_objects(image_path, save=True, save_dir="static/uploads/"):
    # Read the image
    img = cv2.imread(image_path)
    # Perform object detection with the YOLOv8 model
    results = model.predict(source=img)  # Running inference on the image
    
    # Get the annotated image (draw bounding boxes on the original image)
    annotated_image = results[0].plot()  # results[0] is the first image, annotated with bounding boxes

    # Save the annotated image if requested
    result_image_path = f"{save_dir}result_{image_path.split('/')[-1]}"  # Save with a new name
    cv2.imwrite(result_image_path, annotated_image)

    occupied_count = 0
    empty_count = 0
    if results:
        predictions = results[0].boxes.cls  # Access predictions from the Results object

        for prediction in predictions:
            predicted_class_index = int(prediction.cpu().numpy())  # Convert tensor to int

            # Define a mapping from class index to class name (adjust if necessary)
            class_names = {0: 'Occupied', 1: 'Unoccupied'}

            predicted_class = class_names.get(predicted_class_index, 'Unknown')

            # Increment counts based on predicted classes
            if predicted_class == 'Occupied':
                occupied_count += 1
            elif predicted_class == 'Unoccupied':
                empty_count += 1

    return annotated_image, occupied_count, empty_count

if __name__ == '__main__':
    app.run(debug=True)
