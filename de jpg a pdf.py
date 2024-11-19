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
    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        image = image.convert('RGB')

        # Convertir la imagen a bytes y agregarla al PDF
        with open(image_path, 'rb') as img_file:
            img_bytes = img_file.read()

        pdf.add_page()
        pdf.image(image_path, 10, 10, pdf.w - 20)

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
