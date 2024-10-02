import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conectar a la base de datos
def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="SQL123*",
            database="semana8"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo conectar: {err}")
        return None

# Función para agregar un nuevo objeto a la base de datos
def agregar_objeto():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "INSERT INTO FaunaFlora (ID, NombreCientifico, Habitat, EstadoConservacion, RegionGeografica) VALUES (%s, %s, %s, %s, %s)"
            datos = (
                id_entry.get(),
                nombre_entry.get(),
                habitat_entry.get(),
                estado_entry.get(),
                region_entry.get()
            )
            cursor.execute(query, datos)
            conexion.commit()
            messagebox.showinfo("Éxito", "Objeto agregado correctamente")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo agregar: {err}")
        finally:
            cursor.close()
            conexion.close()
    else:
        messagebox.showerror("Error", "No se pudo establecer la conexión con la base de datos")

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Gestión de Fauna y Flora")

# Etiquetas y campos de entrada
tk.Label(root, text="ID").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Nombre Científico").grid(row=1, column=0)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=1, column=1)

tk.Label(root, text="Hábitat").grid(row=2, column=0)
habitat_entry = tk.Entry(root)
habitat_entry.grid(row=2, column=1)

tk.Label(root, text="Estado de Conservación").grid(row=3, column=0)
estado_entry = tk.Entry(root)
estado_entry.grid(row=3, column=1)

tk.Label(root, text="Región Geográfica").grid(row=4, column=0)
region_entry = tk.Entry(root)
region_entry.grid(row=4, column=1)

# Botón para agregar
agregar_btn = tk.Button(root, text="Agregar", command=agregar_objeto)
agregar_btn.grid(row=5, column=1)

root.mainloop()

