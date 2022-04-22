import pytube
from pytube import YouTube
yt = YouTube(input('Link: '))
print("Title = " + yt.title)
stream = None

def get_stream_audio():
    # print("Downloading audio from: " + yt)
    stream = yt.streams.get_by_itag(22)

def get_stream_video():
    print("Downloading video and audio from: " + yt)
    stream = yt.streams.get_by_itag(140)

def get_stream_captions():
    try:
        caption = yt.captions.get_by_language_code('en-CA')
    except:    
        print("Error trying en-CA")
    else:
        print("bruh")
        # try:
        #     print("CA", file=open("output.txt", "a"))
        #     caption = yt.captions.get_by_language_code('en-CA')
        # except:
        #     print("Error trying autogenerated")
        # else:
        #     try:
        #         print("a.en", file=open("output.txt", "a"))
        #         caption = yt.captions.get_by_language_code('a.en')
        #     except:
        #         print("There are no english subtitles")
    print(caption.generate_srt_captions(), file=open("output.txt", "a"))

def download():
    try:
        stream.download("Desktop")
        print("success")
    except:
        print('connection error')

print("1. Full Video")
print("2. Audio only")
print("3. Captions")
method = int(input("Pick a number: "))

if method == 2:
    get_stream_audio()
    download()
elif method == 1:
    get_stream_video()
    download()
elif method == 3:
    get_stream_captions()
else:
    print('invalid number')