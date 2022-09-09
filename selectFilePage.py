from tkinter import *
from tkinter import filedialog
from XMLtoXCEL import xmlToExcel
from tkinter import messagebox


filePATH = 'test'

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    
    xmlToExcel(str(filename),filename[filename.rindex('/')+1:])

    messagebox.showinfo("Success !!","Xml to Excel is done !")
    
def secondPage():
    w = Tk()


    # Using piece of code from old splash screen
    width_of_window = 800
    height_of_window = 600
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %
            (width_of_window, height_of_window, x_coordinate, y_coordinate))
    w.configure(width=800, height=600)
    w.title("Python GUI App")
    Frame(w, width=800, height=600, bg='#272727').place(x=0, y=0)
    label1 = Label(w, text='Welcome to XML to EXCEL convertor',
                fg='white', bg='#272727')  # decorate it
    # You need to install this font in your PC or try another one
    label1.configure(font=("Game Of Squids", 20, "bold"))
    label1.place(x=40, y=90)

    label2 = Label(w, text='ayoub SMO', fg='white', bg='#272727')  # decorate it
    label2.configure(font=("Calibri", 6))
    label2.place(x=30, y=560)

    label3 = Button(w,bd=0,
    relief="groove",
    bg="white",
    fg="black",
    activeforeground="black",
    activebackground="white",
    font="arial 30",
    pady=1, text='Open XML', command=UploadAction)
    label3.place(x=300, y=300)

    w.mainloop()

