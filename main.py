from youtubesearchpython import SearchVideos
import json
import webbrowser
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
from selenium import webdriver
num = 1

def speaks(output):
    global num
    num += 1
    print(output)
    Speak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3"
    Speak.save(file)
    playsound.playsound(file, True)
    os.remove(file)


def process_text(input):
    search = SearchVideos(input, offset=1, mode="json", max_results=20)
    data = json.loads(search.result())
    data2 = data["search_result"]
    url = data2[0]['link']
    #webbrowser.open_new(url)
    if input=='close':
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[0])
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        browser.get("https://google.com")
    else:
        browser.get(url)



def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")
    try:
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:
        return 0




flag=False
chromedriver = r"C:\Users\Inception\Downloads\Compressed\chromedriver_win32\chromedriver.exe"
browser= webdriver.Chrome(chromedriver)

while (1):
    if flag==False:
        speaks("what song play for you?")
        flag=True
    else:
        speaks("another song?")
    text = get_audio().lower()
    if text == 0:
        continue
    if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text) or "no" in str(text):
        speaks("Ok bye, ")
        break
    process_text(text)

print("Shahidul Salim Shakib\nCSE,KUET\nshahidulshakib034@gmail.com")

