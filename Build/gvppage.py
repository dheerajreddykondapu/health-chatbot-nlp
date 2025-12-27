# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:25:24 2021

@author: dell
"""


import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os


def awakedoa():
    os.system('python gui.py')

BG_BLUE = "#0341fc"
BG_GRAY = "#aec1e6"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
BT_COLOR = "#00d6d3"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
FONT_BOLD2 = "Helvetica 16 bold"



root = Tk()
root.resizable(width=False, height=False)
frame=Frame(root)
frame.configure(bg="#17202A")

root.geometry("956x540")
# Create a photoimage object of the image in the path
image1 = Image.open("dbg5.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)

def homedelete():
    h_head.place_forget()
    h_body1.place_forget()
    h_body2.place_forget()
    
def abstractdelete():
    a_head.place_forget()
    a_body.place_forget()
    
def systemdelete():
    s_head.place_forget()
    s_body.place_forget()
    s_button.place_forget()
    
def doadelete():
    d_body.place_forget()
    d_button.place_forget()
    
def conclusiondelete():
    c_head.place_forget()
    c_body.place_forget()


def home():

        
    global h_head, h_body1, h_body2
          
    h_head = Label(root, text="HEALTH CHECK CHATBOT", font=("Helvetica", 30,"bold"),bg="#CAFBED")
    h_head.place(relx=0.225, rely=0.42)
    h_body1 = Label(root, text="PROJECT GUIDE:\n\nSmt. CH. SUNEETHA,\n ASSISTANT PROFESSOR", font=FONT_BOLD2, bg="#CAFBED")
    h_body1.place(relx=0.06, rely=0.67)
    h_body2 = Label(root, text="PROJECT MEMBERS:\nK. DHEERAJ REDDY       2018-1902004\nMEGHNA GHALE             2018-1902019\nL.VAMSI                           2018-1902008", font=FONT_BOLD2, bg="#CAFBED")
    h_body2.place(relx=0.52, rely=0.67)
        
    abstractdelete()
    systemdelete()
    doadelete()
    conclusiondelete()
    
def abstract():
    
    global a_head, a_body    
        
    a_head = Label(root, text="CHATBOT USING DEEP LEARNING", font=("Helvetica", 26,"bold"),bg="#CAFBED")
    a_head.place(relx=0.200, rely=0.36)
    a_body = Message(root, text="In our lives, health is extremely vital. It is quite difficult to seek a doctor's consultation for a basic health condition in this epidemic circumstance. This Project aims on developing a medical chatbot using Artificial Neural Network concept which is programmed in a way to diagnose the disease and provide a general prescription and basic remedies  which a person can relay to some extent. More or Less it helps in providing the information as programmed to respond within a short time and ease in accessibility for the user. To do so, thorough research is performed and programmed by analyzing the probability   of the text input.", font=("Helvetica", 17,"bold"),aspect=380,bg="#CAFBED",justify="left")
    a_body.place(relx=0.026, rely=0.46)

    homedelete()
    systemdelete()
    doadelete()
    conclusiondelete()
            

def SYSTEM():
    def systemflow():
        
        image2 = Image.open("FLOWCHAT.jpg")
        test = ImageTk.PhotoImage(image2)
            
        label2 = tkinter.Label(image=test)
        label2.image = test
            
        # Position image
        label2.place(x=0, y=0)
                        
        
        def back():
            label2.destroy()
            f_button.destroy()
            
        f_button = Button(text="BACK",bd=3, font=FONT_BOLD, bg=BT_COLOR, command=back)
        f_button.place(relx=0.90, rely=0.88)      
        
    global s_head, s_body, s_button, t
    
    s_head = Label(root, text="SYSTEM INFORMATION", font=("Helvetica", 26,"bold"),bg="#CAFBED")
    s_head.place(relx=0.300, rely=0.37)
    s_body = Message(root, text="Indian developed chatbots are still  under development in healthcare field and usage of these bots are limited due to lack of sources. Some of the widely used general chatbots are unable to diagnose health problems as they depend on internet search.\n\nThis project helps the people with disease diagnosis, common medications, and general prescriptions through ease in accessibility. This chatbot responds to the user's command’s using NLP (Natural Language Processing), NLTK (Natural Language Toolkit) and classification algorithms i.e. Artificial Neural Network(ANN) with a activation function.", font=("Helvetica", 16,"bold"),aspect=430,bg="#CAFBED",justify="left")
    s_body.place(relx=0.024, rely=0.48)
    s_button = Button(text="SYSTEM FLOW",bd=3, font=FONT_BOLD, bg=BT_COLOR, command=systemflow)
    s_button.place(relx=0.43, rely=0.87)
        
        
    homedelete()
    abstractdelete()
    doadelete()
    conclusiondelete()      
        
def DOA():
    
    global d_body, d_button
    
    d_body = Message(root, text="OS : Windows 7 with SP1;  Recommended: Windows 10\n\nCPU : Intel or AMD processor with 64-bit support;\nRecommended: 2.8 GHz or faster processor\n\nDisk Storage : 2 GB of free disk space\n\nMonitor Resolution : 1280x800;  Recommended: 1920x1080\n\nInternet : Internet connection required for web search", font=("Helvetica", 16,"bold"),aspect=430,justify="left", bg="#CAFBED")
    d_body.place(relx=0.024, rely=0.36)

    d_button = Button(text="ACTIVATE DOA", font=FONT_BOLD, bg=BT_COLOR,width=15, command=awakedoa)
    d_button.place(relx=0.42, rely=0.85)
    
    
    homedelete()
    abstractdelete()
    systemdelete()
    conclusiondelete()

    
def conclusion():
    
    global c_head, c_body

    c_head = Label(root, text="CONCLUSION", font=("Helvetica", 26,"bold"),bg="#CAFBED")
    c_head.place(relx=0.380, rely=0.36)    
    c_body = Message(root, text="This AI chatting bot will reduce the burden of both medical staff and patients.\nAs the world is Leaning on the online mode, it is very necessary to bring the same change in the medical field too. This project is a small step towards the goal to build an Indian AI chatbot for helping people with quick medical assistance.\n\nHealth check chat bot will reduce cost and man power requirements of medical industry and will be an efficient way to save time for the patients to get medical assistant.", font=("Helvetica", 17,"bold"),bg="#CAFBED",aspect=380,justify="left")
    c_body.place(relx=0.030, rely=0.46)
    
    homedelete()
    abstractdelete()
    systemdelete()
    doadelete()
    

    

home_button = Button(text="HOME",bd=3, font=FONT_BOLD, bg=BT_COLOR,width=12, command=home)
home_button.place(relx=0.06, rely=0.262)

abstract_button = Button(text="ABSTRACT",bd=3, font=FONT_BOLD, bg=BT_COLOR,width=12, command=abstract)
abstract_button.place(relx=0.250, rely=0.262)

algorithm_button = Button(text="SYSTEM INFO",bd=3, font=FONT_BOLD, bg=BT_COLOR,width=12, command=SYSTEM)
algorithm_button.place(relx=0.434, rely=0.262)

DOA_button = Button(text="SYSTEM REQ",bd=3, font=FONT_BOLD, bg=BT_COLOR, width=12, command=DOA)
DOA_button.place(relx=0.618, rely=0.262)

conclusion_button = Button(text="CONCLUSION",bd=3, font=FONT_BOLD, bg=BT_COLOR,width=12, command=conclusion)
conclusion_button.place(relx=0.80, rely=0.262)


"""
close_button = Button(text="EXIT", font=FONT_BOLD, bg=BG_GRAY, command=close)
close_button.place(relx=0.80, rely=0.60)
"""

root.mainloop()

