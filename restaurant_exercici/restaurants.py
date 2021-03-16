from .taules import Taula


class Restaurant:

    def __init__(self, nom_resto, nombre_taules):
        self.nom = nom_resto
        self.__nombre_taules = nombre_taules
        self.__taules = []
        for i in range(0, self.__nombre_taules):
            nova_taula = Taula(capac=0)
            self.__taules.append(nova_taula)

    def __len__(self):
        return self.__nombre_taules

    def __str__(self):
        return 'Restaurant {:s}'.format(self.nom)

    def __setitem__(self, idt, npers):
        taula = self.__taules[idt]
        taula.ocupar(npers)

    def __getitem__(self, idt):
        taula = self.__taules[idt]
        return taula.ocupacio()

    def modif_taula(self, idt, novacap):
        taula = self.__taules[idt]
        taula.capacitat = novacap
        taula.alliberar()

    def capacitat(self):
        capacitat = 0
        for taula in self.__taules:
            capacitat += taula.capacitat
        return capacitat

    def ocupacio(self):
        ocupacio = 0
        for taula in self.__taules:
            ocupacio += taula.ocupacio()
        return ocupacio
