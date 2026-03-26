import tkinter as tk
from tkinter import messagebox

# ---------- función modal ----------
def abrir_login():
    modal = tk.Toplevel(ventana)
    modal.title("Login")
    modal.geometry("300x200")
    modal.resizable(False, False)

    # 🔒 hacerla modal
    modal.transient(ventana)
    modal.grab_set()

    tk.Label(modal, text="Usuario:").pack(pady=5)
    entry_user = tk.Entry(modal)
    entry_user.pack()

    tk.Label(modal, text="Contraseña:").pack(pady=5)
    entry_pass = tk.Entry(modal, show="*")
    entry_pass.pack()

    def validar():
        if entry_user.get() == "admin" and entry_pass.get() == "1234":
            messagebox.showinfo("Login", "Acceso correcto")
            modal.destroy()
        else:
            messagebox.showerror("Login", "Datos incorrectos")

    tk.Button(modal, text="Ingresar", command=validar).pack(pady=10)
    tk.Button(modal, text="Cancelar", command=modal.destroy).pack()

    # centrar ventana (opcional profesional)
    centrar(modal)

# ---------- centrar ventana ----------
def centrar(win):
    win.update_idletasks()
    ancho = win.winfo_width()
    alto = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (ancho // 2)
    y = (win.winfo_screenheight() // 2) - (alto // 2)
    win.geometry(f"{ancho}x{alto}+{x}+{y}")

# ---------- ventana principal ----------
ventana = tk.Tk()
ventana.title("App principal")
ventana.geometry("400x300")

tk.Button(ventana, text="Abrir Login Modal", command=abrir_login).pack(pady=50)

ventana.mainloop()