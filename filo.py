from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
xml_file="/home/user/team" 
root = Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = xml_file,title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
print (root.filename)
