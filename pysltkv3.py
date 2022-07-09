import tkinter as tk
from tkinter import BOTH, BOTTOM, LEFT, RIGHT, Y, Frame, ttk
import os

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # create the self window
    self.title('StreamlinkTk')
    self.geometry('330x500')
    self.resizable(True, True)
    
    if os.name == "nt":
        self.option_add('*Font', 'Arial 12')
    else:
        self.option_add('*Font', 'Arial 20')

    self.frame = Frame(self)
    self.frame.pack()

    # listbox def
    self.listbox = tk.Listbox(self.frame, height=16, width=30, selectmode='single')
    self.listbox.pack(pady=10, side= LEFT)

    # link a scrollbar to a list
    self.scrollbar = ttk.Scrollbar(self.frame, orient='vertical')
    self.scrollbar.pack(side=RIGHT, fill= Y)
    self.listbox.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.config(command=self.listbox.yview)

    # textbox def
    self.textBox=tk.Entry(self)
    self.textBox.bind('<Return>',lambda event:retrieve_input())
    self.textBox.bind('<Button-3>',lambda event:Paste())
    self.textBox.pack(padx=10, side= LEFT)

    # button def
    self.buttonCommit=tk.Button(self, text="Commit", command=lambda: self.retrieve_input())
    self.buttonCommit.pack(padx=10, side= LEFT)
     
    def loadFile():
        # open links
        filetxt = open('links.txt', 'r')
        liste =  filetxt.readlines()
        filetxt.close()
        return liste

    # populate listbox
    for item in loadFile():
            itemr = item.replace("\n", "")
            self.listbox.insert(tk.END, itemr)
            
    # retrieve textbox text
    def retrieve_input():
        inputValue=self.textBox.get() + '\n'
        print(inputValue)
        self.listbox.insert(tk.END, inputValue)
        with open('links.txt', 'a') as f:
            f.write(inputValue)
            f.close()

    # paste when R-click
    def Paste():
            self.textBox.event_generate('<<Paste>>')
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

    self.listbox.bind('<<ListboxSelect>>', items_selected)


if __name__ == "__main__":
  app = App()

  app.mainloop()