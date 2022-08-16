import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
from email.message import EmailMessage
'''
email_list= {
    
}
def send_email(receiver,subject,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login()
    email=EmailMessage()
    email['from']=''
    email['to']=receiver
    email['subject']=subject
    email.set_content(email_body)
    server.send_message(email)'''

    

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING SIR")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON SIR")
    else :
        speak("good evening")


    speak(" how may i help u   ")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("RECOGNIZING....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("sir i didnt get ya can u please repeat yourself")
        return "None "
    return query
if __name__ == "__main__":
    greeting()
    while True:
     query = takecommand().lower()

     if 'wikipedia' in query:
         speak('fetching resources from wikipedia..')
         query=query.replace("wikipedia","")
         results= wikipedia.summary(query,sentences=4)
         speak('according to resources')
         speak(results)


     elif 'open youtube' in query:
          webbrowser.open("youtube.com")
     elif 'open google ' in query:
         webbrowser.open("google.com")
     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
     elif'open facebook' in query:
         webbrowser.open("facebook.com")
     
     elif 'play music ' in  query:
         msuic_dir = 'E:\\songs'
         songs=os.listdir(msuic_dir)
         print(songs)
         os.startfile(os.path.join(msuic_dir,songs[0]))
     elif 'who are you alfred' in query:
          speak('i am alfred i was designed with the vision and mission of making life better ')
     elif 'initiate shutdown protocol' in query:
         speak('shutdown')
         os.system("shutdown /s /t 1")
     elif 'restart the system' in query:
         speak('initiating restart protocol')
         os.system("shutdown /r")
     elif 'initiate restart protocol'in query:
         speak('initiating restart protocol')
         os.system("shutdown /r")
     elif 'whats the time alfred ' in query:
         strtime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir the time is {strtime}")
     elif  'send an email ' in query:
         speak('initialising email protocol')
         speak('sir whom do u want to send this email too')
         name=takecommand()
         receiver=email_list[name]
         speak('sir what is the subject of this email')
         subject=takecommand()
         speak('sir what should i write in this email')
         email_body=takecommand()
         send_email(receiver,subject,email_body)



    