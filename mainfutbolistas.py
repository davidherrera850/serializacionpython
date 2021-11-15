from futbolistas import futbolista
from tkinter import *
from tkinter import ttk


def anadir():
    tabla.insert("", 'end',text = "", values=(txtNombre.get(),txtEquipo.get(),txtPosicion.get(),int(txtDorsal.get())))
def borrar():
    selected_item = tabla.selection()[0]
    tabla.delete(selected_item)
def modificar():
    selected_item = tabla.selection()[0]
    tabla.item(selected_item, text="", values=(txtNombre.get(),txtEquipo.get(),txtPosicion.get(),int(txtDorsal.get())))
def guardar():
    conten = ""
    mania=""
    for fila in tabla.get_children():
        for registro in tabla.item(fila)['text'], tabla.item(fila)['values']:
            conten = str(registro)
            mania = str(mania) + "" + str(conten) + "\n"
    archivo = open("Prueba.txt", "w")
    archivo.writelines(str(mania))
    archivo.close()
if __name__ == "__main__":
    cuadro = Tk()
    cuadro.geometry("830x500")
    label = Label(cuadro, text="FUTBOLISTAS")
    label.pack()
    label.config(fg="red",  # Foreground
                 bg="yellow",  # Background
                 font=("Verdana", 20))
    label = Label(cuadro, text="Nombre")
    label.pack()
    label.place(x=0,y=60)
    txtNombre=Entry(cuadro)
    txtNombre.place(x=60,y=60)
    label = Label(cuadro, text="Equipo")
    label.pack()
    label.place(x=0, y=90)
    txtEquipo = Entry(cuadro)
    txtEquipo.place(x=60, y=90)
    label = Label(cuadro, text="Posicion")
    label.pack()
    label.place(x=0, y=120)
    txtPosicion = Entry(cuadro)
    txtPosicion.place(x=60, y=120)
    label = Label(cuadro, text="Dorsal")
    label.pack()
    label.place(x=0, y=150)
    txtDorsal = Entry(cuadro)
    txtDorsal.place(x=60, y=150)
    cuadro.config(width=300, height=200)
    cuadro.title("Botón en Tk")
    botonanadir = ttk.Button(text="Añadir",command=anadir)
    botonanadir.place(x=50, y=200)
    cuadro.config(width=300, height=200)
    cuadro.title("Botón en Tk")
    botonborrar = ttk.Button(text="Borrar",command=borrar)
    botonborrar.place(x=140, y=200)
    cuadro.config(width=300, height=200)
    cuadro.title("Botón en Tk")
    botonmodificar = ttk.Button(text="Modificar",command=modificar)
    botonmodificar.place(x=230, y=200)
    cuadro.config(width=300, height=200)
    cuadro.title("Botón en Tk")
    botonguardar = ttk.Button(text="Guardar", command=guardar)
    botonguardar.place(x=320, y=200)
    tabla = ttk.Treeview(cuadro,columns=("Nombre","Equipo","Posicion","Dorsal"),show="headings")
    tabla.heading("#1", text="Nombre")
    tabla.heading("#2", text="Equipo")
    tabla.heading("#3", text="Posicion")
    tabla.heading("#4", text="Dorsal")
    tabla.place(x=10, y=250)
    cuadro.mainloop()

