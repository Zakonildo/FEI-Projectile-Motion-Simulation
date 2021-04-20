import os
import tkinter as tk
from tkinter import filedialog

def getFile():
    file = filedialog.askopenfilename(initialdir = './', title = 'Selecione o arquivo', filetypes=(("Comma-separated values", "*.csv"),))
    return file

def getFileLines(file):
    f = open(file, "r")
    points = [[], [], [], [], [], [], []]
    count = 0
    for i in f.readlines():
        if count > 1:
            i.replace("\n", "").split(",")
            
            try:
                points[0].append(float(i.replace("\n", "").split(",")[0]))
            except:
                continue
            try:
                points[1].append(float(i.replace("\n", "").split(",")[1]))
            except:
                continue
            try:
                points[2].append(float(i.replace("\n", "").split(",")[2]))
            except:
                continue
            try:
                points[3].append(float(i.replace("\n", "").split(",")[3]))
            except:
                continue
            try:
                points[4].append(float(i.replace("\n", "").split(",")[4]))
            except:
                continue
            try:
                points[5].append(float(i.replace("\n", "").split(",")[5]))
            except:
                continue
            try:
                points[6].append(float(i.replace("\n", "").split(",")[6]))
            except:
                continue
        count += 1
    f.close()
    
    return points

def exportSingleGraph(filename, v, x, y):
    s = filename + "\n" + x + "," + y + "\n"
    for i in range(len(v[0])):
        s += str(v[0][i]) + "," + str(v[1][i]) + "\n"
    file = open(filename + ".csv", "w")
    file.write(s)
    file.close()
    return