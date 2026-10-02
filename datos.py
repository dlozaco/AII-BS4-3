from tkinter import messagebox

def cargar():
    respuesta = messagebox.askyesno(
        title="Confirmar",
		message="¿Está seguro que quiere recargar los datos?\n"
    )
    if respuesta:
        almacenardb()

def almacenardb():
    