#Import Modul dan Pustaka Yang Diperlukan
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#Kelas Editor Teks
class EditorTeks:
    #Fungsi Inisialisasi
    def __init__(self, window):
        #Inialisasi Window
        self.window = window
        self.window.title("Makrohard Word")
        self.window.geometry("1280x720")
        self.filename = None
        self.title = StringVar()
        self.status = StringVar()

        #Pembentukan Label Judul
        self.titlebar = Label(self.window,textvariable=self.title,font=("roboto",15,"bold"),bd=2,relief=GROOVE)
        self.titlebar.pack(side=TOP,fill=BOTH)
        self.settitle()

        #Pembentukan Label Status
        self.statusbar = Label(self.window,textvariable=self.status,font=("roboto",15,"bold"),bd=2,relief=GROOVE)
        self.statusbar.pack(side=BOTTOM,fill=BOTH)
        self.status.set("Selamat Datang")

        #Pembuatan Tombol-tombol
        self.newbutton = Button(self.window, text="new", bg="green", fg="white", height=100, width=100, command=self.newfile).place(relx=0.0, rely=0.05, relwidth=0.1, relheight=0.05)
        self.openbutton = Button(self.window, text="open", bg="green", fg="white", height=100, width=100, command=self.openfile).place(relx=0.0, rely=0.1, relwidth=0.1, relheight=0.05)
        self.savebutton = Button(self.window, text="save", bg="green", fg="white", height=100, width=100, command=self.savefile).place(relx=0.0, rely=0.15, relwidth=0.1, relheight=0.05)
        self.saveasbutton = Button(self.window, text="save as", bg="green", fg="white", height=100, width=100, command=self.saveasfile).place(relx=0.0, rely=0.2, relwidth=0.1, relheight=0.05)
        self.exitbutton = Button(self.window, text="exit", bg="red", fg="white", height=100, width=100, command=self.window.destroy).place(relx=0.0, rely=0.9, relwidth=0.1, relheight=0.05)

        #Pembuatan Area Ketik
        scroll = Scrollbar(self.window,orient=VERTICAL)
        self.txtarea = Text(self.window,yscrollcommand=scroll.set,font=("times new roman",12,"normal"),state="normal", bg="white",relief=GROOVE)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.txtarea.yview)
        self.txtarea.place(relx=0.1, rely=0.05, relwidth=1.0, relheight=0.9)

    #Fungsi Setter Judul
    def settitle(self):
        if self.filename:
          self.title.set(self.filename)
        else:
          self.title.set("Untitled")

    #Fungsi New
    def newfile(self,*args):
        self.txtarea.delete("1.0",END)
        self.filename = None
        self.settitle()
        self.status.set("File Baru Dibuat")

    #Fungsi Open
    def openfile(self,*args):
        self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        if self.filename:
            infile = open(self.filename,"r")
            self.txtarea.delete("1.0",END)
            for line in infile:
              self.txtarea.insert(END,line)
            infile.close()
            self.settitle()
            self.status.set("Sukses Dibuka")

    #Fungsi Save
    def savefile(self,*args):
        if self.filename:
            data = self.txtarea.get("1.0",END)
            outfile = open(self.filename,"w")
            outfile.write(data)
            outfile.close()
            self.settitle()
            self.status.set("Sukses Tersimpan")
        else:
            self.saveasfile()

    #Fungsi Save As
    def saveasfile(self,*args):
        untitledfile = filedialog.asksaveasfilename(title = "Menyimpan Sebagai",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        data = self.txtarea.get("1.0",END)
        outfile = open(untitledfile,"w")
        outfile.write(data)
        outfile.close()
        self.filename = untitledfile
        self.settitle()
        self.status.set("Sukses Tersimpan")


#Pembuatan Kontainer Tk, Penurunan, dan Pengulangan
word = Tk()
EditorTeks(word)
word.mainloop()
