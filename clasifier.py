import numpy as np
from tensorflow.keras.preprocessing import image


def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(60, 40))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array


def classify(model, image_path: str):
    preprocessed_image = preprocess_image(image_path)
    prediction = model.predict(preprocessed_image)

    predicted_class = np.argmax(prediction)
    class_label = ""

    if predicted_class == 0:
        class_label = "paper"
    elif predicted_class == 1:
        class_label = "rock"
    else:
        class_label = "scissors"

    probability = prediction[0][predicted_class]
    return class_label, probability
