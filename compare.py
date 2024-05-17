import numpy as np 
import matplotlib.pyplot as plt  
import pickle

def addlabels(methods,values):
    for i in range(len(methods)):
        plt.text(i,values[i],values[i])


def plot1():

    # creating the dataset 
    data = {'DNN Model':95.45,'SVM Model':68.50} 
    methods = list(data.keys()) 
    values = list(data.values()) 
    
    fig = plt.figure(figsize = (10, 5)) 
    
    # creating the bar plot 
    plt.bar(methods, values, color ='green', width = 0.4)

    addlabels(methods,values)
    
    plt.xlabel("Methods") 
    plt.ylabel("Accuracy") 
    plt.title("Performance comparison ")
    plt.savefig('RESULT/compare.jpg')
    plt.show() 

plot1()