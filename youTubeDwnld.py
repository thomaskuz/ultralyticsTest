from pytubefix import YouTube
YouTube('https://www.youtube.com/watch?v=WvhYuDvH17I').streams.first().download()


'''
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.streams.filter(progressive=True, file_extension='mp4')
yt.streams.order_by('resolution')
yt.streams.desc()
yt.streams.first()
yt.streams.download()

'''
