####################Imports#####################
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Toplevel
from tkinter import *
import pyperclip 
##################Characters####################
characters = [["Zero Width Space","\u200b"],["Hair Width Space", "\u200a"],["Zero Width No-Break Space", "\ufeff"],["Zero Width Non-Joiner", "\u200c"],["Zero Width Joiner", "\u200d"],
              ["Soft Hyphen", "\u00ad"],["Combining Grapheme Joiner", "\u034f"],["Mongolian Vowel Separator","\u180e"],["Left-To-Right Mark","\u200e"],["Right-To-Left Mark","\u200f"],
              ["Left-To-Right Embedding","\u202a"],["Right-To-Left Embedding","\u202b"],["Pop Directional Formatting","\u202c"],["Left-To-Right Override","\u202d"],
              ["Right-To-Left Override","\u202e"],["Word Joiner","\u2060"],["Inhibit Symmetric Swapping", "\u206a"]]
replacements = [["a","\u200b"],["b","\ufeff"],["c","\u200c"],["d","\u200d"],["e","\u00ad"],["f","\u034f"],["1","\u180e"],["2","\u200e"],["3","\u200f"],["4","\u202a"],["5","\u202b"],
         ["6","\u202c"],["7","\u202d"],["8","\u202e"],["9","\u2060"],["0","\u206a"]]
##################Functions#####################
def insert_zws(characters):
    text_box.insert(tk.INSERT, characters[0][1])
def insert_hs(characters):
    text_box.insert(tk.INSERT, characters[1][1])
def insert_zwnbs(characters):
    text_box.insert(tk.INSERT, characters[2][1])
def insert_zwnj(characters):
    text_box.insert(tk.INSERT, characters[3][1])
def insert_zwj(characters):
    text_box.insert(tk.INSERT, characters[4][1])

def findInvisibleCharacters(characters):
    text = text_box.get("1.0","end-1c")
    count = 0
    for i in range(len(characters)):
        text = text.replace(characters[count][1],("["+characters[count][0]+"]"))
        count+=1
    text_box.delete("1.0","end")
    text_box.insert(tk.INSERT, text)

def hideInvisibleCharacters(characters):
    text = text_box.get("1.0","end-1c")
    count = 0
    for i in range(len(characters)):
        text = text.replace(("["+characters[count][0]+"]"),characters[count][1])
        count+=1
    text_box.delete("1.0","end")
    text_box.insert(tk.INSERT, text)

def convertToUnicode():
    text = text_box.get("1.0","end-1c")
    newtext = ""
    for i in text:
        newletter=hex(ord(i))
        newletter = newletter[2:]
        while len(newletter) < 4:
            newletter = "0"+newletter
        newtext += newletter
    text_box.delete("1.0","end")
    text_box.insert(tk.INSERT, newtext)
    
def convertFully():
    convertToUnicode()
    text = text_box.get("1.0","end-1c")
    count = 0
    for i in range(len(replacements)):
        text = text.replace(replacements[count][0],replacements[count][1])
        count+=1
    text_box.delete("1.0","end")
    text_box.insert(tk.INSERT, text)

def copyText():
    text = text_box.get("1.0","end-1c")
    pyperclip.copy(text)

def countChars():
    text = text_box.get("1.0","end-1c")
    length = len(text)
    mainWindow.setvar(name = "charCountText", value = ("Character Count: " + str(length)))

def saveToFile():
    filename = filename_entry.get()
    filename+=".txt"
    with open(filename, "a") as file:
        text = text_box.get("1.0", "end")
        file.write(text)
        
def loadFromFile():
    loadName = filename_loader_entry.get()
    loadName = loadName.replace('"', "")
    with open(loadName, "r") as fileOpened:
        try: 
            toLoad = fileOpened.read()
            text_box.insert(tk.INSERT, toLoad)
        except:
            error_window()
            
def openReadMe():
    newWindow = tk.Tk()
    newWindow.title("Instructions and Help")
    newWindow.geometry("1500x700")
    paragraphs = scrolledtext.ScrolledText(newWindow, wrap = tk.WORD, height = 60, width = 175)
    paragraphs.pack()
    with open("readMe.txt", "r") as toInsert:
        textInserted = toInsert.read()
        paragraphs.insert(tk.END, textInserted)
        
