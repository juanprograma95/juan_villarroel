import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para limpiar el formulario
def limpiar_formulario():
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    clase_entry.delete(0, tk.END)
    seccion_entry.delete(0, tk.END)
    estado_inscripcion.set(None)
    for var in optativas_vars:
        var.set(0)
    comentarios_text.delete(1.0, tk.END)
    nivel_escolar.set('Seleccionar Nivel')

# Función para registrar estudiante
def registrar_estudiante():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    edad = edad_entry.get()
    clase = clase_entry.get()
    seccion = seccion_entry.get()
    estado = estado_inscripcion.get()
    nivel = nivel_escolar.get()
    comentarios = comentarios_text.get(1.0, tk.END).strip()
    optativas_seleccionadas = [materia for i, materia in enumerate(materias) if optativas_vars[i].get() == 1]
    
    detalles = (
        f"Nombre: {nombre}\n"
        f"Apellido: {apellido}\n"
        f"Edad: {edad}\n"
        f"Clase: {clase}\n"
        f"Sección: {seccion}\n"
        f"Estado de Inscripción: {estado}\n"
        f"Nivel Escolar: {nivel}\n"
        f"Materias Optativas: {', '.join(optativas_seleccionadas)}\n"
        f"Comentarios: {comentarios}"
    )
    
    messagebox.showinfo("Detalles del Estudiante", detalles)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Registro de Estudiantes - InnovadoresX")

# Frame para la información personal
frame_personal = ttk.LabelFrame(root, text="Datos Personales")
frame_personal.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

ttk.Label(frame_personal, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
nombre_entry = ttk.Entry(frame_personal)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_personal, text="Apellido:").grid(row=1, column=0, padx=5, pady=5)
apellido_entry = ttk.Entry(frame_personal)
apellido_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_personal, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
edad_entry = ttk.Entry(frame_personal)
edad_entry.grid(row=2, column=1, padx=5, pady=5)

# Frame para detalles académicos
frame_academicos = ttk.LabelFrame(root, text="Detalles Académicos")
frame_academicos.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

ttk.Label(frame_academicos, text="Clase:").grid(row=0, column=0, padx=5, pady=5)
clase_entry = ttk.Entry(frame_academicos)
clase_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_academicos, text="Sección:").grid(row=1, column=0, padx=5, pady=5)
seccion_entry = ttk.Entry(frame_academicos)
seccion_entry.grid(row=1, column=1, padx=5, pady=5)

# Frame para estado de inscripción
frame_inscripcion = ttk.LabelFrame(root, text="Estado de Inscripción")
frame_inscripcion.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

estado_inscripcion = tk.StringVar()
ttk.Radiobutton(frame_inscripcion, text="Inscrito", variable=estado_inscripcion, value="Inscrito").grid(row=0, column=0, padx=5, pady=5)
ttk.Radiobutton(frame_inscripcion, text="No Inscrito", variable=estado_inscripcion, value="No Inscrito").grid(row=0, column=1, padx=5, pady=5)

# Frame para materias optativas
frame_optativas = ttk.LabelFrame(root, text="Materias Optativas")
frame_optativas.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

materias = ["Matemáticas", "Ciencias", "Historia", "Deportes"]
optativas_vars = [tk.IntVar() for _ in materias]
for i, materia in enumerate(materias):
    ttk.Checkbutton(frame_optativas, text=materia, variable=optativas_vars[i]).grid(row=i, column=0, padx=5, pady=5, sticky="w")

# Frame para comentarios adicionales
frame_comentarios = ttk.LabelFrame(root, text="Comentarios Adicionales")
frame_comentarios.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

ttk.Label(frame_comentarios, text="Comentarios:").grid(row=0, column=0, padx=5, pady=5)
comentarios_text = tk.Text(frame_comentarios, height=4, width=40)
comentarios_text.grid(row=1, column=0, padx=5, pady=5)

# Menú desplegable para nivel escolar
ttk.Label(root, text="Nivel Escolar:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
nivel_escolar = tk.StringVar(value="Seleccionar Nivel")
nivel_menu = ttk.OptionMenu(root, nivel_escolar, "Seleccionar Nivel", "Primaria", "Secundaria")
nivel_menu.grid(row=6, column=0, padx=10, pady=5, sticky="ew")

# Botones de acción
frame_botones = ttk.Frame(root)
frame_botones.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

ttk.Button(frame_botones, text="Registrar Estudiante", command=registrar_estudiante).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_botones, text="Limpiar", command=limpiar_formulario).grid(row=0, column=1, padx=5, pady=5)

root.mainloop()
