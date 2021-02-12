import ctypes
import json
import os.path
import webbrowser

from infi.systray import SysTrayIcon


class Call:

    def __init__(self, url):
        self.url = url

    def __call__(self, a):
        print("Opening URl: " + self.url)
        webbrowser.get(chrome_path).open(self.url)


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

if not os.path.isfile(chrome_path):
    ctypes.windll.user32.MessageBoxW(0, "Chrome wurde auf diesem System nicht gefunden! Short-Build wird geschlossen!",
                                     "Fehler", 0)
    exit(0)

# Wird hinzugefügt
chrome_path = chrome_path + " %s"

menu_options = ()

with open('config.json') as json_file:
    data = json.load(json_file)

    for entry in data["links"]:
        name = entry['name']
        url = entry['url']
        menu_options = menu_options + ((name, None, Call(url)),)

systray = SysTrayIcon("icon.ico", "Jenkins Shortcuts", menu_options)
systray.start()
