from tkinter import *
from tkinter import ttk

mi_id =0

master = Tk ()

var_nombre = StringVar()
var_apellido = StringVar()
var_edad = IntVar()

nombre= Label(master, text="Nombre")
nombre.grid(row =0, column =0)

apellido =Label(master, text ="Apellido")
apellido.grid(row=1, column = 0)

edad = Label(master, text="Edad")
edad.grid(row=2, column=0)

nombre = Entry(master,textvariable=var_nombre, width=25)
nombre.grid(row=0, column=1)
 
apellido = Entry(master,textvariable=var_apellido, width=25)
apellido.grid(row=1, column=1)

edad = Entry(master,textvariable=var_edad, width=25)
edad.grid(row=2, column=1)

def funcion_g():
    global mi_id
    mi_id += 1
    tree.insert("","end", text=str(mi_id), values=(var_nombre.get(), var_apellido.get(), var_edad.get()))

def funcion_b():
    global mi_id
    item = tree.focus()
    print(item)
    tree.delete(item)
    mi_id -=1

tree = ttk.Treeview(master)
tree["columns"] = ("Col1", "Col2", "Col3", "Col4")
tree.column("#0", width=50, minwidth=50)
tree.column("Col1", width=80, minwidth=80)
tree.column("Col2", width=80, minwidth=80)
tree.column("Col3", width=100, minwidth=100)


tree.grid(column=0, row=4, columnspan=4)

boton_g= Button(master, text="Guardar", command=funcion_g)
boton_g.grid(row=2, column=2)

boton_f= Button(master, text="Borrar", command=funcion_g)
boton_f.grid(row=3, column=1)

master.mainloop()

