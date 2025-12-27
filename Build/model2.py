# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:38:16 2021

@author: dell
"""

import numpy
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from tkinter import *


BG_BLUE = "#0341fc"
BG_GRAY = "#3a9997"
BG_COLOR = "#004f4e"
TEXT_COLOR = "#EAECEE"
BT_COLOR = "#00d6d3"

#Loading CSV Data
    
Dataset=pd.read_csv("dengue.csv")

X = Dataset.values[:,:8]
Y = Dataset.values[:,-1]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=2,test_size=0.25)

min_max_scaler = preprocessing.MinMaxScaler()
X_train=min_max_scaler.fit_transform(X_train)
X_test=min_max_scaler.transform(X_test)

#model creation --> model2

model2 = Sequential()


model2.add(Dense(32, activation='relu'))
model2.add(Dropout(0.2))

model2.add(Dense(32, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)
#can use mse
model2.compile(loss='sparse_categorical_crossentropy',
	optimizer=opt,
	metrics=['accuracy'])

#training model2

model2.fit(X_train, Y_train, epochs=150, validation_data=(X_test,Y_test))


root=Tk()
root.title("DENGUE")
root.resizable(width=False, height=False)
root.configure(bg=BG_GRAY)


frame=Frame(root)
frame.configure(bg=BG_GRAY)
 
arr=[]  


def destr():
    output.configure(state='normal')
    output.delete(1.0,END)

def but():
    a=F.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    F.delete(0,END)
    
    
    a=H.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    H.delete(0,END)
    
    
    a=B.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    B.delete(0,END)
    
    a=J.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    J.delete(0,END)
    
    a=T.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    T.delete(0,END)
    
    a=A.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    A.delete(0,END)
    
    a=AP.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    AP.delete(0,END)
    
    a=V.get()
    if a=="YES" or a=="yes":
        arr.append(1)
    else:
        arr.append(0)
    V.delete(0,END)
    
    results2 = model2.predict(numpy.array([arr], dtype=numpy.float32))[0]
    print(results2)
    results2_index = numpy.argmax(results2)
    
    output.configure(state='normal')        
    output.insert(END, "\t\tMedical Prescription")
    output.configure(state='disabled')
    

    if results2[results2_index] > 0.75:
        output.configure(state='normal')
        output.insert(END, "\n\n\nYou have dengue symptoms\n\nPlease consult a infectious diseases specialist ASAP\n\nFirst Aid Medication:\n\nPyrapem syrup -> 15ml\n=>after meal 3 times a day\nCalpal ->4 Tablets(2 Days course)\n=>After breakfast 1\nAfter dinner 1\nCaripill ->4 Tablets(2 Days course)\n=>After breakfast 1\nAfter dinner 1\nInjection -> Montaz")
        output.configure(state='disabled')

        del arr[:]

    else:
                             
        output.configure(state='normal')
        output.insert(END, "\n\n\nYou don't have dengue")
        output.configure(state='disabled')
        
        
        if arr[0] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine for fever:\nCalphal ->4 Tablets(2 Days course)\n=>After breakfast 1\nAfter Dinner 1\nDolo->4 Tablets(2 Days course)\n=>After breakfast 1\nAfter dinner 1")
            output.configure(state='disabled')
            
        if arr[1] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine for headache:\nCalphal ->2 Tablets(2 Days course)\n=>After Lunch 1\nNeproshin D->2 Tablets(2 Days course)\n=>After Lunch 1")     
            output.configure(state='disabled')
            
        if arr[2] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine for body pains:\nFastac plus ->4 Tablets(2 Days course)\n=>After Lunch 1\nAfter Dinner 1\nZerodol P ->2 Tablets(1 Day course)\n=>After Lunch 1\nAfter Dinner 1\nInjection -> Zonac")    
            output.configure(state='disabled')
            
        if arr[3] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine for joint pains: \nAcelo Plus ->4 Tablets(2 Days course)\n=>After Breakfast 1\nAfter Dinner 1\nAcelodol MR ->4 Tablets(2 Days course)\n=>After Breakfast 1\nAfter Dinner 1")
            output.configure(state='disabled')
            
        if arr[4] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine for taste loss: \nAmitriptyline ->4 Tablets(2 Days course)\n=>After Breakfast 1\nAfter Dinner 1\nMetronidazole ->4 Tablets(2 Days course)\n=>After Breakfast 1\nAfter Dinner 1")
            output.configure(state='disabled')
            
        if arr[5] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine and dite for  appetite loss:")
            output.configure(state='disabled')
            
        if arr[6] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine for abdominal pain:\nCylophom ->4 Tablets(2 Days course)\n=>After breakfast 1\nAfter dinner 1\nBigspas ->4 Tablets(2 Days course)\n=>After breakfast 1\nAfter dinner 1\nAnaspas ->Afternoon 1 Tablet")
            output.configure(state='disabled')
            
        if arr[7] == 1:
            output.configure(state='normal')
            output.insert(END, "\n\nmedicine for vomiting:\nVomikind ->2 Tablets(1 Day course)\n=>Morning 1\nAfter Dinner 1\nPerinorm ->2 Tablets(1 Day course)\n=>Morning 1\nAfter dinner 1\nInjection -> Vomikind")
            output.configure(state='disabled')

        output.configure(state='normal')
        output.insert(END, "\n\n\nIf your symptoms are getting worse, consult a infectious\ndiseases specialist \n")
        output.configure(state='disabled')
        
       
    del arr[:]        
    
HEAD=Label(frame, 
         text="ENTER YES IF YOU ARE HAVE THE SYMPTOM \nAND\n ENTER NO IF YOU ARE NOT HAVE THE SYMPTOM", 
         font=("calibri", 18,'bold'),
         bg=BG_GRAY)
HEAD.grid(row=0, column=0,columnspan=2,padx=30, pady=10)
    
OUT=Label(frame, 
         text="DIAGNOSIS RESULT", 
         font=("calibri", 18,'bold'),
         bg=BG_GRAY)
OUT.grid(row=0, column=2,padx=50, pady=10)
       
output=Text(frame,
        width=50,
        height=28,
        fg="#ffffff",
        bg=BG_COLOR,
        font=("calibiri", 10), state='disabled')
output.grid(row=1,column=2,rowspan=10,padx=15)

    
    
FEVER=Label(frame,
         text="Are you having fever ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
FEVER.grid(row=2, column=0,padx=10)
    
F=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
F.grid(row=2, column=1, pady=10,padx=50)

HEADACHE=Label(frame,
         text="Are you having headache ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
HEADACHE.grid(row=3, column=0,padx=10)
    
H=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
H.grid(row=3, column=1, pady=10,padx=50)

body_pains=Label(frame,
         text="Are you having body pains ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
body_pains.grid(row=4, column=0,padx=10)
    
B=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
B.grid(row=4, column=1, pady=10,padx=50)

joint_pains=Label(frame,
         text="Are you having joint pains ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
joint_pains.grid(row=5, column=0,padx=10)
    
J=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
J.grid(row=5, column=1, pady=10,padx=50)

taste=Label(frame,
         text="Are you not able to taste ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
taste.grid(row=6, column=0,padx=10)
    
T=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
T.grid(row=6, column=1, pady=10,padx=50)


appetite_loss=Label(frame,
         text="Appetite loss ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
appetite_loss.grid(row=7, column=0,padx=10)
    
A=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
A.grid(row=7, column=1, pady=10,padx=50)

abdominal_pain=Label(frame,
         text="Are you having Abdominal pain ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
abdominal_pain.grid(row=8, column=0,padx=10)
    
AP=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
AP.grid(row=8, column=1, pady=10,padx=50)

vomiting=Label(frame,
         text="Are you having nausea OR vomiting ",
         font=("calibri", 18,'bold'),
         bg=BG_GRAY,
         justify="left")
vomiting.grid(row=9, column=0,padx=10)
    
V=Entry(frame, 
        width=20, 
        font=("calibiri", 14,'bold'),
        fg="#022423",
        bg="#0bb3af")
V.grid(row=9, column=1, pady=10,padx=50)


FBUTTON=Button(frame, 
       text="START DIAGNOSIS",
       width=15,
       font=("lora", 14,'bold'), 
       bg=BT_COLOR,
       command=but)
FBUTTON.grid(row=11, column=0,columnspan=2,pady=40)

dest_button=Button(frame,
       text="CLEAR RESULT",
       width=13,
       font=("lora", 14,'bold'), 
       bg=BT_COLOR, 
       command=destr)
dest_button.grid(row=11, column=2,columnspan=2,pady=40)    
            
frame.pack()
root.mainloop()


"""

