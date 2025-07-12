from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)
DATA_FILE = 'places.json'

def load_places():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_places(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/places', methods=['GET'])
def get_places():
    return jsonify(load_places())

@app.route('/add_place', methods=['POST'])
def add_place():
    data = request.get_json()
    places = load_places()
    places.append(data)
    save_places(places)
    return jsonify({'status': 'success'})
