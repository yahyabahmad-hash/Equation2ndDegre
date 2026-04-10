import tkinter as tk
from tkinter import messagebox
from math import sqrt

def resoudre():
    try:
        a = float(entryA.get())
        b = float(entryB.get())
        c = float(entryC.get())
        if a != 0:
            delta = b**2 - 4*a*c
            if delta < 0 :
                sol = "L'équation n'admet pas de solutions en ℝ"
            elif delta == 0 :
                x = -b / (2*a)
                sol = "L'équation admet une solution unique: S = { "+str(x)+" }"
            else:
                x1 = (-b+sqrt(delta))/(2*a)
                x2 = (-b-sqrt(delta))/(2*a)
                sol = "L'équation admet deux solutions:\n\nS = { "+str(x1)+" ; "+str(x2)+" }"
            lblDelta["text"] = f"Δ = {delta}"
        else:
            lblDelta["text"] = "Votre équation est de 1er degré"
            if b!=0:
                x = -c/b
                sol= "L'équation admet une solution : S = { "+str(x)+" }"
            elif c != 0:
                sol = "L'équation n'admet pas de solutions en ℝ"
            else:
                sol = "Tout nombre en ℝ est une solutions de l'équation"
        lblSol["text"] = sol
    except ValueError:
        messagebox.showwarning("Error", "Veuillez entrer des valeurs valides !")

root = tk.Tk()
root.geometry("600x600")
root.title("Résolution de l'équation de 2ème degré")
imgIcone = tk.PhotoImage(file="images/icone.png")
root.iconphoto(True, imgIcone)
#root.config(background="#4da5ee")
root.minsize(600,600)
#image d'entête
imgEntete = tk.PhotoImage(file="images/entête.png")
tk.Label(root, image=imgEntete, bg="#4da5ee").pack(pady=5)
tk.Label(root, text="     Résolution des équations de 2ème degré en ℝ     ", height=2, font=("Arial", 16, "bold"), fg="darkred", bg="#4da5ee").pack()
frame0 = tk.Frame(root, relief="solid", background="darkred")
frame0.pack(pady=(5,0))
frame1 = tk.Frame(frame0, relief="groove", borderwidth=2, background="#9cc5e7")
frame1.pack(padx=2, pady=2)
frameL1 = tk.LabelFrame(frame1, text="Equation", font=("Calibri", 14, "bold"), relief="groove", borderwidth=2, background="#9cc5e7")
frameL1.pack(padx=80)
entryA = tk.Entry(frameL1, width=5, font=("Calibri", 14, "bold"))
entryA.grid(row=0, column=0, padx=(40,0))
entryA.focus_set()
tk.Label(frameL1, text=" x² + ", font=("Calibri", 14, "bold"), bg="#9cc5e7").grid(row=0, column=1)
entryB = tk.Entry(frameL1, width=5, font=("Calibri", 14, "bold"))
entryB.grid(row=0, column=2)
tk.Label(frameL1, text=" x + ", font=("Calibri", 14, "bold"), bg="#9cc5e7").grid(row=0, column=3)
entryC = tk.Entry(frameL1, width=5, font=("Calibri", 14, "bold"))
entryC.grid(row=0, column=4)
tk.Label(frameL1, text=" = 0 ", font=("Calibri", 14, "bold"), bg="#9cc5e7").grid(row=0, column=5, padx=(0,40), pady=20)
tk.Button(frame1, text="Résoudre",font=("Calibri", 16, "bold"),fg="white", bg="#2f4ca1", command=resoudre).pack(pady=20)
lblDelta = tk.Label(frame1, font=("Calibri", 16, "bold"), fg="brown", bg="#9cc5e7")
lblDelta.pack(pady=10)
lblSol = tk.Label(frame1, font=("Calibri", 14, "bold"), fg="blue", height=3, bg="#9cc5e7")
lblSol.pack(pady=(10,30))
tk.Label(root, text= "--------------------------\nYAHYA BAHMAD - 2026", font=("Calibri", 12 , "bold"), fg="#172141", height=3).pack(pady=(0,5))
root.mainloop()