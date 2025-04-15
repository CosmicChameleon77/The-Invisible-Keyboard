Welcome to the Invisible Keyboard - a project that allows you to type invisible characters easily. 

This document should contain everything you need to interact with the project and modify the code for your own purposes. 

Things you must have installed to run the code: 

Something capable of running (and ideally editing) .py files. Just install python for this.
the Tkinter library. If you have python installed but do not have tkinter installed, question why. It's supposed to be pre-packaged with python. Maybe try attempting a clean install of python?
The Pyperclip Library- go into your command line and type "pip install pyperclip" without the quotes. It can take a moment to wake up or do anything so please be patient and if you're inexperienced with the command line, don't worry. This just installs a python library and it's one I'm almost certain is safe. 

You should also have this file in the same folder as the main program. 



Help - buttons and inputs: 

Zero Width Space- adds a zero width space wherever your cursor is. This is completely invisible but you can see its presence when you press the backspace button. Great for really irritating pranks if added at random in the middle of words. You should be aware that if placed in the middle of a word, the sections of word either side of it are treated as two separate words so may appear on opposite sides of a line break. 

Hair Width Space- adds a hair width space wherever your cursor is. It's not perfectly invisible and appears extremely large in the font used by the editor but in most fonts is noticeable but tiny. 

Zero Width No Break Space- adds a zero width no break space to wherever your cursor is. It's completely invisible. 

Zero Width Non Joiner- adds a zero width non joiner to wherever your cursor is. It's completely invisible in most languages but worth noting that it may cause issues for languages that do use ligatures. Some English fonts and contexts use ligatures such as combining the letters in "fi" when placed together or in "fl" but most don't. 

Zero Width Joiner- adds a zero width joiner wherever your cursor is. The same warning as above also applies here but instead this tells the computer to create a ligature. I've not tried it myself but I've heard it can also be used to combine two emojis into one new one in some apps. 

Save Text To File- type the file name of the file you want to save it to in the text entry box below the button and press the button to save it. If it doesn't already exist, a new file will be created in the same location as the code is in. If the file isn't in the same folder as the code, you will have to type out the full file path or a new file of the same name will be created. The program automatically adds .txt to the end of the filename so please don't add it yourself. See the "Modifying the Program" section for instructions on how to change this. So that you don't accidentally delete the contents of a file, I've made it add the text to the end of the file. You CAN modify the program to overwrite the old file but I really cannot stress how ill-advised that would be. Any data lost due to your own foolishness is your own responsibility. Even so, I have put instructions on modifying the program to do this at the end of this readMe. 

Load Text From File- paste the file path to the file you want to load into the text box below the button and press the button. If you use windows, you will notice speech marks either side of the file path. Don't worry about these- my code automatically removes all speech marks from the file path. If your file name contains speech marks, you will need to refer to the modifying the code section of this file. 

Text input- Just type into the big text box. It's scrollable so don't worry about disappearing off the end of the box. 

Show Invisible Characters - replaces invisible characters with their names in the text box. Remember to press hide before saving to file. 

Hide Invisible Characters - replaces invisible character names with their corresponding characters in the text box

Convert To Encrypted - converts to my choice of encryption (to unicode hex codes corresponding to each character, then to morse, then to invisible characters) 

Copy To Clipboard - Who could possibly guess...



Help- Glitches and Errors:

Honestly, just contact me if there's a glitch. I've tested this program but not especially thoroughly. Hopefully I'll be able to fix the problem. Also check that you've inputted a valid file path if your file isn't loading. Could be that the file path or file doesn't exist (though you should see a popup window warning you of this). 
If the window doesn't fit on your screen, try changing its size in mainWindow.geometry()


Modifying the program: 

If you need any help with this, contact me. It should be fairly simple to make most modifications. Same goes for additional features you want, I'm around to update the code if you need it updated or anything added but it's faster to do it yourself. With that in mind, here's some code you can (almost) copy and paste across to make different features in the program. Please note that anything inside these: <> is something you should replace with your own input (usually variable names). 

Stopping the program from adding .txt to the end of filenames when creating new files: 
delete the line that says filename+=".txt". 

Changing the type of file you write the code to: 
in the line filename+=".txt", replace ".txt" with "<file ending>" or alternatively just delete the line and add the file ending yourself whenever you create a new file. 

Adding extra buttons: 
Insert the code below into the GUI section of the code, after the line that says mainWindow.geometry("1030x600") and before the line that says mainWindow.mainloop() or equivalent for other windows (the code for which can be found within various functions). Ensure that the button name you want to use doesn't already exist and that the function you want to tie it to has been written, alongside any variables the function uses. 
<Button Name> = tk.Button(mainWindow, text = "<Your text here>", width = 25, command = lambda: <function>)
<Button Name>.pack()

If you want to make the button you add insert a character, you need to define a variable as follows: 
<variable name> = "<text to insert>"
for unicode characters, make <text to insert> read \u<4 digit hex code>
you can find the hex codes online. Now in the functions section, ideally before all the other functions, add the following code: 
def <function>(<variable name>):
    text_box.insert(tk.INSERT, <variable name>)

Overwriting files- NOT RECCOMENDED: 
Swap the line that says file = open(filename, "a") in saveToFile() for file = open(filename, "w")

Stopping the program from removing speech marks: 
Note that if you intend to do this, you need to remember to remove speech marks from filepaths manually. Simply delete this line: loadName = loadName.replace('"', "")

Changing the default window size: 
In the lines which say <window name>.geometry("<number 1>x<number 2>"), try changing the values of <number 1> and <number 2>

If there's anything else you want to modify but don't know how to, please just reach out. 


What you can do with the code: 
See the license for full details but essentially I'm permitting you to download, use and modify the code for your purposes- just not make it proprietary, paid-for or use it for your own purposes without crediting/obtaining permission from me first. I doubt that this will be a problem but it's always important to cover these areas before problems arise
