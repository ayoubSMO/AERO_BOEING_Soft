from tkinter import *
from tkinter import filedialog
from XMLtoXCEL import xmlToExcel
from tkinter import messagebox
from tkinter import *
from TkinterDnD2 import *

filePATH = 'test'

var = StringVar()

def drop(event):
    var.set(event.data)

def open_text_file():
    w = Tk()
    text = Text(w, height=12)
    text.grid(column=0, row=0, sticky='nsew')
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())
    
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
    w.title("XML to EXCEL convertor")
    Frame(w, width=800, height=600, bg='#272727').place(x=0, y=0)
    label1 = Label(w, text='Welcome to XML to EXCEL convertor',
                fg='white', bg='#272727')  # decorate it
    # You need to install this font in your PC or try another one
    label1.configure(font=("Game Of Squids", 20, "bold"))
    label1.place(x=40, y=90)

    label2 = Label(w, text='', fg='white', bg='#272727')  # decorate it
    label2.configure(font=("Calibri", 6))
    label2.place(x=30, y=560)

    ws = TkinterDnD.Tk()
    ws.title('PythonGuides')
    ws.geometry('300x200')
    ws.config(bg='#fcba03')

    var = StringVar()
    Label(ws, text='Path of the Folder', bg='#fcba03').pack(anchor=NW, padx=10)
    e_box = Entry(ws, textvar=var, width=80)
    e_box.pack(fill=X, padx=10)
    e_box.drop_target_register(DND_FILES)
    e_box.dnd_bind('<<Drop>>', drop)

    lframe = LabelFrame(ws, text='Instructions', bg='#fcba03')
    Label(
        lframe, 
        bg='#fcba03',
        text='Drag and drop the folder \nof your choice in the above text field.\n You will notice a path over there.'
        ).pack(fill=BOTH, expand=True)
    lframe.pack(fill=BOTH, expand=True, padx=10, pady=10)

    w.mainloop()