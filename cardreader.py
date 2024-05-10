#Designed and developed by: Ibrahim Shehadeh
#Created on: 10-may-2024
#Desc: 
 #Prompts the user to select the anki exported .txt file and converts the card titles to an array.
#Github repo:
    #https://github.com/TheHeisenBurglar/AnkiArray

#Imports 
from tkinter import *
import re
from tkinter import filedialog

#Variables
text = "empty"
ready = False
towrite = []
#Functions
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    string = (filename)
    return string
def extractJapaneseText(textline):
    txt = ""
    japanese_pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3000-\u303F]')
    if "font-size: 50px;" in textline:
        for char in textline:
            if(japanese_pattern.search(char)):
                txt += char
        if(txt != ""):
            return txt
        else:
            return 
def toFile(toappend, array):
    array.append(word)

#Logic
text = browseFiles()      
print(text) 
file = open(text, "r")   
if text:
    with open(text, "r", encoding="utf-8") as file:
        for line in file:
            word = extractJapaneseText(line)
            if word:
                toFile(word, towrite)
print("array: ", towrite)
file.close() 
