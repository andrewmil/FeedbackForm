from tkinter import *
from tkinter import messagebox
import tkinter

def feedbackValidation(feedback):
    ##### confirms that comment is under 1200 characters #####
    if (len(feedback)>1200):
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showwarning('Invalid Input', 'Please Limit your comment to 1200 characters')
        return True
    else:
        return False

def satisfactionValidation(satisfaction):
    ##### confirms that user has selected one of the radio button options #####
    if (satisfaction == "None"):
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showwarning('Invalid Input', 'Please select a satisfaction option')
        return True
    else:
        return False
