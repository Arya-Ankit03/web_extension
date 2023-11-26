from flask import Flask, request, send_file
import main as mn

app = Flask()

@app.route('/download_video', methods=['POST'])
def download_vid():
    url = request.form.get('url')
    quality = request.form.get('quality')

    try:
        mn.video_checker(url)
        
        if quality == 'highest':
            file_path = mn.download_yt_video_1080p(url)
        elif quality == 'high':
            file_path = mn.download_yt_video_720p(url)
        elif quality == 'low':
            file_path = mn.download_yt_video_480p(url)
        else:
            return "Invalid quality parameter"
        
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to download video"

@app.route('/download_audio', methods=['POST'])
def download_audio():
    url = request.form.get('url')
    
    try:
        file_path = mn.download_youtube_audio(url)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to download audio"

if __name__ == '__main__':
    app.run(debug=True)
