from flask import Flask, request
from transformers import pipeline
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    # get string from request (base64 encoded image)
    image = request.form['image']

    # The string we got is an image in base64, we
    # need to decode it and save it to a file
    image = base64.b64decode((image.split(','))[1].encode('utf-8'))
    path = 'image.png'
    with open(path, 'wb') as f:
        f.write(image)

    model = pipeline('image-to-text', model = "model")
    caption = model(path)
    return caption[0]

if __name__ == '__main__':
    app.run(debug=True)