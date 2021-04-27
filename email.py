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
    server.login("sender_mail_id", "mail_password")
    print("Message for mail")
    talk("Message for mail")
    message = speechToText()
    print("Message: " + message)
    server.sendmail("sender_mail_id", "reciever_mail_id", message)
    talk('Sent')
    print('Sent')
    server.quit()

elif text.find("no") >= 0:
    talk("Gotcha!!! Loud and clear...")
    print("Gotcha!!! Loud and clear...")
    exit()
