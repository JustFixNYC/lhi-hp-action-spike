from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive_document():
    print(f"Received POST with content length {request.content_length}")
    return 'Hello from the Flask server!'
