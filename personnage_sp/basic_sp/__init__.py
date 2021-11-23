import random
print("fichier basic ouvert")
from personnage_sp.basic_sp.Math.Math_stat import ecart_type
from personnage_sp.basic_sp.basic_of_Basic.So_basic import So_basic

class Basic_v3(So_basic):

    def __init__(self,pere=None,mere=None,v_max=1,v_min=1, v=1, m=0, m_max=0, m_min=0, size=100):
        super(Basic_v3, self).__init__(pere=pere, mere=mere,
                                       v_max=v_max, v_min=v_min, v=v,
                                       m=m, m_max=m_max, m_min=m_min)

    def save_dataBase_v1(self):
        pass















class Basic:
    def __init__(self, v=1, v_min=1, v_max=1, m=0, m_max=0, m_min=0, size=100,d=None,Index=None, **kwargs):
        """
        :param v:
        :param v_min:
        :param v_max:
        :param m:
        :param m_max:
        :param m_min:
        :param size:
        :param d:
        :param Index:
        :param kwargs: TOUT LES PARAMÈTRE AFFECTENT À LONG TERME OU NON, LE PERSSONAGE
        """
        print("init  basic")
        if not d or Index:
            self.d = []
            self.Index = []

            for k, item in kwargs.items():
                self.d.append([k, item])
                self.Index.append(k)

        else:
            self.d = d
            if not Index:
                self.Index = []
                self.Index = [a[0] for a in d]
            else:
                self.Index = Index


        self.m = m
        self.v = v
        self.size = size
        self.v_max = v_max
        self.v_min = v_min  #todo: optimisation: renplacer v_max=1 par v_max=None (économie d'espace).
        self.m_max = m_max
        self.m_min = m_min
        if(v_min != 1) or (v_max != 1): #todo: optimisation: renplacer v_min=1 par v_min=None (économie d'espace).
            if(v_min > v_max) or (v_max < v_min): #todo: optimisation: inversion du if
                pass
            else:
                v = random.random()
                self.v = v*self.size
                while (self.v < v_min) or (self.v > v_max):
                    v = random.random()
                    self.v = v*self.size
                    print(self.v)
                    print(f"\tmin:{v_min},max:{v_max}")
    def get(self, index):
        for i in self.d:
            if i[0] == index:
                return i
        raise IndexError("fail, le paramètre n'a pas été ajouté")
    def __getitem__(self, item):
        if item == "v":
            return self.v
        elif item == "m":
            return self.m
        elif item == "v_max":
            return self.v_max
        elif item == "v_min":
            return self.v_min
        elif item == "m_min":
            return self.m_min
        elif item == "m_max":
            return self.m_max
        else:
            if item in self.Index:
                return self.d[self.Index.index(item)]
            else:
                raise IndexError("fail, le paramètre n'a pas été ajouté")
    def av(self, dm_min=0, dv_min=0, dv_max=0, dv=0, dm=0, dm_max=0, **kwargs):
        """
        l'avancement, dans le temps, des personnages.
        :param dm_min: delta of minimum m
        :param dv_min: delta of minimum value
        :param dv_max: delta of maximum value
        :param dv: variation de la valeur basic
        :param dm: variation de la valeur de variation à chaque tique. (en terme de physique, il s'agit de la variation
                de l'acélération, qui fait varier la vitesse (le m) et qui fait varier la distance, (le v)
        :param dm_max:
        :param kwargs: tout les autre paramètre. NE DOIT PAS AVOIR "d" AVANT, COMME DANS LES AUTRE PARAMÈTRE
        :return:    [self.v, self.m, de,self.size, self.v_max, self.v_min, self.m_min, self.m_max, self.d, self.Index]
        """

        if len(kwargs) != 0:               #todo: optimisation fait: évite de faire une boucle,
            for k, item in kwargs.items(): #todo: possible perte de vitesse puis qu'il devras faire deux et plus test logique pour les élément de kwargs (s'il sont présent.) donc je conseillerais de probablement l'enlevé.
                if k in self.Index:
                    try:
                        self.d[self.Index.index(item)][1] += item
                    except TypeError:
                        raise TypeError(F"valeur non valide, le bon type est:{type(self.d[self.Index.index(item)])}")
        self.v += dv
        self.m += dm
        self.m_max += dm_max
        self.m_min += dm_min
        self.v_max += dv_max
        self.v_min += dv_min
        de = (self.v <= 0)
        return [self.v, self.m, de,self.size, self.v_max, self.v_min, self.m_min, self.m_max, self.d, self.Index]
    def add(self,key,value):
        """
        ajoute un paramètre qui ne fut pas tout de suite ajouté dans l'initialisation de la classe.
        :param key:
        :param value:
        :return:
        """
        self.Index.append(key)
        self.d.append([key,value])
    def __del__(self):
        del self.v
        del self.m
        del self.v_max
        del self.v_min
        del self.m_min
        del self.m_max
        self.Index.clear()
        del self.Index
        for e in self.d:
            e.clear()
        self.d.clear()
        del self.d