def warning_window():
    warningWindow = Toplevel(mainWindow)
    warningWindow.title("Warning")
    warningLabel = tk.Label(warningWindow, text = "Warning! This will delete everything in your screen! Do you still want to proceed?")
    warningLabel.pack()
    proceed = tk.Button(warningWindow, text = "Proceed", width = 15, command = lambda:[text_box.delete("1.0", "end"),warningWindow.destroy(),loadFromFile()])
    proceed.pack()
    cancel = tk.Button(warningWindow, text = "Cancel", width = 15, command = warningWindow.destroy)
    cancel.pack()

def secondWarningWindow():
    warningWindowTwo = Toplevel(mainWindow)
    warningWindowTwo.title("Warning")
    warningLabelTwo = tk.Label(warningWindowTwo, text = "Warning! This will delete everything in your screen! Do you still want to proceed?")
    warningLabelTwo.pack()
    proceedTwo = tk.Button(warningWindowTwo, text = "Proceed", width = 15, command = lambda:[text_box.delete("1.0", "end"),warningWindowTwo.destroy()])
    proceedTwo.pack()
    cancelTwo = tk.Button(warningWindowTwo, text = "Cancel", width = 15, command = warningWindowTwo.destroy)
    cancelTwo.pack()

def error_window():
    errorWindow = Toplevel(mainWindow)
    errorWindow.title("ERROR")
    errorLabel = tk.label(errorWindow, text = "Error: invalid filepath. Please check your filepath and try again.")
    errorLabel.pack()
######################GUI#######################
mainWindow = tk.Tk()
mainWindow.title("The Invisible Keyboard")
mainWindow.geometry("1030x600")
text_box = scrolledtext.ScrolledText(mainWindow, wrap =tk.WORD, width = 100, height = 35)
text_box.pack(side= tk.LEFT)
blank_space = tk.Label(mainWindow)
blank_space.pack()
zws_button = tk.Button(mainWindow, text = "Zero Width Space", width = 25,height = 2, command = lambda: insert_zws(characters))
zws_button.pack()
hs_button = tk.Button(mainWindow, text = "Hair Width Space", width = 25, height = 2, command = lambda: insert_hs(characters))
hs_button.pack()
zwnbs_button = tk.Button(mainWindow, text = "Zero Width No Break Space", width = 25, height = 2, command = lambda: insert_zwnbs(characters))
zwnbs_button.pack()
zwnj_button = tk.Button(mainWindow, text = "Zero Width Non-Joiner", width = 25, height = 2, command = lambda: insert_zwnj(characters))
zwnj_button.pack()
zwj_button = tk.Button(mainWindow, text = "Zero Width Joiner", width = 25, height = 2, command = lambda: insert_zwj(characters))
zwj_button.pack()
save_text_button = tk.Button(mainWindow, text = "Save text to file:", width = 25, command = saveToFile)
save_text_button.pack()
filename_entry = tk.Entry(mainWindow, width = 25)
filename_entry.pack()
load_text_button = tk.Button(mainWindow, text = "Load text from file:", width = 25, command = warning_window)
load_text_button.pack()
filename_loader_entry = tk.Entry(mainWindow, width = 25)
filename_loader_entry.pack()
readme_button = tk.Button(mainWindow, text = "Open instructions", width = 25, command = openReadMe)
readme_button.pack()
clearScreenButton = tk.Button(mainWindow, text = "Clear Screen", width = 25, command = secondWarningWindow)
clearScreenButton.pack()
show_chars_button = tk.Button(mainWindow, text = "Show Invisible Characters", width = 25, command = lambda: findInvisibleCharacters(characters))
show_chars_button.pack()
hide_chars_button = tk.Button(mainWindow, text = "Hide Invisible Characters", width = 25, command = lambda: hideInvisibleCharacters(characters))
hide_chars_button.pack()
convert_fully_button = tk.Button(mainWindow, text = "Convert To Encrypted", width = 25, command = convertFully)
convert_fully_button.pack()
copy_to_clipboard_button = tk.Button(mainWindow, text = "Copy Text To Clipboard", width = 25, command = copyText)
copy_to_clipboard_button.pack()
count_characters_button = tk.Button(mainWindow, text = "Count Characters", width = 25, command = countChars)
count_characters_button.pack()
charCountText = StringVar(mainWindow, name = "charCountText", value = "Character Count: 0")
char_count = tk.Label(mainWindow, textvariable = charCountText)
char_count.pack()
mainWindow.mainloop()
