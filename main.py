import speech_recognition as sr
import webbrowser as wb


def speechToText():
    v1 = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            text = v1.recognize_google(v1.listen(source)).lower()
        except sr.UnknownValueError:
            print('Error: Unclear Pronounciation\nTry Again in a bit')
            exit()
        except sr.RequestError:
            print('Error: Network Issue\nTry Again in a bit')
            exit()
    return text


print('Say something to search!\nLike --> "Search Dinosaurs"')
text = speechToText()
print(text)
index = text.find("search ")
if index == -1:
    print('Wanna search: YES or NO')
    text = speechToText()
    print(text)
    if text.find("no") >= 0:
        exit()
    elif text.find("yes") >= 0:
        print('Try Searching!!!')
        text = speechToText()
        print(text)
    else:
        print('Man u can\'t even speak correct\n\t  GO FUCK OFF!!!')
        exit()

index = text.find("search ")
if index == -1:
    print('Man u wasting my time\nTry again later')
    exit()

text = text[index + 7:]
url = 'https://www.google.com/search?q='
print("Search Query: " + text)
wb.open(url + text)