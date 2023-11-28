from tkinter import *
from time import strftime

class Horloge(Tk):
    def __init__(self):
        super().__init__()

        self.title("Horloge")
        self.geometry("400x200")
        self.configure(bg="black")

        self.pause_activee = BooleanVar(value=False)
        self.format_24h = BooleanVar(value=True)

        self.creer_interface()

        self.actualiser_horloge()

    def creer_interface(self):
        # interface
        self.label_heure = Label(self, font=('calibri', 40, 'bold'), foreground='white', background='black')
        self.label_heure.pack(anchor='center', pady=20)

        # Bouton arret marche
        self.bouton_pause = Button(self, text="Pause", command=self.basculer_pause, font=('calibri', 12, 'bold'), fg='white', bg='gray')
        self.bouton_pause.pack(side='left', padx=10)

        # Bouton 12h 24h
        self.bouton_format_heure = Button(self, text="12h / 24h", command=self.basculer_format_heure, font=('calibri', 12, 'bold'), fg='white', bg='gray')
        self.bouton_format_heure.pack(side='right', padx=10)

    def actualiser_horloge(self):
        if not self.pause_activee.get():
            heure_format = '%I:%M:%S %p' if not self.format_24h.get() else '%H:%M:%S'
            heure_str = strftime(heure_format)
            self.label_heure.config(text=heure_str)
        self.after(1000, self.actualiser_horloge)

    def basculer_pause(self):
        self.pause_activee.set(not self.pause_activee.get())

    def basculer_format_heure(self):
        self.format_24h.set(not self.format_24h.get())

    def afficher_heure(self, heure):
        heure_str = '{:02d}:{:02d}:{:02d}'.format(*heure)
        self.label_heure.config(text=heure_str)

if __name__ == "__main__":
    horloge = Horloge()
    horloge.afficher_heure((12, 30, 45))
    horloge.mainloop()
