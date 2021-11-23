from personnage_sp.basic_sp import Basic
from personnage_sp.basic_sp.Math_stat import stat_p1

class Soif(Basic):
    def __init__(self,mere=None,pere=None):


        if (mere !=None) and (pere != None):
            self.__init__children(mere,pere)
        super(Soif, self).__init__()




    def __init__children(self,mere,pere):
        self.v_

