import pytube as pt

video_url = 'https://www.youtube.com/watch?v=AsvhscWKcnM&t=4s'

for i in pt.YouTube(video_url).streams:
    # print(i)
    pass
yt = pt.YouTube(video_url)
def video_checker(url):
    try:
        my_dict = {
            "1080p" : None,
            "720p" : None,
            "480p" : None
        }

        
        video = yt.streams.filter(progressive=True)

        for avail_streams in video:
            if avail_streams.resolution == "720p":
                my_dict["720p"] = avail_streams.itag
            if avail_streams.resolution == "1080p":
                my_dict["1080p"] = avail_streams.itag
                print(avail_streams.itag)
            if avail_streams.resolution == '480p':
                my_dict["480p"] = avail_streams.itag
                print(avail_streams.itag)

    except:
        print(f'An error occurred: ')

def download_yt_video_1080p(itag):
    try:
        stream=yt.stream.get_by_itag(itag)
        stream.dowload()
    except:
        print(f'An error occurred: ')


def download_yt_video_720p(itag):
    try:
        stream=yt.stream.get_by_itag(itag)
        stream.dowload()
    except:
        print(f'An error occurred: ')

def download_yt_video_480p(itag):
    try:

        stream=yt.stream.get_by_itag(itag)
        stream.dowload()
    except:
        print(f'An error occurred: ')


def download_youtube_audiio(url):
    try:
        yt = pt.YouTube(url)
        audio = yt.streams.filter(only_audio=True)
        final = audio.order_by("abr").last()
        final.download()
    except:
        pass


download_youtube_audiio(video_url)
# Call the function with the video URL
# download_youtube_audiio(video_url)