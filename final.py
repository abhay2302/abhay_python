#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:04:02 2018

@author: Abhay Kumar
"""
from Tkinter import *
import Tkinter as tk, Tkconstants, tkFileDialog
import os
import sys
from tkMessageBox import *

path_to_native ="/home/user/Abhay/jellyfish/tools/sanity_test/native_test"

class App:
    def __init__(self, master):
        frame=Frame(master)
        frame.pack()
        self.xml_file=""
       
        messg="Test Suit - Native Test App"
        self.button=Button(frame,text=messg,fg='red',bg='lightblue',font=('times',20,'italic')).grid(pady=8,padx=15)#pack(side=LEFT)



        self.hi_there = Button(frame, text="Check Compitability",fg='green',font=('times',18), command=self.say_hi)
        self.hi_there.grid(row=1,column=0,sticky=W)#pack(side=LEFT
        
        
        self.quit1=Button(frame,text="QUIT", fg="red",bg='orange',font=('times',18),command=frame.quit)
        self.quit1.grid(row=2,column=1,sticky=E,pady=8)#pack(side=LEFT)
        self.hi_there = Button(frame, text="Load Test Case",fg='green',bg='lightyellow',font=('times',18), command=self.Load_case)
        self.hi_there.grid(row=2,column=0,pady=10,sticky=W)#pack(side=LEFT)
        self.button1=Button(frame,text="Start",fg='red',bg='lightgreen',font=('times',18),command=self.startTest)
        self.button1.grid(row=3,pady=5)#pack(side=LEFT)
        #self.check1=Checkbutton(frame, text="[-s sensor or --sensor=]", variable=self.var1).grid(row=3, sticky=W)
        #self.var2 = IntVar()
        #self.check2=Checkbutton(frame, text="[-e event type or --event=]", variable=self.var2).grid(row=4,sticky=W)
        
        
    def say_hi(self):
        status="Status: install ok installed\n"
        found=0
        tt=os.system("dpkg -s libxml > some.txt")
        with open("some.txt",'r') as file:
            for line in file:
                if status in line:
                    found=1
        
        if found ==1:

            print("Package is already installed, Please Load Test Cases")
        else:
            showerror("Error","libxml2 package not found")
            print("package not installed, Please Installed libxml2 ")
        
    def startTest(self):
        print "hi test started"
        #print "variable is", self.var1.get()
        os.chdir(path_to_native)
        os.system("./native_app -f "+ self.xml_file)
        ''' if self.var1.get()==1:
            print("Test will execute as \"./native_app  [-s sensor or --sensor=]\"")
            os.chdir(path_to_native)
            os.system("./native_app -s "+ self.xml_file)
        
        if self.var2.get()==1:
            print("Test will execute as \" ./native_app  [-e event type or --event=]\"")
            os.chdir(path_to_native)
            os.system("./native_app -e "+ self.xml_file)
        '''
    def Load_case(self):
        root.filename = tkFileDialog.askopenfilename(initialdir = "/home/user",title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
        self.xml_file=root.filename
        print (self.xml_file)
        print "Test cases loaded successfully"

        


root=tk.Tk()
root1=Frame(root,height=500,width=600,bg='lightblue')
root1.pack_propagate(0)
root1.pack()
app=App(root1)
root.mainloop()
        
