from dataclasses import replace
import tkinter as tk
from tkinter import BOTH, BOTTOM, LEFT, RIGHT, Y, Frame, ttk
import os

print(os.name)

# create the root window
root = tk.Tk()
root.geometry('330x500')
root.resizable(True, True)
root.title('StreamlinkTk')
if os.name == "nt":
    root.option_add('*Font', 'Arial 12')
else:
    root.option_add('*Font', 'Arial 20')


frame = Frame(root)
frame.pack()

# listbox def
listbox = tk.Listbox(
    frame,
    height=16,
    width=30,
    selectmode='single')

listbox.pack(pady=10, side= LEFT)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    frame,
    orient='vertical'
)
scrollbar.pack(side=RIGHT, fill= Y)
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
# listbox['yscrollcommand'] = scrollbar.set

# textbox def
textBox=tk.Entry(root)
textBox.bind('<Return>',lambda event:retrieve_input())
textBox.bind('<Button-3>',lambda event:Paste())
textBox.pack(padx=10, side= LEFT)

# button def
buttonCommit=tk.Button(root, text="Commit", command=lambda: retrieve_input())
buttonCommit.pack(padx=10, side= LEFT)

# open links
filetxt = open('links.txt', 'r')
liste =  filetxt.readlines()
filetxt.close()

# # populate listbox
for item in liste:
        # print(item)
        # item.replace("\n", "")
        itemr = item.replace("\n", "")
        listbox.insert(tk.END, itemr)
        #listbox.insert(tk.END, item)

 
# retrieve textbox text
def retrieve_input():
    inputValue=textBox.get() + '\n'
    print(inputValue)
    listbox.insert(tk.END, inputValue)
    with open('links.txt', 'a') as f:
        f.write(inputValue)
        f.close()

# paste when R-click
def Paste():
          textBox.event_generate('<<Paste>>')
          retrieve_input()

# click link
def items_selected(event):
    indexLb = event.widget.curselection()
    link = event.widget.get(indexLb).replace("\n", "")
    commandsl(link)

# Send link to streamlink
def commandsl(link):    
    command = "streamlink " + link + " best"
    print(command)
    res = os.system(command)

listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()