class Delta:
    """
    cette classe permet la variation non constante de v.

    PASSAGE EN MODE DATABASE
    """
    def __init__(self):

        pass

        #####################################################
        #####################################################
class basic_effet:
    __slots__ = "v"
    def __init__(self,v):
        """
        :param v: test
        :param genetique =
        :param
        :param
        :param
        :param
        :param
        :param

        v: valeur
        m: variation
        effect:

        --------------------------------------------
        note:
        une maladie se retire, elle devien juste de moins en moins présente. et à un sertain seuil, il devien non perceptible.


        les médicament reste TOUJOURS dans le corp.


        --------------------------------------------

        """
        s=0

from personnage_sp.basic_sp.Math.Math_stat import stat_p1,max_min

def convert_day_to_m(valeur,nombre_de_jour,type):
    s = valeur

class Basic_v2():
    def __init__(self,v_max=1,v_min=1,pere=None,mere=None, v=1, m=0, m_max=0, m_min=0, size=100):
        if (pere != None) and (mere != None):    #todo: alors, il y a des parents
            self.__init__child(pere=pere,mere=mere)

        else:
            self.v_max = random.uniform(0,100)    #todo: À REFAIRE
            self.v_min = random.uniform(0,100)
            self.m_min = random.uniform(0,5)
            self.m_min = random.uniform(0,5)
            self.v = stat_p1(self.v_min,self.v_max)
            self.m = stat_p1(self.m_min,self.m_max)

    def __init__child(self,pere,mere):
        """
        cette méthode permet de surdéfnire l'ignitialisation dans le cas d'un enfant.
        :param pere:
        :param mere:
        :return:
        """
        self.v_max = stat_p1(mere.v_max, pere.v_max)
        self.v_min = stat_p1(mere.v_min, pere.v_min)
        self.m_min = stat_p1(mere.m_min, pere.m_min)
        self.m_max = stat_p1(mere.m_max, pere.m_max)
        self.v = stat_p1(self.v_max, self.v_min)
        self.m = stat_p1(self.m_min, self.m_max)
        self.d = {  # todo: d pour diver
            "génétique": [],
            "maladie": [],
            "medicament": []
        }



    def av(self,dv=0,dv_max=0,dv_min=0,dm=0,dm_max=0,dm_min=0,**kwargs):
        """

        :param dv:
        :param dv_max:
        :param dv_min:
        :param dm:
        :param dm_max:  j'ai un soudain doute sur sont utiliter
        :param dm_min:
        :param kwargs:
        :return:
        """
        # todo: possible amélioration de la mémoire demander,

        self.v += dv
        self.m += dm
        self.v_max += dv_max
        self.v_min += dv_min
        self.m_max += dm_max
        self.m_min += dm_min
        return [self.v,
                self.m,
                self.v_max,
                self.v_min,
                self.m_max,
                self.m_min,
                ]



if __name__ == '__main__':
    s = "3"
    eval(s)




