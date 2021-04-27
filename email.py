import smtplib as sm
import speech_recognition as sr
import pyttsx3 as pyt

def talk(str):
    v1 = pyt.init()
    v1.say(str)
    v1.runAndWait()

def speechToText():
    v1 = sr.Recognizer()
    with sr.Microphone() as source:
        talk("Speak")
        print('Speak')
        v1.adjust_for_ambient_noise(source)
        text = v1.recognize_google(v1.listen(source)).lower()
    return text

talk('Email by ADI Assistant Wanna Send Mail(Yes or No)')
print('Email by ADI Assistant\nWanna Send Mail(Yes or No)')
text = speechToText()
if text.find("yes") >= 0:
    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("adi.assistant260421@gmail.com", "adiaiassistant260421")
    print("Message for mail")
    talk("Message for mail")
    message = speechToText()
    print(message)
    # talk("Send Email to what address")
    # print("Send Email to what address")
    # address = speechToText()
    server.sendmail("adi.assistant260421@gmail.com", "1905223@kiit.ac.in", message)
    talk('Sent')
    print('Sent')
    server.quit()

elif text.find("no") >= 0:
    talk("Gotcha!!! Loud and clear...")
    print("Gotcha!!! Loud and clear...")
    exit()