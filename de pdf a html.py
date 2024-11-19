import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF

# Función para convertir el PDF a HTML
def pdf_to_html(pdf_path, html_output):
    try:
        # Abrir el archivo PDF
        doc = fitz.open(pdf_path)
        
        # Crear una variable para almacenar el contenido HTML
        html_content = ""

        # Extraer el texto en formato HTML de cada página
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Cargar la página
            html_content += page.get_text("html")  # Obtener el texto en formato HTML

        # Guardar el contenido HTML en un archivo
        with open(html_output, "w", encoding="utf-8") as f:
            f.write(html_content)

        messagebox.showinfo("Éxito", f"PDF convertido a HTML correctamente y guardado como {html_output}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Función para seleccionar el archivo PDF
def select_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    if pdf_path:
        html_output = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("Archivos HTML", "*.html")])
        if html_output:
            pdf_to_html(pdf_path, html_output)

# Crear la ventana principal
root = tk.Tk()
root.title("Convertir PDF a HTML")

# Establecer tamaño de la ventana
root.geometry("300x150")

# Crear un botón para seleccionar y convertir el archivo
btn_convertir = tk.Button(root, text="Convertir PDF a HTML", command=select_pdf)
btn_convertir.pack(pady=30)

# Ejecutar la interfaz
root.mainloop()
