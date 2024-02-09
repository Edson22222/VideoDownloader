from pytube import YouTube

def downloadVideo(url, path):
    yt = YouTube(url);
    stream = yt.streams.get_highest_resolution();
    stream.download(path);
    
url = input("Qual o url do video: ");
localPath = input("Qual a pasta que irá instala o video: ");
downloadVideo(url, localPath);