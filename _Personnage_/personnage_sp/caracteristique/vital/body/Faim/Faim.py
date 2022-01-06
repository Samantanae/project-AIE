
from _Personnage_.personnage_sp.basic_sp.Basic import Basic    #todo: surdéfinition de la class Basic


class Faim(Basic):
    #__slots__ = "v_min", "v", "v_max",\
    #            "m", "m_max", "m_min",\
    #            "Bv_max", "save", "Id","file"
    def __init__(self, Id=None, pere=None, mere=None, v_max=100, v_min=30, m_max=2, m_min=0.000000000000001,
                 size=100):
        super(Faim, self).__init__(
            file="Faim.csv", Id=Id,pere=pere, mere=mere,v_max=v_max,
            v_min=v_min,m_max=m_max, m_min=m_min,size=size)


#from personnage_sp.basic_sp import Basic
#from personnage_sp.basic_sp.Math.Math_stat import stat_p1
#class Faim(Basic):
#    def __init__(self,v=10000,v_min=9400,v_max=10000,m_min=8,m_max=30,size=10000,pere=None,mere=None,**kwargs):
#        if (pere != None) and (mere !=None):
#            super(Faim, self).__init__()
#            self.__init__child(pere,mere)    # todo: le module de génération secondaire, qui créer à partire de deux parent
#
#
#        else:
#            d = []
#            Index = []
#            for e in kwargs:
#                Index.append(e)
#                d.append([e,kwargs[e]])
#            super(Faim, self).__init__(v=v, v_min=v_min, v_max=v_max, m_min=m_min, m_max=m_max,size=size,d=d,Index=Index)
#
#    def __init__child(self,f_mere,f_pere):
#
#        self.v_min  = stat_p1(f_mere.v_min,f_pere.v_min)
#        self.v_max  = stat_p1(f_mere.v_max,f_pere.v_max)
#        self.m_max  = stat_p1(f_mere.m_max,f_pere.m_max)
#        self.m_min  = stat_p1(f_mere.m_min,f_pere.m_min)
#        self.size   = stat_p1(f_mere.size,f_pere.size)
#        self.m      = stat_p1(f_mere.m,f_pere.m)

s=0
del s
#Faim()

