from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для всех источников

PLACES_FILE = "places.json"

# Загрузка мест
@app.route("/places", methods=["GET"])
def get_places():
    if not os.path.exists(PLACES_FILE):
        return jsonify([])
    with open(PLACES_FILE, encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

# Добавление нового места
@app.route("/add_place", methods=["POST"])
def add_place():
    new_place = request.get_json()
    if not new_place:
        return jsonify({"status": "error", "message": "No data received"}), 400

    places = []
    if os.path.exists(PLACES_FILE):
        with open(PLACES_FILE, encoding="utf-8") as f:
            places = json.load(f)

    places.append(new_place)
    with open(PLACES_FILE, "w", encoding="utf-8") as f:
        json.dump(places, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "success"})
