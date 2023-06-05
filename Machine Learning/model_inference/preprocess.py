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

    # # For TF Lite, Don't uncomment yet
    # processed_image = preprocess_image(image)
    # input_details = interpreter.get_input_details()
    # output_details = interpreter.get_output_details()

    # interpreter.set_tensor(input_details[0]['index'], processed_image)
    # interpreter.invoke()
    # prediction = interpreter.get_tensor(output_details[0]['index'])
    # predicted_class = np.argmax(prediction)
    # get_class = grape_labels[predicted_class]

    return get_class