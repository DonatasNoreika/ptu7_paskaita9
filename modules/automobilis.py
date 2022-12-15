class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        # print(self.metai, self.modelis, self.kuro_tipas)
        print(self.__str__())

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

    def __str__(self):
        return f"{self.metai} {self.modelis}, {self.kuro_tipas}"
