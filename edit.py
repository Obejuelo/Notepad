from tkinter import *
from tkinter import filedialog as Filedialog
from io import open

ruta = ''  # La usaremos para almacenar la ruta del fichero

def nuevo():
    global ruta
    ruta = ''
    mensaje.set('Nuevo')
    texto.delete(1.0, 'end')  # Borramos desde el caracter 1 hasta el final
    root.title('Mi editor')

def abrir():
    global ruta
    mensaje.set('Abrir')
    ruta = Filedialog.askopenfilename(
        initialdir='../',
        filetype=(('Ficheros de texto', '*.txt'),),
        title='Abrir un documento de texto'
    )
    if ruta != '':
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + ' - mi editor')

def guardar():
    global ruta
    mensaje.set('Guardar')
    if ruta != '':
        # end-1c Corta hasta el final menos 1 caracter
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Fichero guardado')
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set('Guardar como')
    fichero = Filedialog.asksaveasfile(
        title='Guardar archivo',
        mode='w',
        defaultextension='.txt'
    )
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set('Archivo guardado de forma exitosa')
    else:
        mensaje.set('Error al guardar')
        ruta = ''

# Configuración de la raíz
root = Tk()
root.title('Editor de texto')

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Nuevo', command=nuevo)
filemenu.add_command(label='Abrir', command=abrir)
filemenu.add_command(label='Guardar', command=guardar)
filemenu.add_command(label='Guardar como', command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)
menubar.add_cascade(label='Archivo', menu=filemenu)
root.config(menu=menubar)

# Caja de texto dentral
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(font=('Open Sans', 11), padx=6, pady=4, bd=0)

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido')
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side='left')

root.mainloop()
