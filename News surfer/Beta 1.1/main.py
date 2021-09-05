import requests
import os
from importlib import reload  

while True:
    value = input(".")
    if("bbs" in value):
        value2 = input("Enter news code:")
        e=open(r'bbs.py',"wb")
        rf = requests.get("https://timuruch.github.io/bbs/%s.py" % value2)
        e.write(rf.content)
        e.close()
        try:
            import bbs
            reload(bbs)
            os.remove("bbs.py")
        except SyntaxError:
            print("You wrote wrong password")
    elif(value == "about"):
        print("This program made by Timur Zenin")
        print("Version: Beta 1.0")
        print("Name: News surfer")
        print("Discribe: A program made for easy")
        print("access to news")
    elif(value == "active_servers"):
        a=open(r'active.py',"wb")
        r = requests.get("https://timuruch.github.io/active.py")
        a.write(r.content)
        a.close()
        try:
            import active
            reload(active)
            os.remove("active.py")
        except SyntaxError:
            print("No servers onine")
            print("Check your internet")
            print("Or author closed all servers")
    else:
        print("You wrote wrong program")
