import random

from personnage_sp.basic_sp.Math_stat import ecart_type,gauss,stat_p1
from personnage_sp.Faim import Faim

#try:
#    from Faim import Faim
#except:
#    try:
#        from personnage_sp.Faim import Faim
#    except:
#        from Perso_v2.personnage_sp.Faim import Faim




class Personnage:
    def __init__(self,mere=None,pere=None):

        if(mere!=None) and (pere != None):
            self.faim = Faim(mere=mere.faim, pere=pere.faim)






            #todo: dans le cas ou il y a des parent.
            #v_min_faim = random.gauss((mere.faim.v_min + pere.faim.v_min)/2,
            #                          ecart_type(mere.faim.v_min, pere.faim.v_max)) #todo: optimisation: posibilité de réduire le nombre de valeur chercher plusieurs fois

            #m_min_faim = random.gauss((mere.faim.v_min + pere.faim.v_min)/2,
            #                          ecart_type(mere.faim.v_min, pere.faim.v_max))

        else:
            self.faim = Faim()


P1 = Personnage()
P2 = Personnage()
P3 = Personnage(P1,P2)