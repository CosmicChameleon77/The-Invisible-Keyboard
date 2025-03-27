####################Imports#####################
import tkinter as tk
from tkinter import scrolledtext
from tkinter import Toplevel
##################Characters####################
zero_width_space = "\u200b"
hair_space = "\u200a"
zero_width_no_break_space = "\ufeff"
zero_width_non_joiner = "\u200c"
zero_width_joiner = "\u200d"
characters = [["[Zero-Width Space]","[Hair-Width Space]","[Zero-Width No Break Space]","[Zero-Width Non-Joiner]","[Zero-Width Joiner]"],
              [zero_width_space, hair_space, zero_width_no_break_space, zero_width_non_joiner, zero_width_joiner]]
##################Functions#####################
def insert_zws(zero_width_space):
    text_box.insert(tk.INSERT, zero_width_space)
def insert_hs(hair_space):
    text_box.insert(tk.INSERT, hair_space)
def insert_zwnbs(zero_width_no_break_space):
    text_box.insert(tk.INSERT, zero_width_no_break_space)
def insert_zwnj(zero_width_non_joiner):
    text_box.insert(tk.INSERT, zero_width_non_joiner)
def insert_zwj(zero_width_joiner):
    text_box.insert(tk.INSERT, zero_width_joiner)

def findInvisibleCharacters(characters):
    text = text_box.get("1.0","end-1c")
    count = 0
    for i in characters[1]:
        text = text.replace(characters[1][count],characters[0][count])
        count+=1
    text_box.delete("1.0","end")
    text_box.insert(tk.INSERT, text)

def hideInvisibleCharacters(characters):
    text = text_box.get("1.0","end-1c")
    count = 0
    for i in characters[1]:
        text = text.replace(characters[0][count],characters[1][count])
        count+=1
    text_box.delete("1.0","end")
    text_box.insert(tk.INSERT, text)

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
zws_button = tk.Button(mainWindow, text = "Zero Width Space", width = 25,height = 2, command = lambda: insert_zws(zero_width_space))
zws_button.pack()
hs_button = tk.Button(mainWindow, text = "Hair Width Space", width = 25, height = 2, command = lambda: insert_hs(hair_space))
hs_button.pack()
zwnbs_button = tk.Button(mainWindow, text = "Zero Width No Break Space", width = 25, height = 2, command = lambda: insert_zwnbs(zero_width_no_break_space))
zwnbs_button.pack()
zwnj_button = tk.Button(mainWindow, text = "Zero Width Non-Joiner", width = 25, height = 2, command = lambda: insert_zwnj(zero_width_non_joiner))
zwnj_button.pack()
zwj_button = tk.Button(mainWindow, text = "Zero Width Joiner", width = 25, height = 2, command = lambda: insert_zwj(zero_width_joiner))
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
mainWindow.mainloop()

