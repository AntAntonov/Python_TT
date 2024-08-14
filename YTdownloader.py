# from pytube import YouTube
# from sys import argv

# link = argv [1]
# yt = YouTube(link)
# print ("Title: ", yt.title)

# print ("View: ", yt.views)

# audio_streams = yt.streams.filter(only_audio=True)
# # [<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">,
# # <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">,
# # <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">,
# # <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]

# # print(yt.streams.filter(only_audio=True))
# for x in audio_streams:
#     print(x)


from pytube import YouTube
from sys import argv
import traceback

try:
    link = argv[1]
    yt = YouTube(link)
    
    print("Title:", yt.title)
    print("Views:", yt.views)
    
    audio_streams = yt.streams.filter(only_audio=True)
    for stream in audio_streams:
        print(stream)
except Exception as e:
    print("An error occurred:", e)
    traceback.print_exc()
