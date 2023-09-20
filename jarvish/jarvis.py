import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import keyboard
import pyjokes
import openai
import webbrowser
from apikey import api_data
import datetime
from playsound import playsound
from  googletrans import Translator
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import PyPDF2


# from PyDictonary import PyDictonary as dict

from dotenv import load_dotenv


openai.api_key=api_data
load_dotenv()
completion=openai.Completion()


def Reply(question,chat_log=None):
    FileLog =open("chat_log.txt","r")
    chat_log_template= FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log= chat_log_template
    prompt= f'{chat_log}You:{question}\nJarvise:'
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\You'], max_tokens=1000)
    answer=response.choices[0].text.strip()
    chat_log_template_update= chat_log_template + f"\nYou : {question} \nJarvise :{answer}"
    FileLog= open("chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
reply=Reply("hello how are you?")
print(reply)

assistent = pyttsx3.init("sapi5")
voices= assistent.getProperty('voices')
print(voices)
assistent.setProperty('voices',voices[0].id)
assistent.setProperty('rate',150)
def speak(audio):
    print("     ")
    assistent.say(audio)
    print(f": {audio}   ")
    print("       ")
    assistent.runAndWait()

def takecommand():
    command= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.............")
        command.pause_thersold= 1
        audio = command.listen(source)
        try:
            print("Recognizing.............")
            query= command.recognize_google(audio,language='en-in')
            print(f"You said : {query}")
        except Exception as Error:
            return "none"
        return query.lower()
    
    

    
    

    
    
def taskexe():
    
    
    def takehindi():
        command= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listining.............")
            command.pause_thersold= 1
            audio = command.listen(source)
        
        
            try:
                print("Recognizing.............")
                query= command.recognize_google(audio,language='hi')
                print(f"You said : {query}")
            except Exception as Error:
                return "none"
            return query.lower()
    
    
    
    
    
    
    def tran():
        speak("tell me the line")
        line = takehindi()
        traslate = Translator()
        result = traslate.translate(line, dest="en")
        
        speak(result.text)
    
    
    def music():
        speak("tell me the name of the music")
        musicname= takecommand()
        if 'Ram Bhajan Kar Man' in musicname:
            os.startfile('Music')
        else:
            pywhatkit.playonyt(musicname)
        speak("Your song has been started!......, Enjoy sir")
    
    def whatsapp():
        speak("tell me the name of the person")
        name= takecommand()
        if 'Bharat Patel' in name:
            speak("sir tell me the messege!")
            msg=takecommand()
            speak("tell me the timre sir")
            speak("time in hour")
            hour =int(takecommand())
            speak("time in minutes")
            minute= int(takecommand())
            pywhatkit.sendwhatmsg("+918429267680",msg,hour,minute,20)
            speak("ok sir, sending whatsapp messege!")
        else:
            speak("tell me the number")
            phone = int(takecommand())
            speak("sir tell me the messege!")
            msg=takecommand()
            speak("tell me the timre sir")
            speak("time in hour")
            hour =int(takecommand())
            speak("time in minutes")
            minute= int(takecommand())
            pywhatkit.sendwhatmsg(phone,msg,hour,minute,20)
            speak("ok sir, sending whatsapp messege!")
            
    def openapps():
        speak("ok sir wait s second")
        if 'code' in query:
            os.startfile("C:\\Users\abhib\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            
        elif 'OBS studio' in query:
            os.startfile("C:\\Program Files\obs-studio\bin\64bit\obs64.exe")
        
                
        
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("youtube is opened")
        
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("instagram is opened")
        
        elif 'chrome' in query:
            webbrowser.open("https://www.chrome.com")
            speak("chrome is opened")
        elif 'xampp' in query:
            os.startfile("C:\\xampp")
            speak("xampp is opened")
        speak("i hope it is helpfull for you sir.............!")
    
    def closeapp():
        speak("ok sir wait a second")
        
        if 'close code' in query:
            os.system("TASKKILL /F /in opencode.exe")
        elif 'close OBS studio' in query:
            os.system("TASKKILL /F /in obs_studio.exe")
        elif ' close youtube' in query:
            os.system("TASKKILL /F /in youtube.exe")
        elif 'close instagram' in query:
            os.system("TASKKILL /F /in instagram.exe")
        elif 'close chrome' in query:
            os.system("TASKKILL /F /in chrome.exe")
        elif 'close xampp' in query:
            os.system("TASKKILL /F /in xampp.exe")
        speak("app closed")
    
    def youtubeauto():
        speak("please tell me command ?")
        comm=takecommand()
        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'restart' in comm:
            keyboard.press('0') 
        elif 'mute' in comm:
            keyboard.press('m') 
        elif 'skipp' in comm:
            keyboard.press('l') 
        elif 'back' in comm:
            keyboard.press('j') 
        elif 'full screenmode' in comm:
            keyboard.press('f') 
        elif 'filmmode' in comm:
            keyboard.press('t') 
        speak("done sir")
  
    def chromeautomate():
        speak("chrome automation")
        command=takecommand()
        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')
        elif 'download' in command:
            keyboard.press_and_release('ctrl + j')
   
    def dict():
        speak("activated dictionary")
        prob=takecommand()

        if 'meaning' in prob:
            prob= prob.replace("what is this","")
            prob= prob.replace("of","")
            prob= prob.replace("meaning","")
            result= dict.meaning(prob)
            speak(f"the meaning for {prob} is {result}")
        elif 'synonym' in prob:
            prob= prob.replace("what is the ","")
            prob= prob.replace("of","")
            prob= prob.replace("synonym","")
            result= dict.synonym(prob)
            speak(f"the synonym for {prob} is {result}")
        elif 'antonym' in prob:
            prob= prob.replace("what is the ","")
            prob= prob.replace("of","")
            prob= prob.replace("antonym","")
            result= dict.synonym(prob)
            speak(f"the antonym for {prob} is {result}")
  
    def screenshot():
            speak("ok boss what should i name that file")
            path=takecommand()
            path1name= path + ".png"
            path1= "C:\\Users\\abhib\\OneDrive\\Pictures\\Screenshots\\" + path1name
            kk= pyautogui.screenshot()
            kk.save(path1)
            os.startfile("C:\\Users\\abhib\\OneDrive\\Pictures\\Screenshots\\")
            speak("here is your screenshot sir")      
    
    
    def temp():
        # search ="temperature in jalaun"
        url= f"https://www.google.com/search?q={query}"
        r= requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp =data.find("div",class_="BNeawe").text
        speak(f"{query} is {temp}")
    
    
    def reader():
        speak("tell me the name the book")     

        name =takecommand()
        
        
        if 'india' in name:
            
            os.startfile('final project report on effect of dyes on different types of fabrics.pdf')
            book =open('final project report on effect of dyes on different types of fabrics.pdf','rb')
            pdfreader= PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"number of the pages in this book are {pages}")
            speak("from which page i have to start reading?")
            numPage= int(input("enter the page number"))
            page= pdfreader.getPage(numPage)
            text = page.extractText()
            speak("in which language, i have to read ?")
            lang= takecommand()

            if 'hindi' in lang:
                transl =Translator()
                textHin =transl.translate(text,'hi')
                textm= textHin.text
                speech=gTTS(text=textm)
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                except:
                    playsound('book.mp3')
            else:
                speak(text)



    while True:

        query=  takecommand()
        if 'hello' in query:
            speak("hello, sir I am jarvise")
            speak("your persoal assistant how can i help you")
        elif 'how are you' in query:
            speak("I am fine what about you sir")
        elif 'you need a break jarvise' in query:
            speak("ok sir you may call me at any time")
            break
        elif 'kya hal hai' in query:
            speak("Mai accha hu sir bs ldki dilwa dijiye")
        elif 'bye' in query:
            speak("bye sir ")
            break
        elif 'youtube search' in query:
            speak("ok sir , This is what i found for your search")
            query= query.replace("jarvise", "")
            query= query.replace("youtube search", "")
            web='https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir!")
        
                
        elif 'website' in query:
            speak("ok sir , This is what i found for your search")
            query= query.replace("jarvise", "")
            query= query.replace("website", "")
            query = query.replace("open","")
            web2 ='https://www' + query + '.com'
            webbrowser.open(web2)
            speak("launched sir!...........")          
        elif 'launch' in query:
            speak("tell me the name of the website")
            name =takecommand()
            web ='http://www.' + name + '.com'
            webbrowser.open(web)
            speak("done sir!...........")
        elif 'music' in query:
            music()
        elif 'wikipedia' in query:
            speak("your wikipedia search is here sir!")
            query= query.replace("jarvise","")
            query= query.replace("wikipedia","")
            query= query.replace("search","")
            wiki = wikipedia.summary(query,222)
            speak(f"according to wikipedia: {wiki}")
        elif 'Whatsapp message' in query:
            whatsapp()
          
        elif 'open code' in query:
            openapps()
        elif 'open OBS studio' in query:
            openapps()
        elif 'open youtube' in query:
            openapps()
        elif 'open instagram' in query:
            openapps()
        elif 'open chrome' in query:
            openapps()
        elif 'open xampp' in query:
            openapps()
        elif 'close code' in query:
            closeapp()
        elif 'close OBS studio' in query:
            closeapp()
        elif ' close youtube' in query:
            closeapp()
        elif 'close instagram' in query:
            closeapp()
        elif 'close chrome' in query:
            closeapp()
        elif 'close xampp' in query:
            closeapp()
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0') 
        elif 'mute' in query:
            keyboard.press('m') 
        elif 'skipp' in query:
            keyboard.press('l') 
        elif 'back' in query:
            keyboard.press('j') 
        elif 'full screenmode' in query:
            keyboard.press('f') 
        elif 'filmmode' in query:    
            keyboard.press('t') 
        elif 'youtube tool' in query:
            Youtubeauto()
        elif 'internet portal' in query:
            web='http://172.16.1.1:8090/httpclient.html'
            webbrowser.open(web)
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')
        elif 'chrome automation' in query:
            chromeautomate()
        elif 'joke' in query:
            get =pyjokes.get_joke()
            speak(get)
        elif 'repeat my word' in query:
            speak("speak sir")
            jj=takecommand()
            speak(f"you said : {jj}")
        elif 'my location' in query:
            speak("ok sir wait a second")
            webbrowser.open('https://www.google.com/maps/place/Mahotara,+Uttar+Pradesh+210201/@25.3125035,80.5451454,14z/data=!3m1!4b1!4m5!3m4!1s0x39834c60018cb84d:0x5673c9ff84f4a15f!8m2!3d25.3098642!4d80.5688428')
        elif 'dictonary' in query:
            dict()
        elif 'screenshot' in query:
            screenshot()
        elif 'alarm' in query:
            speak("tell me the time")
            time =input(" : enter the time : ")
            while True:
                Time_Ac =datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                
                if now == time:
                    speak("time to wake up sir")
                    playsound('alarm.mp3')
                    speak("Alarm closed!")
                elif now>time:
                    break
        elif 'translator' in query:
            tran()
        elif 'remember that' in query:
            query= query.replace("remember that","")
            query = query.replace("jarvise","")
            speak("you tell me to remind me that:"+query)
            full_file=open('remember.txt','r')
            full_file_log=full_file.read()
            full_file.close()
            remember =open('latest_remember.txt','w')
            full_file=open('remember.txt','w')
            # full_file_log.write(query)
            remember.write(query)
            full_file.write(query)
    
            # full_file_log=full_file.read()
           
            
            full_file.close()
            remember.close()




        
        
        elif 'what do you remember' in query:
            remember =open('latest_remember.txt','r')
            speak("you tell me that "+ remember.read())
        
        elif 'tell me all the things you remember' in query:
            full_file =open('remember.txt','r')
            speak("you tell me that "+ full_file.read())
            
        elif 'google search' in query:  
            import wikipedia as googleScrap
            query= query.replace("jarvise","")
            query= query.replace("google search","")
            query= query.replace("google","")
            speak("this is what i found for you sir")
            
            try:
                pywhatkit.search(query)
                result= googleScrap.summary(query,3)
                speak(result)

            except:
                speak("no speakable data Availbale")
        
        
        elif 'temperature' in query:
            temp()
                
        elif 'reader' in query:
            reader()
            
            
        
        else:
            ans=Reply(query)
            print(ans)
            speak(ans)
taskexe()



