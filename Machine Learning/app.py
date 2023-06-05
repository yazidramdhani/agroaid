from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
from keras.utils import img_to_array, load_img
import keras
from model_inference.preprocess import inference_pred

app = Flask(__name__)

# TODO Add Model
grape_model = keras.models.load_model('./models/grape_model')
pepperbell_model = keras.models.load_model('./models/pepperbell_model')
potato_model = keras.models.load_model('./models/potato_model')

# TODO Add Labels
file_paths = ['./labels/grape_labels.txt', './labels/pepperbell_labels.txt', './labels/potato_labels.txt']
label_lists = []

for file_path in file_paths:
    with open(file_path, 'r') as file:
        labels = [line.strip() for line in file.readlines()]
    label_lists.append(labels)

# TODO Sesuai urutan file_paths
grape_labels, pepperbell_labels, potato_labels = label_lists

@app.route('/')
def hello():
    helo = "Ini versi tensorflow: " + tf.__version__
    return helo

if __name__ == '__main__':
    app.run()

# TODO Add Route
@app.route('/predict-grape', methods=['POST'])
def prediction_grape():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})

    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(grape_model, image, grape_labels)

    return jsonify({'prediction':predicted_disease})

@app.route('/predict-pepperbell', methods=['POST'])
def prediction_pepperbell():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(pepperbell_model, image, pepperbell_labels)

    return jsonify({'prediction':predicted_disease})

@app.route('/predict-potato', methods=['POST'])
def prediction_potato():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(potato_model, image, potato_labels)

    return jsonify({'prediction':predicted_disease})