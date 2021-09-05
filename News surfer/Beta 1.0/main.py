import requests

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
        except SyntaxError:
            print("You wrote wrong password")
    elif(value == "about"):
        print("This program made by Timur Zenin")
        print("Version: Beta 1.0")
        print("Name: News surfer")
        print("Discribe: A program made for easy")
        print("access to news")
