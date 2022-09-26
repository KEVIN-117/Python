from pytube import YouTube
YouTube('https://youtu.be/TlMieC74SGQ').streams.first().download()
yt = YouTube(input("Ingrese el link del video: "))
yt.streams.filter(progressive="true", file_extension="mp4").order_by('resolution').desc().first().download()
print("complete download")