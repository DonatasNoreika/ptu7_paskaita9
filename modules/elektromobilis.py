from modules.automobilis import Automobilis

print("Elektromobilio klase")

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")
