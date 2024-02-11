import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: if_06bis
---
Enunciado:

A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parametros:

Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Altura")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_altura = customtkinter.CTkEntry(master=self)
        self.txt_altura.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, padx=30, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        text_altura = self.txt_altura.get()
        altura = float(text_altura)

        if (altura < 160 ):
            alert("Base", "La posición es Base")

        if (altura > 159 and altura < 180):
            alert("Escolta", "La posición es escolta")

        if (altura > 179 and altura < 200 ):
            alert("Alero","La posición es alero")
        if ( altura >= 200):
            alert("Ala pivot", "La posición es ala-pívot o pívot")   


        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()