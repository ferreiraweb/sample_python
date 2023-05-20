import tkinter as tk

# from tkinter import ttk

# janela = tk.Tk()
# janela.title("Aplicação GUI")
# janela.resizable(False, False)

# ttk.Label(janela, text="Componente label").grid(column=10, row=20)

# --- -----------------

contador = 0


def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)
        funcao_contar()


janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem',
                    width=50, command=janela.destroy)
btnAcao.pack()


janela.mainloop()
