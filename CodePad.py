import tkinter
import webbrowser
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *



class Notepad: 
  
    __root = Tk()
    
     
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisFontMenu = Menu(__thisMenuBar, tearoff=0)
      
     
    __thisScrollBar = Scrollbar(__thisTextArea)      
    __file = None
    
    
    def __init__(self,**kwargs): 
  
         
        try: 
                self.__root.wm_iconbitmap("Notepad.ico")  
        except: 
                pass
  
        
  
        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
  
        
        self.__root.title("Untitled - Codepad") 
  
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight()
      
         
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
         
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))  
  
             
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1) 
  
        
        self.__thisTextArea.grid(sticky = N + E + S + W) 
          
      
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)     
          
        
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
          
       
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)     
  
                 
        self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)      
          
          
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)              
      
             
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)          
          
         
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)          
          
         
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)      
          
        
        self.__thisHelpMenu.add_command(label="About Codepad", 
                                        command=self.__showAbout)
        self.__thisHelpMenu.add_command(label="Release Notes", 
                                        command=self.__releaseNotes)
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu)
        self.__thisFontMenu.add_command(label="Comic Sans MS", 
                                        command=self.__fontSans)
        self.__thisFontMenu.add_command(label="Lazer 84", 
                                        command=self.__fontLazer)
        self.__thisFontMenu.add_command(label="Helvetica", 
                                        command=self.__fontHelvetica)
        self.__thisFontMenu.add_command(label="Goose Invasion", 
                                        command=self.__fontGoose)
        self.__thisFontMenu.add_separator()
        self.__thisFontMenu.add_command(label="Font Size 8px", 
                                        command=self.__font8px)
        self.__thisFontMenu.add_command(label="Font Size 16px", 
                                        command=self.__font16px)
        self.__thisFontMenu.add_command(label="Font Size 32px", 
                                        command=self.__font32px)
        self.__thisFontMenu.add_command(label="Font Size 48px", 
                                        command=self.__font48px)
        self.__thisMenuBar.add_cascade(label="Font Options", 
                                       menu=self.__thisFontMenu)
        
  
        self.__root.config(menu=self.__thisMenuBar) 
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
          
                 
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
        
          
    def __quitApplication(self): 
        self.__root.destroy() 
         
    def __releaseNotes(self):
        webbrowser.open('https://thecupofcaits.github.io/codepad.html')
    def __showAbout(self): 
        showinfo("Codepad","This is CodePad v0.4")

    def __fontSans(self): 

        global font; font = "comic sans ms"
        global text

        self.__thisTextArea.config(font=("Comic Sans MS",size))

    def __fontLazer(self):

        global text
        global font; font = "lazer84"
        
        self.__thisTextArea.config(font=("lazer84",size))

    def __fontGoose(self):

        global text
        global font; font = "Goosefont"
        
        self.__thisTextArea.config(font=("Goosefont",size))

    def __fontHelvetica(self):

        global text
        global font; font = "Helvetica"
        
        self.__thisTextArea.config(font=("Helvetica",size))

    def __font8px(self):
        self.__thisTextArea.config(font=(font,8))
        global size; size = "8"

    def __font16px(self):
        self.__thisTextArea.config(font=(font,16))
        global size; size = "16"

    def __font32px(self):
        self.__thisTextArea.config(font=(font,32))
        global size; size = "32"
    def __font48px(self):
        self.__thisTextArea.config(font=(font,48))
        global size; size = "48"
  
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt"),
                                                ("Python Scripts", "*.py"),
                                                ("Markdown Documents", "*.md"),
                                                ("JavaScript Files", "*.js"),
                                                ("HTML Documents", "*.html"),
                                                ("CSS Documents", "*.css"),
                                                ("CodeCode Script", "*.code"),
                                                ("Batch File", "*.bat"),
                                                ("GooseScript File", "*.honk"),
                                                ("Rich Text Document", "*.rtf")])
        
  
        if self.__file == "": 
              
             
            self.__file = None
        else: 
              
             
            self.__root.title(os.path.basename(self.__file) + " - Codepad") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self): 
        self.__root.title("Untitled - Codepad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END)
  
    def __saveFile(self): 
  
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt"), 
                                                 ("Python Scripts", "*.py"),
                                                 ("Markdown Documents", "*.md"),
                                                 ("JavaScript Files", "*.js"),
                                                 ("HTML Documents", "*.html"),
                                                 ("CSS Documents", "*.css"),
                                                ("CodeCode Script", "*.code"),
                                                ("Batch File", "*.bat"),
                                                ("GooseScript File", "*.honk"),
                                                ("Rich Text Document", "*.rtf")])
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
  
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 
  
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 
  
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>") 
  
    def run(self): 
        self.__root.iconbitmap('editor.ico')
        global font; font = "Helvetica"
        global size; size = "8"
        self.__root.mainloop()
  
  
  
   
notepad = Notepad(width=600,height=400)
notepad.run() 
