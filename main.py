from flask import Flask, request
from tensorflow.keras.models import load_model
from imutils import paths
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import os
from flask_cors import CORS
import base64
import uuid

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'Model')
TEMP_DIR = os.path.join(BASE_DIR, "temp_img")
model_path = os.path.join(MODEL_DIR, "covid19.model")
print(BASE_DIR)
print(TEMP_DIR)
BS = 8

model = load_model(model_path)
predict_classes = ['covid', 'normal']
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'something-secret'

@app.post('/check_covid')
def check_covid():
    data = request.get_json()
    encoded_data = data['image_data'].split(',')[1]
    nparr = np.frombuffer(
        base64.b64decode(encoded_data),
        np.uint8
    )
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    temp_img_path = str(uuid.uuid4()) + ".png"
    temp_img = f"{TEMP_DIR}/{temp_img_path}"
    print(TEMP_DIR)
    print(temp_img)
    if not os.path.exists(TEMP_DIR):
        return {
            "msg": "Something went wrong"
        }, 200
    cv2.imwrite(temp_img, image)
    image = cv2.imread(temp_img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    image = image.reshape(1,224,224,3)
    preds = model.predict(image, batch_size=BS)
    index = np.argmax(preds)
    if predict_classes[index] == "covid":
        return {
            "msg": "Covid Detected",
            "status_code": 200
        }, 200
    else:
        return {
            "msg": "Covid Negative",
            "status_code": 200
        }, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
