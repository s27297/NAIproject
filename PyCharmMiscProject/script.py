from flask import Flask, jsonify, request
from tdIf import classiffy_sentence
from mistral import ask_ollama
import requests
app = Flask(__name__)

# Allow CORS requests properly
from flask_cors import CORS

CORS(app)


@app.route("/<text>", methods=["GET", "POST", "OPTIONS"])
def handle_request(text):
    if request.method == "OPTIONS":
        return "", 200

    classification = classiffy_sentence(text)
    print("Classification:", classification)
    print("Authorization:", request.headers.get("Authorization"))
    json_req=(request.get_json())
    if(classification=="True"):
        json_req['text']=ask_ollama(text)
    response=requests.post('http://localhost:5000/posts/'+json_req['id']+'/comments', json=json_req,headers=request.headers)
    return jsonify({"message": "Hello world!", "classification": classification})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)