# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 18:40:00 2018

@author: Jin
"""
import csv


f = open("toneonly.txt", "r")
texttones = [(i.strip(" \n")).split(", ") for i in f.readlines()]
print(texttones)
f.close()

#print(texttones)
#print(texttones[0][1])

tone = ['anger','fear','sadness','analytical','confident','tentative','joy']
emotion = ['Energetic','frantic','sad','calm','contentment','depression','happy + exuberant']
emotionlists = [[] for i in range(len(emotion))]
songnamelists = [[] for i in range(len(emotion))]
songlist = {}

# function to normalise all confidence scores 
def norm(x,maxx,minx):
    return ((x-minx)/(maxx-minx))


with open('Confidence_Level2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songlist[(row["Song Title"])] = (row["Predicted Mood"],float(row["Confidence_Level"]))


textscore = [float(i[2]) for i in texttones]
textscore = [norm(i,max(textscore),min(textscore)) for i in textscore]


for key,value in songlist.items():
    (emotionlists[emotion.index((value[0]))]).append(value[1])
    (songnamelists[emotion.index((value[0]))]).append(key)

normemotionlists =[]
for emotion in emotionlists:
    print(emotion)
    try:
        normemotion = [norm(i,max(emotion),min(emotion)) for i in emotion]
        normemotionlists.append(normemotion)
    except:
        normemotionlists.append([1])

previous1song = ''
previous2song = ''
previous3song = ''
for enum,i in enumerate(texttones):
    emote = emotion[tone.index(i[1])]
    emotionscorelist = normemotionlists[tone.index(i[1])]
    
    
    #songlist = eval(h.read())
  
    #print(songlist.values())
    closestscore = min((emotionscorelist), key=lambda x:abs(x-textscore[enum]))
    song = songnamelists[tone.index(i[1])][emotionscorelist.index(closestscore)]
    #print(song)
    if (previous2song == song):
        try:
            song = songnamelists[tone.index(i[1])][emotionscorelist.index(closestscore)+2]
        except:
            song = songnamelists[tone.index(i[1])][emotionscorelist.index(closestscore)+1]
    if (previous1song == song or previous2song == song):
        song = songnamelists[tone.index(i[1])][emotionscorelist.index(closestscore)+1]
    previous2song = previous1song
    previous1song = song
    print(song)
    #print(closestscore)
    #song = (list(songlist.keys())[list(songlist.values()).index(closestscore)])

    
    
    
'''   
    g = open("tonemusic.txt", 'a')
    g.write("{},{}".format(enum+1,song))
'''    