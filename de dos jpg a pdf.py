import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Documento PDF Generado', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf_from_images(image_folder, output_path):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Obtener y ordenar las imágenes por nombre de archivo numérico
    image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))],
                         key=lambda x: int(os.path.splitext(x)[0]))

    image_count = len(image_files)
    
    for i in range(0, image_count, 2):  # Procesar de dos en dos
        image_file1 = image_files[i]
        image_path1 = os.path.join(image_folder, image_file1)
        image1 = Image.open(image_path1)
        image1 = image1.convert('RGB')

        # Añadir página
        pdf.add_page()

        # Primer imagen (arriba)
        pdf.image(image_path1, 10, 10, pdf.w - 20)

        # Comprobar si hay una segunda imagen
        if i + 1 < image_count:
            image_file2 = image_files[i + 1]
            image_path2 = os.path.join(image_folder, image_file2)
            image2 = Image.open(image_path2)
            image2 = image2.convert('RGB')

            # Segunda imagen (abajo)
            pdf.image(image_path2, 10, pdf.h / 2 + 10, pdf.w - 20)

    pdf.output(output_path)

def main():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    folder_path = filedialog.askdirectory(title="Selecciona la carpeta con imágenes JPG")
    if not folder_path:
        messagebox.showerror("Error", "No se seleccionó ninguna carpeta.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_path:
        messagebox.showerror("Error", "No se seleccionó una ubicación para guardar el PDF.")
        return

    try:
        create_pdf_from_images(folder_path, output_path)
        messagebox.showinfo("Éxito", f"El archivo PDF se guardó correctamente en: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el PDF: {str(e)}")

if __name__ == "__main__":
    main()
import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Documento PDF Generado', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf_from_images(image_folder, output_path):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Obtener y ordenar las imágenes por nombre de archivo numérico
    image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))],
                         key=lambda x: int(os.path.splitext(x)[0]))

    image_count = len(image_files)
    
    for i in range(0, image_count, 2):  # Procesar de dos en dos
        image_file1 = image_files[i]
        image_path1 = os.path.join(image_folder, image_file1)
        image1 = Image.open(image_path1)
        image1 = image1.convert('RGB')

        # Añadir página
        pdf.add_page()

        # Primer imagen (arriba)
        pdf.image(image_path1, 10, 10, pdf.w - 20)

        # Comprobar si hay una segunda imagen
        if i + 1 < image_count:
            image_file2 = image_files[i + 1]
            image_path2 = os.path.join(image_folder, image_file2)
            image2 = Image.open(image_path2)
            image2 = image2.convert('RGB')

            # Segunda imagen (abajo)
            pdf.image(image_path2, 10, pdf.h / 2 + 10, pdf.w - 20)

    pdf.output(output_path)

def main():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    folder_path = filedialog.askdirectory(title="Selecciona la carpeta con imágenes JPG")
    if not folder_path:
        messagebox.showerror("Error", "No se seleccionó ninguna carpeta.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_path:
        messagebox.showerror("Error", "No se seleccionó una ubicación para guardar el PDF.")
        return

    try:
        create_pdf_from_images(folder_path, output_path)
        messagebox.showinfo("Éxito", f"El archivo PDF se guardó correctamente en: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el PDF: {str(e)}")

if __name__ == "__main__":
    main()
