import wget
import os
import pytube

print('''
                            _
                           | |
  ___ _ __   ___  ___ _   _| |_   _ _ __ ___
 / __| '_ \ / _ \/ __| | | | | | | | '_ ` _ \
 \__ \ |_) |  __/ (__| |_| | | |_| | | | | | |
 |___/ .__/ \___|\___|\__,_|_|\__,_|_| |_| |_|
     | |
     |_|

Making deepfakes as easy as 123, ABC, you and me!

Ingredients:
- url to a photo to animate
- url to youtube video to animate the photo to do
- a big idea (at least one cup)

Directions:
Just follow the instructions on screen, input your video
and grab it out when it tells you to.
''')
image = input("Drop URL to source image: ")
video = input("Drop YT URL to driving video: ")
wget.download(image, 'image.jpg')
pytube.YouTube(video).streams.get_highest_resolution().download()
os.system("deep_animate", image, video, "conf.yaml deep_animator_model.pth.tar")
print('''Your video is now saved to the folder with the code, process complete
go to replit with the 'open in replit' button, then download the video file it created
''')
