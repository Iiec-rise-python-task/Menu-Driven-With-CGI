import speech_recognition as sr
import pyttsx3
import webbrowser
engine=pyttsx3.init()
i='a'
r1=sr.Recognizer()
r1.energy_threshold=10000
while i!='c':
    engine.say("hello sir")
    engine.runAndWait()
    print("hello sir")
    with sr.Microphone() as source:
        engine.say("what do you want me to run sir")
        engine.runAndWait()
        print("what do you want me to run sir")
        audio=r1.listen(source)
    data=r1.recognize_google(audio)
    data=data.lower()
    print(data)
    r=''
    if ('calendar' or 'cal' or 'month' or 'year' )in data:
        r='cal'
    elif 'date' in data:
        r='date'
    elif 'files' in data:
        r='ls'
    elif 'keywords' in data:
        r='compgen -c'
    elif 'ip' in data:
        r='ifconfig'
    elif 'weather' in data:
        webbrowser.open('https://www.msn.com/en-in/weather')
        i=input()
        continue
    elif ('google' or 'info') in data:
        webbrowser.open('https://www.google.com')
        i=input()
        continue
    elif ('youtube' or 'video') in data:
        webbrowser.open('https://youtube.com')
        i=input()
        continue
    elif ('fast' or 'ping' or 'net speed' or 'speed') in data:
        webbrowser.open('https://www.fast.com')
        i=input()
        continue
    elif ('music' or 'song' or 'listen')  in data:
        webbrowser.open('https://www.spotify.com')
        i=input()
        continue
    elif ('locate' or 'map' or 'location' or 'nearby') in data:
        webbrowser.open('https://www.google.co.in/maps')
        i=input()
        continue
    elif ('address' or 'mac address')in data:
        webbrowser.open('https://whatismyipaddress.com')
        i=input()
        continue
    elif ('score' or 'ipl' or 'match') in data:
        webbrowser.open('https://www.espncricinfo.com/series/_/id/8048/season/2020/indian-premier-league')
        i=input()
        continue
    else:
        print(r)
        i=input()
        continue
    print(r)
    c='http://192.168.43.178/cgi-bin/hello.py?n={0}'.format(r)
    webbrowser.open(c)
    i=input()