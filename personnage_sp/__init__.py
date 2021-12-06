from personnage_sp.basic_sp.Math.Math_stat import ecart_type,gauss,stat_p1
from personnage_sp.basic_sp.basic_of_Basic.Faim.Faim import Faim
from personnage_sp.basic_sp.pd import Geo_and_visual


#try:
#    from Faim import Faim
#except:
#    try:
#        from personnage_sp.Faim import Faim
#    except:
#        from Perso_v2.personnage_sp.Faim import Faim




class Personnage:
    def __init__(self, mere=None, pere=None,master=None):
        if master is not None:
            self.M0 = master.attachNewNode("Personnage")    # todo: noeux du personnage: pour un seule personnage

            self.geo_and_visual = Geo_and_visual(master=self.M0)

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