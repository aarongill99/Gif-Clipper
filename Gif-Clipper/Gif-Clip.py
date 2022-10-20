#using python to get the initial prototype working
import pysrt
from re import search
subs = pysrt.open('2_English.srt')
substring = "job"

#print(subs[0])
for sub in subs:
    if search(substring,sub.text):
        print(sub.text)
        print("\nStart Time: " + str(sub.start.minutes) + ":" + str(sub.start.seconds) + "," + str(sub.start.milliseconds))
        print("End Time: " + str(sub.end.minutes) + ":" + str(sub.end.seconds) + "," + str(sub.end.milliseconds) +"\n")
        #print(sub.start.milliseconds)
        #print(sub.end.minutes)
        #print(sub.end.seconds)
        #print(sub.end.milliseconds)
