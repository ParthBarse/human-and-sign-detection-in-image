import cv2
import requests
from flask import Flask, request

app = Flask(__name__)

def isValid(key):
    if key == "myKey":
        return True
    else:
        return False

@app.route('/',methods = ['POST', 'GET'])
def home():
    return "ok"


@app.route('/detectHuman',methods = ['POST', 'GET'])
def detectHuman():
    img = request.args.get("imgUrl")
    key = request.args.get("key")
    print(img)

    if isValid(key):
        imgUrl = img
        response = requests.get(imgUrl)
        file = open("sample_image.png", "wb")
        file.write(response.content)
        file.close()

        # Get user supplied values
        imagePath = "sample_image.png"
        cascPath = "haarcascade_frontalface_default.xml"

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            )

        if len(faces) >= 1:
            return "Person"
        else:
            return "Signature"
    else:
        return "Invalid Api Key"