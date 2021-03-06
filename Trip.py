# Jack Lawrence#
# Comp Prog#
# 10 22 18#

#Version 1.0.7 Fixed more bugs. Made submit show a window, made month box read only

#makes file
results_file = "tripinfo.txt"
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Pricing")
window.geometry('500x300')


# Clears all of the info
def clear():
    spval.set("Month")
    note.delete("1.0", END)
    options.set("Way of travel.")
    l.selection_clear(0, END)
    return

#writes all the info to a txt file
def submit():

    if l.curselection() ==() or options.get()=="Way of travel." or spval.get()=="Month":
        error()
    else:
        list = l.selection_get()
        opt = options.get()
        month = spval.get()
        noets = note.get("1.0", 'end-1c')
        str = "{} , {} , {}, {} \n".format(noets, month, list, opt)
        file = open(results_file, "a")
        file.write(str)
        file.close()
        infoadded()
        return

#sets up variables
options = StringVar()
spval = StringVar()
options.set("Way of travel.")

#sets up the combobox
optiones = ("Plane", "Train", "Automobile")
choices = ttk.Combobox(window, textvariable=options, state='readonly', values=optiones)
choices.bind("<<ComboboxSelected>>")
choices.grid(row=0, column=0, sticky=(N, W))

#sets up listbox
l = Listbox(window, height=10)
l.grid(column=0, row=2, sticky=(N, W))
l.bind("<<ListboxSelect>>")

#lists the countries
l.insert('end', 'United States')
l.insert('end', 'Japan')
l.insert('end', 'United Kingdom')
l.insert('end', 'China')
l.insert('end', 'Russia')
l.insert('end', 'South Korea')
l.insert('end', 'Panama')
l.insert('end', 'Poland')
l.insert('end', 'Hungary')
l.insert('end', 'Switzerland')
l.insert('end', 'Dubai')

#shows the about info
def showHelp():
    window2 = Toplevel(window, width=200, height=100)
    window2.title("About")
    Label(window2, text="'Trip Log Program' by Jack Lawrence in Mr Davis' Advanced Programming class \n"
          "Fill out all the values and it writes all of them into a txt file.").grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=40)

    window2.deiconify()
    return




#grids stuff
menubar = Menu(window)
fmenu = Menu(menubar)
fmenu.add_command(label="Save", command=submit)
fmenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=fmenu)
hmenu = Menu(menubar)
hmenu.add_command(label="About", command=showHelp)
menubar.add_cascade(label="Help", menu=hmenu)
window.config(menu=menubar)

listlable = ttk.Label(window, text="Country List")
listlable.grid(column=0, row=1, columnspan=1, rowspan=1, sticky='NSEW')
s = ttk.Scrollbar(window, orient=VERTICAL, command=l.yview)
s.grid(column=0, row=2, sticky=N + S + E)

l['yscrollcommand'] = s.set

ttk.Sizegrip().grid(column=999, row=999, sticky=(S, E))

notelable = ttk.Label(window, text="Description:")
notelable.grid(column=15, row=0, columnspan=1, rowspan=1, sticky='NSEW')

note = Text(window, height=10, width=30)
note.grid(column=1, row=1, columnspan=30, rowspan=30, sticky="NSEW")

Months = ['Janurary', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
spin = Spinbox(window,value=Months,textvariable=spval, state = 'readonly').grid(row=0,column=2, sticky='N')
spval.set("Month")

submit = Button(window, text="Submit", command=submit)
clear = Button(window, text="Clear", command=clear)
submit.grid(row=15, column=0, pady=5, sticky=W)
clear.grid(row=15, column=0, pady=10)

window.grid_rowconfigure((0), weight=1)
window.grid_columnconfigure((0), weight=1)
window.grid_rowconfigure((1), weight=1)
window.grid_columnconfigure((1), weight=1)
window.grid_columnconfigure((2), weight=1)
window.grid_rowconfigure((2), weight=1)
window.grid_rowconfigure((15), weight=1)
window.grid_columnconfigure((30), weight=1)
window.grid_rowconfigure((30), weight=1)

def infoadded():
    window4 = Toplevel(window, width=200, height=100)
    window4.title("Saved")
    Label(window4, text="Info Added To Text File").grid(row=0,
                                                                 column=0,
                                                                 padx=40)

    window4.deiconify()
    return

def error():
    window3 = Toplevel(window, width=200, height=100)
    window3.title("ERROR")
    Label(window3, text="ERROR: ALL FIELDS MUST BE FILLED").grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=40)

    window3.deiconify()
    return
#runs code
window.mainloop()