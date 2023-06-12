from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
from keras.utils import img_to_array, load_img
import keras
from model_inference.preprocess import inference_pred

app = Flask(__name__)

# TODO Add Model
grape_model = keras.models.load_model('./models/grape_model/grape_model.h5')
pepperbell_model = keras.models.load_model('./models/pepperbell_model/pepperbell_model.h5')
potato_model = keras.models.load_model('./models/potato_model/potato_model.h5')

cherry_model = keras.models.load_model('./models/cherry/cherry_model.h5', compile=False)
cherry_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

peach_model = keras.models.load_model('./models/peach/peach_model.h5', compile=False)
peach_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

strawberry_model = keras.models.load_model('./models/strawberry/strawberry_model.h5', compile=False)
strawberry_model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# TODO Add Labels
file_paths = ['./labels/grape_labels.txt', 
              './labels/pepperbell_labels.txt', 
              './labels/potato_labels.txt',
              './labels/cherry_labels.txt',
              './labels/peach_labels.txt',
              './labels/strawberry_labels.txt']
label_lists = []

for file_path in file_paths:
    with open(file_path, 'r') as file:
        labels = [line.strip() for line in file.readlines()]
    label_lists.append(labels)

# TODO Sesuai urutan file_paths
grape_labels, pepperbell_labels, potato_labels, cherry_labels, peach_labels, strawberry_labels = label_lists

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

@app.route('/predict-cherry', methods=['POST'])
def prediction_cherry():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(cherry_model, image, cherry_labels)

    return jsonify({'prediction':predicted_disease})

@app.route('/predict-peach', methods=['POST'])
def prediction_peach():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(peach_model, image, peach_labels)

    return jsonify({'prediction':predicted_disease})

@app.route('/predict-strawberry', methods=['POST'])
def prediction_strawberry():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')
    
    predicted_disease = inference_pred(strawberry_model, image, strawberry_labels)

    return jsonify({'prediction':predicted_disease})
