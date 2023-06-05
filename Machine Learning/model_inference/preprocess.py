import numpy as np

def preprocess_image(image):
    image = image.resize((224,224))
    image_array = np.array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    return image_array

def inference_pred(model, image, labels):
    # Keras model
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction)
    get_class = labels[predicted_class]

    return get_class