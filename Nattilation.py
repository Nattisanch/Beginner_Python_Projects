from tkinter import *
from tkinter.ttk import *
from tkinter import Button
from googletrans import Translator, LANGUAGES
from tkinter import ttk, messagebox

root = Tk()
root.title("Nattilation")
root.geometry('1200x420')
root.configure(bg='#D2C2D6')

lang = LANGUAGES 
lang_list = list(lang.values())


text_style = {'font': ('Helvetica', 12), 'bg': '#ffffff', 'fg': '#000000', 'bd': 2, 'relief': 'solid'}

original_lang = Text(root, height=10, width=40, **text_style)
original_lang.grid(column=0, row=0, pady=20, padx=10)

translated_text = Text(root, height=10, width=40, **text_style)
translated_text.grid(column=2, row=0, pady=20, padx=10)


combobox_style = {'width': 50, 'font': ('Helvetica', 12)}

original_comb = ttk.Combobox(root, values=lang_list, **combobox_style)
original_comb.current(21)
original_comb.grid(column=0, row=1, pady=10, padx=10)

translated_combo = ttk.Combobox(root, values=lang_list, **combobox_style)
translated_combo.current(26)
translated_combo.grid(column=2, row=1, pady=10, padx=10)

def translate_text():
    translator = Translator()
    try:
        src_lang = list(lang.keys())[list(lang.values()).index(original_comb.get())]
        dest_lang = list(lang.keys())[list(lang.values()).index(translated_combo.get())]
        text_to_translate = original_lang.get("1.0", END).strip()

        if not text_to_translate:
            raise ValueError("No text to translate")

        translated = translator.translate(text_to_translate, src=src_lang, dest=dest_lang)
        if translated is None or translated.text is None:
            raise ValueError("Translation failed")

        translated_text.delete("1.0", END)
        translated_text.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def clear_text():
    original_lang.delete("1.0", END)
    translated_text.delete("1.0", END)


button_style = {'font': ('Helvetica', 24), 'bg': '#957c92', 'fg': '#ffffff', 'bd': 2, 'relief': 'raised'}

translate_btn = Button(root, text="Translate", command=translate_text, **button_style)
translate_btn.grid(column=1, row=0, padx=10, pady=10)

clear_btn = Button(root, text="Clear", font=('Helvetica', 14), command=clear_text, bg='#957c92', fg='#ffffff', bd=2, relief='raised')
clear_btn.grid(column=1, row=2, padx=10, pady=10)

root.mainloop()