uin = []
    
def chat2():


    print(uin)
    
    inp = input("\n are you having fever : ")
    
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)
    
    inp = input("\n are you having headache : ")
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)

    inp = input("\n are you having body pains : ")
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)

    inp = input("\n are you having joint pains : ")
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)
        
    inp = input("\n are you having taste : ")
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)
        
    inp = input("\n are you having appetite loss : ")
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)
        
    inp = input("\n are you having abdominal pain : ")
    
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)
        
    inp = input("\n are you having vomiting (or nausea) : ")
    
    if inp == "yes":
        uin.append(1)
    else:
        uin.append(0)
                

    
    #inp2 = input[""]
         
    results2 = model2.predict(numpy.array([uin], dtype=numpy.float32))[0]

    results2_index = numpy.argmax(results2)
        
    if results2[results2_index] > 0.7:
        print("\n your having dengue. \n")
    else:
        print("\n your not having dengue. \n")
    
# MEDICIN FOR SYMPTOMS        
    
    if uin[0] == 1:
        print("\n medicin for fever")
        
    if uin[1] == 1:
        print("\n medicin for headache")        
        
    if uin[2] == 1:
        print("\n medicin for body pains")    
        
    if uin[3] == 1:
        print("\n medicin for joint pains")

    if uin[4] == 1:
        print("\n what to eat taste loss")

    if uin[5] == 1:
        print("\n medicin and dite for  appetite loss")
        
    if uin[6] == 1:
        print("\n medicin for abdominal pain")

    if uin[7] == 1:
        print("\n medicin for vomiting")
    
    del uin[:]

"""