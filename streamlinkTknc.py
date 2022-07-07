import tkinter as tk
from tkinter import ttk
import os

# create the root window
root = tk.Tk()
root.geometry('200x400')
root.resizable(True, True)
root.title('StreamlinkTk')

# retrieve textbox text
def retrieve_input():
    inputValue=textBox.get()# + '\n'
    listbox.insert(tk.END, inputValue)
    # saveInput = '\n' + inputValue
    listw = ''.join(listbox.get(0, tk.END))
    print(listw)
    # saveInput = listbox.get()
    with open('links.txt', 'a') as f:
        f.write(listw)
        f.close()

# textbox def
textBox=tk.Entry(root)
textBox.grid(row=0, column=0)
buttonCommit=tk.Button(root, text="Commit", command=lambda: retrieve_input())
buttonCommit.grid(row=0, column=1)

# open links
filetxt = open('links.txt', 'r')
liste = filetxt.readlines()
filetxt.close()

# listbox def
listbox = tk.Listbox(
    root,
    height=16,
    selectmode='extended')

listbox.grid(
    column=0,
    row=2,
    sticky='nwes'
)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.grid(
    column=1,
    row=2,
    sticky='ns')

# populate listbox
for item in liste:
        listbox.insert(tk.END, item)

# click link
def items_selected(event):
    # for i in listbox.curselection():
    link = listbox.get(listbox.curselection())
    command = "streamlink " + link + " best"
    print(command)
    
    res = os.system(command)

listbox.bind('<<ListboxSelect>>', items_selected)


root.mainloop()
