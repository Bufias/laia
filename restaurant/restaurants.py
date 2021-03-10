from .taules import Taula


class Restaurant:
    def __init__(self, nom, ntaules):
        self.nom = nom
        self.__taules = []
        for i in range(ntaules):
            self.__taules.append(Taula(0))

    def modif_taula(self, idtaula, novacap):
        self.__taules[idtaula].capacitat = novacap
        self.__taules[idtaula].nlliures = novacap

    def capacitat(self):
        n = 0
        for i in range(len(self)):
            n = n + self.__taules[i].capacitat
        return n

    def ocupacio(self):
        n = 0
        for i in range(len(self)):
            n = n + self.__taules[i].ocupacio()
        return n

    def __getitem__(self, idtaula):
        return self.__taules[idtaula].ocupacio()

    def __setitem__(self, idtaula, npers):
        self.__taules[idtaula].ocupar(npers)

    def __len__(self):
        return len(self.__taules)

    def __str__(self):
        return 'Restaurant ' + self.nom