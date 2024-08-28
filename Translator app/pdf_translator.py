import fitz  # PyMuPDF
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog, messagebox
import time

#to translate a pdf my friend sent me I made this
 
def translate_text(text, retries=3):
    translator = Translator()
    for _ in range(retries):
        try:
            translated = translator.translate(text, dest='en')
            return translated.text
        except Exception as e:
            print(f"Retrying due to error: {e}")
            time.sleep(1)
    return None

def translate_pdf_to_english(pdf_path, output_path):
    document = fitz.open(pdf_path)
    translated_text = ""

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()
        if not text.strip():
            continue
        translated_page = translate_text(text)
        if translated_page:
            translated_text += translated_page + "\n"
        else:
            print(f"Error translating page {page_num}")

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)

    messagebox.showinfo("Success", f"Translation complete. Translated text saved to {output_path}")

def select_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if output_path:
            translate_pdf_to_english(pdf_path, output_path)


root = tk.Tk()
root.title("PDF Translator")


select_button = tk.Button(root, text="Select PDF", command=select_pdf)
select_button.pack(pady=20)


root.mainloop()
