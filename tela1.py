#Tela1.py
import tkinter as tk
#criar uma instancia de uma janela
janela = tk.Tk()


janela.title("bem vindo ao Tkinter")

label = tk.Label(janela, text="esse e um label" , font=('arial Bold', 70))

label.grid(column=0, row = 0)

janela.mainloop()

