import random, time, winsound, speech_recognition as sr
from playsound import playsound

r = sr.Recognizer()
'''
with sr.Microphone() as source:
    print('Speak Anything : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
        if "Vader" in text:
            winsound.PlaySound("Yes my master".format(text), winsound.SND_FILENAME)
        elif "choke" in text:
            winsound.PlaySound("As you wish".format(text), winsound.SND_FILENAME)
        else:
            print("Sorry couldn't recognize your voice")    
    except:
        print("Sorry couldn't recognize your voice")
'''
breathing_cycle = 0
while breathing_cycle < 10:
     breathing_cycle += 1
     trigger = random.randint(0,5)
     if trigger == 4:
         playsound("sounds/Breath.wav")
         print("It works")
         time.sleep(2)

    