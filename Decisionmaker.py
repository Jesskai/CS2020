# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:16:12 2020

@author: silve
"""
#Importing tkinter and setting window parameters
import tkinter as tk
window = tk.Tk()
window.title("Decision Maker App")
window.geometry("500x200")


#Creating a class b/c sometimes tkinter has conniption fits when you call a function w/out a class
class App():
    
    #__init__ defines the class variables so they can be used across the class
    def __init__(self):
        self.Name = ''
        self.years = 1
        self.titleText = ""
        self.lblText = ""
        self.btnText = ""
        self.aapl = False
    
    '''
    #Updates the screen - thanks to the nature of tkinter and this program, 
    adding the function actually makes the code longer, but it was on the rubric
    '''
    def updateScreen(self):
        lblStart["text"] = self.titleText
        
        '''
        Theoretically, x.lblText should return the same as self.lblText, 
        and the same as App.lblText, but only one of them ever work.
        '''
        lblName["text"] = x.lblText
        entName.delete("0", tk.END)
        btnYes["text"] = self.btnText
    
   
    
   
    #Beginning program, called at program initialization and restart
    def begin(self):        
       btnYes.pack_forget() 
       self.titleText =  "What operating system should you choose? \n Please enter your name."
       '''
       In another example of classes being weird, the next line worked once with 'self.lblText',
       but it broke when you hit the restart button. Now, it works every time.       
       '''
       x.lblText = "Name:"
       lblName.pack(side = tk.LEFT)
       entName.pack()
       App.updateScreen(self)
       window.bind("<Return>", lambda x: App.yrs(self))
       
       
    
    #Basically a setScreen() command - in tkinter, events call already defined functions
    def hardware(self):
        self.titleText = "Do you have apple hardware?"
        lblName.pack_forget()
        entName.pack_forget()
        btnYes.pack(side = tk.LEFT)
        btnNo.pack()
        btnYes.bind("<Button-1>", lambda x: App.apple(self))
        btnNo.bind("<Button-1>", lambda x: App.WvL(self))
        window.unbind("<Return>") 
        self.years = float(entName.get())
        self.btnText = "Yes"
        App.updateScreen(self)
        
        
    # about equal to setScreen("Years")
    def yrs(self):
        x.Name = entName.get()
        x.lblText = "Years:"
        self.titleText = "How many years of programming \n experience do you have?"
        window.bind("<Return>", App.hardware)
        App.updateScreen(self)      
                
        
     #Another setScreen function   
    def apple(self):
        self.titleText = "You have to use MacOS, " + x.Name + "; the current version is called Mojave."
        self.btnText = "Restart?"
        btnNo.pack_forget()
        App.updateScreen(self)
        btnYes.bind("<Button-1>", lambda x: App.begin(self))
        self.aapl = True
        
    
    
    #Sets either a windows or linux screen
    def WvL(self):
        self.aapl = False
        btnNo.pack_forget()
        self.btnText = "Restart?"
        btnYes.bind("<Button-1>", lambda x: App.begin(self))
        if self.years >= 1 and self.aapl == False:
            self.titleText = x.Name, "You should install Linux!"
            
        else:
            self.titleText = x.Name, "You should install Windows!"
        App.updateScreen(self)
        
   

#I had to add this line in to get some class calls to work - no clue why
x= App()     
    
# Window dressing & geometry; phrases in parens signify master window or frame
fr1 = tk.Frame(window)
fr2 = tk.Frame(window)
lblStart = tk.Label(fr1)
lblName = tk.Label(fr2)
entName = tk.Entry(fr2)
btnYes = tk.Button(fr2, text = "Yes")
btnNo = tk.Button(fr2, text = "No")

#Putting the widgets that never change on screen
fr1.pack()
fr2.pack()
lblStart.pack()

#Calling functions with x because "App." won't work for some reason
x.begin()
x.updateScreen()

#This command handles all the frame updating and drawing
window.mainloop()
