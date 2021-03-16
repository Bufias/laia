from .restaurants import Restaurant


class RestaurantCovid(Restaurant):
    def __init__(self, nom_resto, ntaules, maxafor):
        super().__init__(nom_resto, ntaules)
        self.maxafor = maxafor

    def capacitat(self):
        capacitat_total = super().capacitat()
        if capacitat_total < self.maxafor:
            return capacitat_total
        return self.maxafor
