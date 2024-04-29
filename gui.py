import lt2ti
import tkinter

#fn = r'examples\catalog.asc'
#l2tobj = lt2ti.lt2circuiTikz()
#l2tobj.readASCFile(fn)
#l2tobj.writeCircuiTikz(fn+r'.tex')

import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import TKinterModernThemes as TKMT
import pyperclip


    
    

class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("LTspice to Latex converter", "park", "dark")
        self.root.geometry("+0+0")
        #self.button_frame = self.addLabelFrame("Frame Label")
        btn = self.Button("Open file", self.load) #the button is dropped straight into the frame
        btn.grid(column=0, row=1)
        self.run()
        self.text = None
        self.text_area = None
        

    def load(self):
        #print("Button clicked!")
        path = tk.filedialog.askopenfilename()
        if path:
            l2tobj = lt2ti.lt2circuiTikz()
            l2tobj.readASCFile(path)
            self.text = l2tobj.writeCircuiTikz()
            self.updateText()
            self.drawCopyButton()

    def updateText(self):
        self.text_area = ScrolledText(self.root, wrap=tk.WORD, width=100, height=30)
        self.text_area.grid(column=0, row=2, padx=5, pady=5)
        self.text_area.delete('1.0', tk.END)   # Clear existing text
        self.text_area.insert(tk.END, self.text)    # Insert new text

    def drawCopyButton(self):
        copy_button = self.AccentButton("Copy to Clipboard", self.copy_to_clipboard)
        copy_button.grid(column=0, row=0, padx=5, pady=5)

    def copy_to_clipboard(self):        
        text_to_copy = self.text_area.get("1.0", "end-1c")  # Get text from text area
        pyperclip.copy(text_to_copy)  # Copy text to clipboard            


App()