#Tkinter interface
from Tkinter import *

#class 
class Gui():
    #window
    window = Tk()
    window.wm_title("Customers")
    #customer text fields
    textFirstName = StringVar()
    textLastName  = StringVar()
    textEmail     = StringVar()
    textCpf       = StringVar()
    #customer labels
    labelFirstName = Label(window, text="First Name")
    labelLastName  = Label(window, text="Last Name")
    labelEmail     = Label(window, text="E-mail")
    labelCpf       = Label(window, text="CPF")
    #customer entry/input datas
    entryFirstName = Entry(window, textvariable=textFirstName)
    entryLastName  = Entry(window, textvariable=textLastName)
    entryEmail     = Entry(window, textvariable=textEmail)
    entryCpf       = Entry(window, textvariable=textCpf)
    #list all customers (Listbox)
    listCostumers = Listbox(window)
    #Scrollbar Listbox
    ScrollCostumers = Scrollbar(window)
    #Buttons
    buttonViewAll = Button(window, text="All Customers")
    buttonSearch  = Button(window, text="Search Customer")
    buttonInsert  = Button(window, text="New Customer")
    buttonUpdate  = Button(window, text="Update Customer")
    buttonDelete  = Button(window, text="Delete Customer")
    buttonClose   = Button(window, text="Close")
    #Grid / objects positions
    #labels
    labelFirstName.grid(row=0, column=0)
    labelLastName.grid(row=1, column=0)
    labelEmail.grid(row=2, column=0)
    labelCpf.grid(row=3, column=0)
    #entries
    entryFirstName.grid(row=0, column=1, padx=50, pady=50)
    entryLastName.grid(row=1, column=1)
    entryEmail.grid(row=2, column=1)
    entryCpf.grid(row=3,column=1)
    #list
    listCostumers.grid(row=0, column=2, rowspan=10)
    ScrollCostumers.grid(row=0, column=6, rowspan=10)
    #buttons
    buttonViewAll.grid(row=4, column=0, columnspan=2)
    buttonSearch.grid(row=5, column=0, columnspan=2)
    buttonInsert.grid(row=6, column=0, columnspan=2)
    buttonUpdate.grid(row=7, column=0, columnspan=2)
    buttonDelete.grid(row=8, column=0, columnspan=2)
    buttonClose.grid(row=9, column=0, columnspan=2)
    #configure Listbox Scrollbar
    listCostumers.configure(yscrollcommand=ScrollCostumers.set)
    ScrollCostumers.configure(command=listCostumers.yview)
    #padding
    x_pad = 5
    y_pad = 3
    width_entry = 30
    #SWAG
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    #main
    def run(self):
        Gui.window.mainloop()           