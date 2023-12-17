// background.js

// Function to handle message passing from content script
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'download_video') {
        // Sending POST request to Flask server for video download
        fetch('http://127.0.0.1:5000/download_video', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `url=${encodeURIComponent(request.url)}&quality=${encodeURIComponent(request.quality)}`
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `video.${request.quality}.mp4`;
            a.click();
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    } else if (request.action === 'download_audio') {
        // Sending POST request to Flask server for audio download
        fetch('http://127.0.0.1:5000/download_audio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `url=${encodeURIComponent(request.url)}`
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.blob();
        })
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'audio.mp3';
            a.click();
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    }
});
