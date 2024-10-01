from flask import Flask, send_file
import pickle
import os

app = Flask(_name_)

# Define a directory to save the extracted files temporarily
MEDIA_DIR = 'media_files'
os.makedirs(MEDIA_DIR, exist_ok=True)


@app.route('/get_media/<media_type>')
def get_media(media_type):
    if media_type == 'audio':
        with open('audio_model.pkl', 'rb') as f:
            audio_data = pickle.load(f)
        audio_file_path = os.path.join(MEDIA_DIR, 'audio_file.mp3')
        with open(audio_file_path, 'wb') as f:
            f.write(audio_data)
        return send_file(audio_file_path, mimetype='audio/mpeg')

    elif media_type == 'video':
        with open('video_model.pkl', 'rb') as f:
            video_data = pickle.load(f)
        video_file_path = os.path.join(MEDIA_DIR, 'video_file.mp4')
        with open(video_file_path, 'wb') as f:
            f.write(video_data)
        return send_file(video_file_path, mimetype='video/mp4')


if _name_ == '_main_':
    app.run(debug=True)