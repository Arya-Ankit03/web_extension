// content_scripts.js

// Function to handle form submission for video download
function downloadVideo(event) {
  event.preventDefault();
  const videoUrl = document.getElementById('video-url').value;
  const videoQuality = document.getElementById('video-quality').value;

  // Sending data to the background script to initiate download
  chrome.runtime.sendMessage({ action: 'download_video', url: videoUrl, quality: videoQuality });
}

// Function to handle form submission for audio download
function downloadAudio(event) {
  event.preventDefault();
  const audioUrl = document.getElementById('audio-url').value;

  // Sending data to the background script to initiate download
  chrome.runtime.sendMessage({ action: 'download_audio', url: audioUrl });
}

// Event listeners for form submissions
document.querySelector('form[action="http://127.0.0.1:5000/download_video"]').addEventListener('submit', downloadVideo);
document.querySelector('form[action="http://127.0.0.1:5000/download_audio"]').addEventListener('submit', downloadAudio);
