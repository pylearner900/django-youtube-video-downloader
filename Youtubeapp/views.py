from django.shortcuts import render
from pytubefix import YouTube
from pytubefix.cli import on_progress

def Index(request):
    
    if request.method == 'POST': 
        link = request.POST['link'] 
        yt = YouTube(link, on_progress_callback = on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download()
    return render(request,'Youtubeapp/index.html')