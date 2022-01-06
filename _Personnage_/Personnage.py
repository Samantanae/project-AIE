from _Personnage_.personnage_sp.caracteristique.vital.body.Faim.Faim import Faim
from _Personnage_.personnage_sp.caracteristique.vital.body.Soif.soif import Soif
from _Personnage_.personnage_sp.caracteristique.vital.body.Vie import vie
from _Personnage_.personnage_sp.caracteristique.vital.body import valeur
from _Personnage_.personnage_sp.caracteristique.vital.body import maladie
from _Personnage_.personnage_sp.caracteristique.vital.body import polution
from _Personnage_.personnage_sp.caracteristique.secondaire import argent
from _Personnage_.personnage_sp.caracteristique.secondaire import inventaire
from _Personnage_.personnage_sp.caracteristique.secondaire import équipement




#from _Personnage_ import physique

class Personnage:
    def __init__(self,mere=None,pere=None):
        self.faim = Faim(mere=mere,pere=pere)
        self.soif = Soif(mere=mere,pere=pere)




    def __del__(self):
        del self.faim
        del self.soif

    def av(self):
        self.faim.av()
        self.soif.av()


