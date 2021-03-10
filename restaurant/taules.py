class Taula:
    def __init__(self, capacitat):
        self.capacitat = capacitat
        self.nlliures = capacitat

    def ocupacio(self):
        return self.capacitat - self.nlliures

    def ocupar(self, npers):
        if self.ocupacio() == 0 and self.nlliures >= npers:
            self.nlliures = self.nlliures - npers
            return True
        else:
            return False

    def alliberar(self):
        self.nlliures = self.capacitat