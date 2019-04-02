import json
from watson_developer_cloud import ToneAnalyzerV3

# uses IBM Watson Tone Analyser API to identify the emotional tone of a block of text
def findTone(text):
    tone_analyzer = ToneAnalyzerV3(
            version ='2017-09-21',
            username ='Your Username Here',
            password ='Your Password Here'
            )
    
    content_type = 'application/json'
    
    tone = tone_analyzer.tone({"text": text},content_type)
    
    #print(json.dumps(tone, indent=1))
    #print(tone)
    try:
        print(tone['document_tone']['tones'][0])
        return(tone['document_tone']['tones'][0])
    except:
        ans = None
    
    # if no overall tone is found in the block of text, the text is split up into smaller sentences
    # the smaller sentences are then run through the API to identify the emotional tone
    try:
        l = []
        text = text.split('.')
        print(text)
        for i in text:
            try:
                tone = tone_analyzer.tone({"text": i},content_type)
                l.append(tone['document_tone']['tones'][0])
            except:
                l.append(None)
    except:
        # this runs if no tone can be found throughout the whole text
        ans = "No tone found"
    return l if not ans else ans
    

#print(findTone("One gloomy day, when the long afternoon shadows gave way to gray twilight, a band of baddies, green with greed, emerged. They were jealous of the friendship that Bella and the children shared. They snuck up on Bella, cut off the jewels with their sharp knives, then ran away into the deep dark night with bags full of Bella's jewels."))
