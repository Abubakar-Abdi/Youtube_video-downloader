from django.shortcuts import render
from pytube import YouTube
# Create your views here.

def how_to_download_youtube_video_hd_v2(request):
    return render(request, "aboutusv4.html")
def aboutusv4(request):
    return render(request, "aboutusv4.html")
def en50(request):
    return render(request, "snapsave.io/en50.html")
def youtubemp3(request):
    return render(request, "youtube-mp3.html")

def home(request):
    return render(request, "home.html")

def final(request):
    return render(request, "final.html")

def submit(request):
    url = request.GET['inp']
    #print("This is main url"+url)
    url2 = url[17:]
    #print("This is second url"+url2)
    url3 = url[:11]
    #print("This is third url"+url3)
    obj = YouTube(url)
    streams = obj.streams.all()
    # list of resolutions
    res = []
    for i in streams:
        res.append(i.resolution)
    # list of resollutions with no duplicates
    res = list(dict.fromkeys(res))
    
    #embed = url.replace("watch?v=", "embed/")
    embed = url3+"tube.com/embed/"+url2  # slicing the main url and added "tube.com/embed/" to it to get the embed url
    #print("This is embed url"+embed)
    return render(request, "list.html", {"url": url,"url2": url2, "embed": embed, "res": res})

def download(request, pixel):
    path = "C:/Users/hp/Downloads"
    pi = pixel[:4]
    val = pixel[4:]
    video_url = "www.youtube.com/watch?v=" + val
    try:
        obj = YouTube(video_url)
        obj.streams.filter(progressive=True, file_extension="mp4").get_by_resolution(pi).download(path)
        print("Video downloaded successfully")
    except Exception as e:
        print("An error occurred:", str(e))
    return render(request, "final.html")


