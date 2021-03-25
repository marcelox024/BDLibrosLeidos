from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sqlite3
import os

# ==================FUNCIONES==================

def conexionBBDD():
    miConexion=sqlite3.connect("Base de Datos Libros")
    
    miCursor=miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE LIBROS
            (
                ID              INTEGER         PRIMARY KEY     AUTOINCREMENT,
                TITULO          VARCHAR(350),
                AUTOR           VARCHAR(100),
                GENERO          VARCHAR(50),
                ANIO_PUB        INTEGER,
                PAIS            VARCHAR(50),
                ANIO_LEC        INTEGER
            )
        ''')

        messagebox.showinfo("Base de datos", "Base de datos creada con éxito.")

    except:
        messagebox.showwarning("¡Atención!", "La base de datos ya existe.")


def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if valor=="yes":
        root.destroy()


def limpiarCampos():
        miId.set("")
        miTitulo.set("")
        miAutor.set("")
        miGenero.set("")
        miAnioPub.set("")
        miPais.set("")
        miAnioLec.set("")


def insertar():
    miId.set("")

    miConexion=sqlite3.connect("Base de Datos Libros")

    miCursor=miConexion.cursor()

    datos=miTitulo.get(), miAutor.get(), miGenero.get(), miAnioPub.get(), miPais.get(), miAnioLec.get()
    miCursor.execute("INSERT INTO LIBROS VALUES(NULL,?,?,?,?,?,?)", (datos))

    miConexion.commit()

    messagebox.showinfo("Base de Datos", "Registro insertado con éxito.")


def consultar():
    miConexion=sqlite3.connect("Base de Datos Libros")

    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM LIBROS WHERE ID = " + miId.get())

    variosCampos=miCursor.fetchall()

    miTitulo.set("")
    miAutor.set("")
    miGenero.set("")
    miAnioPub.set("")
    miPais.set("")
    miAnioLec.set("")

    for i in variosCampos:
        miId.set(i[0])
        miTitulo.set(i[1])
        miAutor.set(i[2])
        miGenero.set(i[3])
        miAnioPub.set(i[4])
        miPais.set(i[5])
        miAnioLec.set(i[6])
    
    miConexion.commit()


def actualizar():
    miConexion=sqlite3.connect("Base de Datos Libros")

    miCursor=miConexion.cursor()

    datos=miTitulo.get(), miAutor.get(), miGenero.get(), miAnioPub.get(), miPais.get(), miAnioLec.get()
    miCursor.execute("UPDATE LIBROS SET TITULO=?, AUTOR=?, GENERO=?, ANIO_PUB=?, PAIS=?, ANIO_LEC=?" +
        "WHERE ID=" + miId.get(), (datos))

    miConexion.commit()

    messagebox.showinfo("Base de Datos", "Registro actualizado con éxito.")


def borrar():
    miConexion=sqlite3.connect("Base de Datos Libros")

    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM LIBROS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("Base de Datos", "Registro borrado con éxito.")


def acercaDe():
    messagebox.showinfo("Acerca de...", "Este formulario y la base de datos fueron creados por\nMarcelo Gómez Peche.")


def img_resource_path(relative_path):
    """ Obtiene el path para los archivos externos ya sea para el archivo .py o .exe """
    try:
        # PyInstaller crea un folder temp y almacena el path en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# # ================BARRA DE MENU================

root=Tk()
root.resizable(0,0) # Esto significa "(False,False)"

barraMenu=Menu(root)

root.title("Formulario de Libros")

iconPath = img_resource_path("resources/libros_icono.ico")
root.iconbitmap(iconPath)
root.config(menu=barraMenu)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

limpiarMenu=Menu(barraMenu, tearoff=0)
limpiarMenu.add_command(label="Limpiar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Ingresar", command=insertar)
crudMenu.add_command(label="Consultar",command=consultar)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=borrar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de...", command=acercaDe)


barraMenu.add_cascade(label="Base de Datos", menu=bbddMenu)
barraMenu.add_cascade(label="Limpiar", menu=limpiarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# =====================TITULO=====================  

miFrame1=Frame(root)
miFrame1.pack()

miFuente = Font(family="Helvetica", size=15, weight="bold", slant="roman")

miTitForm=Label(miFrame1, text="LIBROS LEÍDOS POR\nMARCELO")
miTitForm.grid(row=0, column=0, padx=10, pady=3)
miTitForm.config(fg="blue", font=miFuente)

imagenPath = img_resource_path("resources/libros.gif")
miImagen=PhotoImage(file=imagenPath)
imagenLibro=Label(miFrame1, image=miImagen)
imagenLibro.grid(row=1, column=0, sticky="e", padx=10, pady=0)

# # ====================CAMPOS====================

miFrame2=Frame(root)
miFrame2.pack()

# -------------VARIABLES A ALMACENAR-------------
miId=StringVar()
miTitulo=StringVar()
miAutor=StringVar()
miGenero=StringVar()
miAnioPub=StringVar()
miPais=StringVar()
miAnioLec=StringVar()
# -----------------------------------------------

cuadroID=Entry(miFrame2, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="red")

cuadroTitulo=Entry(miFrame2, textvariable=miTitulo)
cuadroTitulo.grid(row=1, column=1, padx=10, pady=10)
cuadroTitulo.config(fg="green", justify="right")

cuadroAutor=Entry(miFrame2, textvariable=miAutor)
cuadroAutor.grid(row=2, column=1, padx=10, pady=10)

cuadroGenero=Entry(miFrame2, textvariable=miGenero)
cuadroGenero.grid(row=3, column=1, padx=10, pady=10)

cuadroAnioPub=Entry(miFrame2, textvariable=miAnioPub)
cuadroAnioPub.grid(row=4, column=1, padx=10, pady=10)

cuadroPais=Entry(miFrame2, textvariable=miPais)
cuadroPais.grid(row=5, column=1, padx=10, pady=10)

cuadroAnioLec=Entry(miFrame2, textvariable=miAnioLec)
cuadroAnioLec.grid(row=6, column=1, padx=10, pady=10)


# # ====================LABELS====================

idLabel=Label(miFrame2, text="Id:")
idLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

tituloLabel=Label(miFrame2, text="Título:")
tituloLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

autorLabel=Label(miFrame2, text="Autor:")
autorLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

generoLabel=Label(miFrame2, text="Género:")
generoLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

anioPubLabel=Label(miFrame2, text="Año de Publicación:")
anioPubLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

paisLabel=Label(miFrame2, text="País:")
paisLabel.grid(row=5, column=0, sticky="w", padx=10, pady=10)

anioLecLabel=Label(miFrame2, text="Año de Lectura:")
anioLecLabel.grid(row=6, column=0, sticky="w", padx=10, pady=10)


# # ====================BOTONES====================

miFrame3=Frame(root)
miFrame3.pack()

botonIngresar=Button(miFrame3, text="Ingresar", command=insertar)
botonIngresar.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonConsultar=Button(miFrame3, text="Consultar",command=consultar)
botonConsultar.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame3, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame3, text="Borrar", command=borrar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

# # =============CENTRAR LA VENTANA==============

window_height = 600
window_width = 300

screen_width = root.winfo_screenwidth() # Retorna el tamñana de la pantalla en píxeles 
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = (int((screen_height/2) - (window_height/2))) - 40

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

root.mainloop()

# # =============CREAR EL EJECUTABLE==============

# Crear el .spec (en consola):
# pyi-makespec --windowed --onefile --icon .\resources\icono_windows.ico formulario_libros_leidos.py

# Agregar en la lista datas (del archivo .spec):
# ('resources/libros.gif', 'resources'), ('resources/libros_icono.ico', 'resources')

# Crear el .exe una vez modificado el .spec (en la consola):
# pyintaller pyinstaller formulario_libros_leidos.spec
