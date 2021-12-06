from personnage_sp.caracteristique.Faim.Faim import Faim
from personnage_sp.Soif import Soif


class Personnage:
    def __init__(self,mere=None,pere=None):
        self.faim = Faim(mere=mere,pere=pere)
        self.soif = Soif(mere=mere,pere=pere)


    def __del__(self):
        del self.faim
        del self.soif
