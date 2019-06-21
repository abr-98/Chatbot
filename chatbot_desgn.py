from gtts import gTTS
import re
import pyaudio
import wave
import speech_recognition as sr
import os
import string
import nltk
import random
import numpy as np
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from googlesearch import search
import webbrowser
from nltk.tokenize import word_tokenize
import pafy
#from weather import Weather,Unit

know=0
'''responses=
{
	"what's your name?":["my name is echobot","they call me echobot","the name's Bot,Echo Bot"]
	"what's the weather today?":"Its {} today"
    "hello":["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]
    "hi":["hi", "hey","hi there", "hello", "I am glad! You are talking to me"]
    "hey":["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]
    "hi there":["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]

}
responses_dont=["i am unaware,tell me more","i dont know,let me learn"]
'''

     
def swap_pronouns(phrase):
	if 'I' in phrase:
		return re.sub('I','you',phrase)
	if 'my' in phrase:
		return re.sub('my','your',phrase)
	else:
		return phrase


def response(message):
    global know
    pattern_1="do you remember(.*)"
    match=re.search(pattern_1,message)
    if match!=None:
        mssage=message.replace('do ','will ')
        msg=match.group(1)
        res=swap_pronouns(mssage)
        print("I do")
        print(res)
        text=open("record.txt","a")
        text.write(res)

    responses={
	    "what's your name?":["my name is echobot","they call me echobot","the name's Bot,Echo Bot"],
        #"how is the weather?":"Its a sunny day",
        "hello":["hi", "hey","hi there", "hello", "I am glad! You are talking to me"],
        "hi":["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"],
        "hey":["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"],
        "hi there":["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"],
        "thanks":['you are welcome','happy to help'],
        'thank you':['you are welcome','happy to help']

    }
    responses_dont=["i am unaware,tell me more","i dont know,let me learn"]
    if re.search(r"\b(i am)\b",message) is not None:
        msg=re.search(r"\b(i am)\b",message).group(1)
        text=open("record.txt","a")
        know=0
        text.write("your name is"+(message)+"\n")
        res="Nice to meet you,MR X this side"
     
    elif re.search(r"\b(booking|book)\b",message) is not None:
        text=open("booking.txt","a")
        if "hotel" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify the palce where you want to book")
            detail_place=input()
            print("can u please specify the on the date of stay")
            detail_date=input()
            msg="hotel booking at "+str(detail_place)+" on "+str(detail_date)
            url=ext+msg
            text.write(msg)
            text.close()
            webbrowser.open(url,new=1)
            res="Here are the options"
        elif "bus" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify your destination")
            detail_dest=input()
            print("Can u please specify your source")
            detail_source=input()
            print("can u please specify the on the date of journey")
            detail_date=input()
            print("can u please approx time of journey")

            detail_time=input()
            print("AC or NON AC")
            choice=input()
            msg=choice+ " bus booking from "+str(detail_source)+" to "+str(detail_dest)+" on "+str(detail_date)+" at "+str(detail_time)
            url=ext+msg
            text.write(msg)
            text.close()
            webbrowser.open(url,new=1)
            res="Here are the options"
        elif "train" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify your destination")
            detail_dest=input()
            print("Can u please specify your source")
            detail_source=input()
            print("can u please specify the on the date of journey")
            detail_date=input()
            print("can u please approx time of journey")

            detail_time=input()
            print("AC or NON AC")
            choice=input()
            msg=choice+ " train booking from "+str(detail_source)+" to "+str(detail_dest)+" on "+str(detail_date)+" at "+str(detail_time)
            url=ext+msg
            text.write(msg)
            text.close()
            webbrowser.open(url,new=1)
            res="Here are the options"
        elif "flight" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify your destination")
            detail_dest=input()
            print("Can u please specify your source")
            detail_source=input()
            print("can u please specify the on the date of journey")
            detail_date=input()
            print("can u please approx time of journey")

            detail_time=input()
            print("Choice of Flight Service")
            choice=input()
            msg=choice+ " flight booking from "+str(detail_source)+" to "+str(detail_dest)+" on "+str(detail_date)+" at "+str(detail_time)
            url=ext+msg
            text.write(msg)
            text.close()
            webbrowser.open(url,new=1)
            res="Here are the options"
        elif "movie" in message:
            ext="https://www.google.com/search?q="
            print("Can u please tell the movie")
            detail_movie=input()
            print("Can u please specify the timing")
            detail_timing=input()
            print("can u please specify the region or city")
            detail_region=input()
            #print("can u please approx time of journey")

           # detail_time=input()
            #print("Choice of Flight Service")
            #choice=input()
            msg=detail_movie+" movie booking at "+str(detail_timing)+" in "+str(detail_region)
            url=ext+msg
            text.write(msg)
            text.close()
            webbrowser.open(url,new=1)
            res="Here are the options"
        else:
            res="I dont properly understand but i will try to help"
            ext="https://www.google.com/search?q="
            url=ext+message
            webbrowser.open(url,new=1)

    elif re.search(r"\b(play|playing)\b",message) is not None:

        text=open("playlist.txt","a")
        result=re.search(r"\b(play(.*)|playing(.*))",message).group(0)
        ext="https://www.youtube.com/results?search_query="
       # msg=ext+result
        messg=result.replace(" ","+")
        #url = "http://www.youtube.com/watch?v=cyMHZVT91Dw"
        
        text.write(messg)
        text.close()
       # print(messg)
        msg=ext+messg
        
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 3)
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        
        # Navigate to url with video being appended to search_query
        driver.get(msg)

        # play the video
        wait.until(visible((By.ID, "video-title")))
       # player=driver.find_element_by_id("video-title")
        driver.find_element_by_id("video-title").click()
        url = driver.current_url
        #print(url)
        time_prev= int(round(time.time()))
        video=pafy.new(url)
        l=video.length
        #time_now=int(round(time.time()))
        boo=True
        while boo:
            time_now=int(round(time.time()))
            if time_now-time_prev==int(l+2):
                driver.quit()
                boo=False


        #print(l)
        #x=driver.find_element_by_id("video-title").getAttribute("ended")
        #print(x)
        res="Here you go"
    elif know==1 and re.search(r"\b(i|my|he|hi s|we|our|they|their|its|it is)\b",message) is not None :
        res="Thank you,I will remember"
        text=open("record.txt","a")
        know=0
        text.write(swap_pronouns(message)+"\n")
 
        text.close()
    elif re.search(r"\b(what's|what)\b",message) is not None and 'time' in message:
        res="Its "+str(datetime.datetime.now())
        know=0
    elif re.search(r"\b(how)\b",message) is not None and 'weather' in message:
        res="here you go"
        know=0
        webbrowser.open("https://www.google.com/search?q=weather",new=1)
    elif message in responses:
        know=0
        res=random.choice(responses[message])
    else:
        if re.search(r"\b(which|who|what|how|when)\b",message.split(" ")[0]) is not None:
            res=random.choice(responses_dont)
            text=open("record.txt","a")
            know=1
            text.write(message+"\n")

            text.close()
        else:
            res="sorry, i dont understand you but here is some matching searches"
            ext="https://www.google.com/search?q="
            msg=message.replace(" ","+")
            #webbrowser.open(msg,new=1)
            url=ext+msg
            webbrowser.open(url,new=1)

            know=0


    print(res)
    #myobj = gTTS(text=res, lang='en', slow=False)
    #myobj.save("respond.mp3")
   # os.system("mpg321 respond.mp3")
    #os.remove("respond.mp3")
    return res

def send_message(message):
	response(message)

def main():
    flag=True
  #  lan
    print("If you want to exit, type Bye!")
    text=open("record.txt","w")
    text.close()
    text=open("booking.txt","w")
    text.close()
    text=open("playlist.txt","w")
    text.close()
    text=open("choice.txt","w")
    text.close()
    text="If you want to exit, type Bye!"
   # myobj = gTTS(text=text, lang='en', slow=False)
    #myobj.save("respond.mp3")
    #os.system("mpg321 respond.mp3")
    #os.remove("respond.mp3")

    while(flag==True):
        user_response = input()
        user_response=user_response.lower()
        if(user_response!='bye'):
            #if(user_response=='thanks' or user_response=='thank you' ):
             #flag=False
            send_message(user_response)
        else:
            flag=False
            print(" Bye! take care..")
            text="Bye! take care"
        #    myobj = gTTS(text=text, lang='en', slow=False)
       #     myobj.save("respond.mp3")
         #   os.system("mpg321 respond.mp3")
          #  os.remove("respond.mp3")

main()