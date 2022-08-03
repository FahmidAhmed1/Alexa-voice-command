import speech_recognition as sr # we are importing a speech recognizor and naming it "sr"
import pyttsx3 #import text to speech for her voice
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() #creating a recognizer to regognize my voice
engine = pyttsx3.init()

def talk(text): #creating a function where it will say the text
    engine.say(text)
    engine.runAndWait()
def take_command():
        try: #creating a try block
            with sr.Microphone() as source:   #using microphone as a source
                  print('listening...')
                  voice = listener.listen(source) #create a variable to capture the audio from the source
                  command = listener.recognize_google(voice) #creating a variable that uses the goggle API to convert voice to text
                  command = command.lower()
                  if 'alexa' in command:
                      command = command.replace('alexa', '') #when seaching on the web for song, we don't want the word "alexa" in search so we are removing it from the string
                      print(command)       #repeating the command or what you tell
        except:
           pass
        return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song) #calls the python libary which takes the name of the song and types it into goggle
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') #if it hears "time" it will use %I as the 12 hour format and get the minitues and pm or am and display and project it
        print(time)
        talk('The current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
 #  elif 'look' in command:
     #   talk('what is your name')
          #  Name= take_command()
           #  talk(Name + 'you have never looked better')
    else:
        talk('please repeat your statement dear. Alexa could not understand it. Sorry ') 

run_alexa()