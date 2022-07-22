import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        

        #This is the text above the entry box
        self.lbl_1 = tk.Label(self.master,text='Enter custom HTML and click submit, or click the Default HTML page button', font=16)
        self.lbl_1.grid(row=0, column=1, columnspan=2,
                             padx=(10, 10), pady=(10, 0))

        
        # Creates entry for website selection
        self.custom_text = Entry(width=75)
        # Positions entry into GUI using tkinter grid() padx and pady are
        # the same as the button to ensure they will line up
        self.custom_text.grid(row=1, column=1, columnspan=2,
                             padx=(10, 10), pady=(10, 0))


        #This is the Default HTML button
        self.btn = Button(
            self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row = 2, column = 1,padx=(10, 10), pady=(10, 10))

        #This is the Submit custom text button
        self.btn = Button(
            self.master, text="Submit Custom HTML", width=30, height=2, command=self.customHTML)
        self.btn.grid(row = 2, column = 2,padx=(10, 10), pady=(10, 10))


        # Creates an exit button
        self.exit_btn = Button(text="Exit", width=65, height=2, bg="light blue",
                               command=self.exit_program)
        # position the exit button
        self.exit_btn.grid(row=3, column=1, columnspan=2 , padx=(10, 10), pady=(0, 15))


    def get_data(self):
        label.config(text= entry.get(), font= ('Helvetica 16'))

        entry = Entry(self, width= 42)
        entry.place(relx= .5, rely= .5, anchor= CENTER)

        
        #This will send you to a default website when you click on the Default HTML button
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "<h1>\n<body>\n<html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    
        #This will send you to the website with custom text enteredyou entered
    def customHTML(self):
        htmlText=self.custom_text.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "<h1>\n<body>\n<html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        # Creates function to exit program
    def exit_program(self):
        # root is the main GIU window, the Tkinter destroy method
        # tells Python to terminate root.mainloop and all widgets in the GUI
        # window
        root.destroy()

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
