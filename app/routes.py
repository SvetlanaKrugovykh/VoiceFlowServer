# app/routes.py

from flask import Blueprint, request, jsonify
import os

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        segment_number = request.form.get('segment', 'unknown')
        filename = f"segment_{segment_number}.wav"
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        return jsonify({'message': f'File {filename} uploaded successfully'}), 200

