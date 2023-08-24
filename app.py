import os

from flask import Flask, request, render_template
import tensorflow as tf

from clasifier import classify

app = Flask(__name__)

STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/uploads/"


model = tf.keras.models.load_model(STATIC_FOLDER + "/models/" + "rps.h5")


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/classify", methods=["POST"])
def upload_file():

    file = request.files["image"]
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    predicted_class, probability = classify(model, filename)
    return render_template("result.html", predicted_class=predicted_class, probability=round((probability * 100), 2))


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
