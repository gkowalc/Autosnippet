from os import listdir
from tkinter import *
from pathlib import Path
from tkinter.font import Font
from pyperclip import copy
from pyautogui import hotkey, click, moveTo, position
base_dir = 'C:/snippets/'
snippetsList = []
for i in  sorted(listdir(base_dir), reverse=True):
    snippetsList.append(i)
directoriesList = []
multipleSelectionList = []
stringtobecopied = []
#############################################################################

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    # https://stackoverflow.com/questions/7616541/get-selected-item-in-listbox-and-call-another-function-storing-the-selected-for
    createSnippetList(retrieveSnippetValue(evt, buttonnobject_1))

def retrieveSnippetValue(evt, buttonnobject_1):
    eventwidgetobject = evt.widget
    index = int(eventwidgetobject.curselection()[0])
    multipleSelectionList.append(index)
    for i in multipleSelectionList:
        buttonnobject_1.select_set(i)
        buttonnobject_1.activate(i)
    snippetValue = eventwidgetobject.get(index)
    return snippetValue

def createSnippetList(snippetValue):
    stringtobecopied.append(readFromLocalFile(createFilePath(snippetValue)))

def readFromLocalFile(path):
    contents = Path(path).read_text()
    return contents

def createFilePath(onselect):
    path = base_dir + onselect
    return path

def toClipboard():
    mergedstring = ''.join(stringtobecopied)
    copy(mergedstring)
    top.destroy()
    triggerClipboard()

def destroyClipboard():
    top.destroy()

def triggerClipboard():
    moveTo(currentMouseX, currentMouseY)
    click()
    hotkey('ctrl', 'v')

def enterKeyPressed(event):
    if str(event.char) == '\r':
        toClipboard()

def update_list():
        search_term = search_var.get()
        buttonnobject_1.delete(0, END)
        for item in snippetsList:
            if search_term.lower() in item.lower():
                buttonnobject_1.insert(END, item)

def close(event):
    sys.exit()

### GUI CREATION ###
def listboxLenght(listboxlenghtparameter):
    if len(snippetsList) > listboxlenghtparameter:
        return listboxlenghtparameter
    else:
        return len(snippetsList)
top = Tk()
myFont = Font(family="Times New Roman", size=11)
f = Frame(top)
Label(f, text="Select snippet",  font=myFont).grid(row=0, column=0)
f.pack()
### Listbox item creation
# this function call is required to limit listbox lenght to 55 - otherwise expanding list will  block out searchbox/entry object. Value 55 should be smaller if myFont size is larger than 11
buttonnobject_1 = Listbox(top, font=myFont, height=listboxLenght(55))
n = 1
for i in snippetsList:
    buttonnobject_1.insert(n, i)
    n = +1
buttonnobject_1.bind('<<ListboxSelect>>', onselect)
buttonnobject_1.bind("<Key>", enterKeyPressed)
buttonnobject_1.bind('<Escape>', close)
buttonnobject_1.pack()
f.pack()
f = Frame(top)
### Button add/exit creation
b1 = Button(f, text="Paste snippet", command=toClipboard)
b2 = Button(f, text="Exit", command=destroyClipboard)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
### Searchbox item creation
search_var = StringVar()
search = search_var.trace("w", lambda name, index, mode: update_list())
entry = Entry(textvariable=search_var, width=16)
entry.pack()
f.pack()
entry.focus()
entry.focus()
update_list()
currentMouseX, currentMouseY = position()
# Required for bundling GUI item
top.mainloop()
