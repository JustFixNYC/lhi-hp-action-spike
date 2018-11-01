import json
import base64
from flask import Flask, request

POST_DATA_JSON = 'post_data.json'
BINARY_FILE = 'binary_file.pdf'
ANSWER_FILE = 'answer_file.xml'

app = Flask(__name__)


def decode_and_write_data(data, filename):
    data = base64.b64decode(data.replace(' ', '+'))
    with open(filename, 'wb') as f:
        f.write(data)
    print(f"Wrote {filename}.")


@app.route('/', methods=['POST'])
def receive_document():
    print(
        f"Received POST with "
        f"length={request.content_length}, type={request.content_type}."
    )
    form = request.form
    for key in form:
        print(f"Form key {key} has length {len(form[key])}.")

    with open(POST_DATA_JSON, 'w') as f:
        f.write(json.dumps(form, indent=2))
    print(f"Wrote POST data to {POST_DATA_JSON}.")

    decode_and_write_data(form['binary_file'], BINARY_FILE)
    decode_and_write_data(form['answer_file'], ANSWER_FILE)

    return (
        'Data received by Flask server! See the Flask server '
        'console for more details.'
    )
