from personnage_sp.basic_sp import Basic_v2


class Soif(Basic_v2):
    def __init__(self,mere=None,pere=None):
        super(Soif, self).__init__(mere=mere,pere=pere)

    def __del__(self):
        for e in self.d:
            d.clear()





