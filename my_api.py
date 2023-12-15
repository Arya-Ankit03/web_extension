from flask import Flask, request, send_file
import main as mn

app = Flask(__name__)

@app.route('/download_video', methods=['POST'])
def download_vid():
    url = request.form.get('url')
    quality = request.form.get('quality')
    vid = mn.VideoDownloader(url)
    vid.video_checker(url)

    try:
        if quality == 'highest':
            # file_path = mn.download_yt_video_1080p(url)
            return send_file(vid.download_video('1080p'), as_attachment=True)
        elif quality == 'high':
            # file_path = mn.download_yt_video_720p(url)
            return send_file(vid.download_video('720p'), as_attachment=True)
        elif quality == 'low':
            file_path = mn.download_yt_video_480p(url)
            return send_file(vid.download_video('480p'), as_attachment=True)
        else:
            return "Invalid quality parameter"
        # return send_file(file_path, as_attachment=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to download video"

@app.route('/download_audio', methods=['POST'])
def download_audio():
    url = request.form.get('url')
    audio = mn.VideoDownloader(url)

    try:
        file_path = audio.download_audio()
        return send_file(file_path, as_attachment=True, download_name='audio.webm')
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to download audio"

if __name__ == '__main__':
    app.run(debug=True)
