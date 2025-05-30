import os
from flask import Flask, request, render_template, send_file, jsonify
from werkzeug.utils import secure_filename
import requests
from PIL import Image
import io
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

API_KEY = os.getenv('CLIPDROP_API_KEY', 'b08e190eced2606342e3f5007f916e14330008642db7485b9a95fe9a1d7b8c7ca6d475be18b8a1285a3154a6b80f29bc')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def resize_and_center(img, target_size=125, margin=1.5):
    img.thumbnail((target_size - 2 * margin, target_size - 2 * margin), Image.LANCZOS)
    
    new_img = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
    paste_x = (target_size - img.width) // 2
    paste_y = (target_size - img.height) // 2
    new_img.paste(img, (paste_x, paste_y), img)

    return new_img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    # Read the image file
    image_data = file.read()
    
    # Remove background using ClipDrop API
    response = requests.post(
        "https://clipdrop-api.co/remove-background/v1",
        files={"image_file": image_data},
        headers={"x-api-key": API_KEY},
    )

    if response.status_code != 200:
        return jsonify({'error': 'Failed to remove background'}), 500

    # Process the image
    img = Image.open(io.BytesIO(response.content)).convert("RGBA")
    final_img = resize_and_center(img)

    # Save to bytes
    img_byte_arr = io.BytesIO()
    final_img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return send_file(
        img_byte_arr,
        mimetype='image/png',
        as_attachment=True,
        download_name='processed_image.png'
    )

# For local development
if __name__ == '__main__':
    app.run(debug=True) 