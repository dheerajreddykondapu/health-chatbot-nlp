# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 23:41:56 2021

@author: dell
"""

from tkinter import *
from main import *
import os

BG_BLUE = "#0341fc"
BG_GRAY = "#3a9997"
BG_COLOR = "#004f4e"
TEXT_COLOR = "#EAECEE"
BT_COLOR = "#00d6d3"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def chat2():
    os.system('python model2.py')   

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
        
        
    def _setup_main_window(self):
        self.window.title("Chat Bot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=670, height=750, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg="#092e2d", fg=TEXT_COLOR,
                           text="DOA IS LIVE :)\nShould NOT be used for real diagnosis.Trained for Dengue", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=15, pady=15)
        self.text_widget.place(relheight=0.745, relwidth=0.780,relx=0.220, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        #selection table
        r_label = Label(self.window, bg=BG_GRAY, height=40, width=50)
        r_label.place(relwidth=0.220, rely=0.08)
        
        #dengue button
     
        dengue_button = Button(r_label, text="DENGUE\nDIAGNOSIS", font=FONT_BOLD, width=20, bg=BT_COLOR, command=chat2)
        dengue_button.place(relx=0.02, rely=0.022, relheight=0.10, relwidth=0.960)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.022, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BT_COLOR, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.022, relheight=0.06, relwidth=0.22)
    
   
    
   
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "YOU")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
    
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"  
        
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
    
  
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()