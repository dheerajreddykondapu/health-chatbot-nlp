import nltk 
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import random
import json
from tkinter import *
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import webbrowser
from gui import *


#Loading JSON Data

with open("intents.json") as file:
    data = json.load(file)
    
    #Extracting Data
    
words = []
labels = []
docs_x = []
docs_y =[]
        
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
                
        if intent["tag"] not in labels:
            labels.append(intent["tag"])
     
        
    #Pre-Processing->
     
    #stemming
                
words = [stemmer.stem(w.lower())for w in words if w not in "?"]
words = sorted(list(set(words)))
        
labels = sorted(labels)
      
    #bag of words
      
training = []
output =[]
        
out_empty = [0 for _ in range(len(labels))]
        
for x, doc in enumerate(docs_x):
    bag = []
            
    wrds = [stemmer.stem(w) for w in doc]
            
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
                    
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
            
    training.append(bag)
    output.append(output_row)
            
training = numpy.array(training)
output = numpy.array(output)
    
     
    #model creation
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
    
model = tflearn.DNN(net)   

#training model

model.fit(training, output, n_epoch=500, batch_size=8, show_metric=True)
 
    
#Predictions(input, Convert a bag, prediction from the model, most probable class, Pick a response the choosen class)
    
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
                
    return numpy.array(bag)
 
bot_name = "DOA"

def get_response(msg):
    
       
    inp = msg
        
    results = model.predict([bag_of_words(inp, words)])[0]

    results_index = numpy.argmax(results)
    tag = labels[results_index]
        
    if results[results_index] > 0.7:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                if 'google' in tag:
                          new=2
                          tabUrl="http://google.com/?#q="
                          webbrowser.open(tabUrl+tag,new=new)
                responses = tg['responses']
                
        return random.choice(responses)

    return "i didn't get that, try again"




