import pytube as pt

video_url = 'https://www.youtube.com/watch?v=rx57Og8MTm0'
        
class VideoDownloader:
    def __init__(self, vid_url):
        self.vid_url = vid_url
        self.yt_video = pt.YouTube(self.vid_url)
        self.my_dict = {
                "1080p" : None,
                "720p" : None,
                "480p" : None
            }

    def video_checker(self):
        try:
                video = self.yt_video.streams.filter(progressive=True)
                print(video)
                for avail_streams in video:
                    for res, tag in self.my_dict.items():
                        if avail_streams.resolution == res:
                            self.my_dict[res] = avail_streams.itag
                            print(avail_streams.itag)
                print(self.my_dict)
        except:
            print(f'An error occurred')
            print(self.my_dict)

    def download_video(self, resolution):
        # Not working as of now 
        try:
            if self.my_dict[resolution] != None:
                stream = self.yt_video.stream.get_by_itag(self.my_dict[resolution])
                stream.default_filename()
                stream.dowload()
        
        except:
            print("Something wrong, unable to download")
        
    def download_audio(self):
        try:
            audio = self.yt_video.streams.filter(only_audio=True)
            audio_file = audio.order_by("abr").last()
            audio_file.download()
        except:
            print(f"Unable to download audio file")

if __name__ == '__main__':
    vid_down = VideoDownloader(video_url)
    vid_down.video_checker()
    # vid_down.download_audio()
