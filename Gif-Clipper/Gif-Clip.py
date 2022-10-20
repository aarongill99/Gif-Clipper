#using python to get the initial prototype working
import pysrt
from re import search
from moviepy.editor import *
clip = VideoFileClip("G:\Downloads\TV and Movies\Silicon.Valley.S02.1080p.BluRay.x265-RARBG\Silicon.Valley.S02E01.1080p.BluRay.x265-RARBG.mp4")
subs = pysrt.open('2_English.srt')
substring = "damn"

i=0
#print(subs[0])
for sub in subs:
    if search(substring,sub.text):
        startSec = sub.start.minutes*60  + sub.start.seconds
        endSec = sub.end.minutes*60  + sub.end.seconds + 0.5
        txt_clip = TextClip(sub.text, fontsize = 20, color = 'white')
        txt_clip = txt_clip.set_pos('bottom').set_duration(endSec-startSec) 
        print("\nStart Time in seconds: " + str(startSec))
        print("\nEnd Time in seconds: " + str(endSec))
        if(i < 2):
            clipx = clip.subclip(startSec,endSec).resize(0.3)
            video = CompositeVideoClip([clipx, txt_clip]) 

        if(i == 0):
            clip1 = video
            clip1.write_gif("clip.gif")
            i+=1
        elif(i == 1):
            clip2 = video
            clip2.write_gif("clip2.gif")


        #print(sub.start.milliseconds)
        #print(sub.end.minutes)
        #print(sub.end.seconds)
        #print(sub.end.milliseconds)

