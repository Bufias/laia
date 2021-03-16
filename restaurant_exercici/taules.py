class Taula:
    def __init__(self, capac):
        self.capacitat = capac
        self.nlliures = capac

    def ocupacio(self):
        return self.capacitat - self.nlliures

    def ocupar(self, npers):
        if self.nlliures == self.capacitat and npers <= self.capacitat:
            self.nlliures = self.nlliures - npers
            return True
        return False

    def alliberar(self):
        self.nlliures = self.capacitat
