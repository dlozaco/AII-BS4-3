from tkinter import *

def main():

    def prueba():
        print("Prueba")

    root = Tk()
    root.geometry('600x400')

    menubar = Menu(root)

    databar = Menu(menubar, tearoff=0)
    databar.add_command(label="Cargar", command=prueba)
    databar.add_separator()
    databar.add_command(label="Salir", command=root.destroy)
    menubar.add_cascade(label="Datos", menu=databar)

    listarbar = Menu(menubar, tearoff=0)
    listarbar.add_command(label="Recetas", command=prueba)
    menubar.add_cascade(label="Listar", menu=listarbar)

    buscarbar = Menu(menubar, tearoff=0)
    buscarbar.add_command(label="Recetas por autor", command=prueba)
    buscarbar.add_command(label="Recetas por fecha", command=prueba)
    menubar.add_cascade(label="Buscar", menu=buscarbar)


    root.config(menu=menubar)
    root.mainloop()


if __name__ == "__main__":
    main()