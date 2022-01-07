from _Personnage_.personnage_sp.basic_sp.Math.Math_stat import stat_p1
import random, json

import pandas as pd
import csv
from json import dump,load,dumps,loads

class So_basic:
    __slots__ = "v_min", "v", "v_max", \
                "m", "m_max", "m_min", \
                "Bv_max", "save", "Id", "file","diver","tempon"

    def __init__(self, file=None, Id=None, pere=None, mere=None, v_max=1, v_min=1, v=1, m=0, m_max=0, m_min=0,
                 size=100,diver=None):
        self.diver = diver
        self.tempon={}

        if file:
            self.save = True
        else:
            self.save = False
        self.Id = Id
        self.file = file
        self.Bv_max = v_max

        if (pere is not None) and (mere is not None):  # todo: alors, il y a des parents
            self.__init__child(pere=pere, mere=mere)
        self._prep_VM(v=v, m=m,
                      v_min=v_min, v_max=v_max,
                      m_min=m_min, m_max=m_max)
        if file is not None:
            self._data_new()
    def __del__(self):
        del self.v
        del self.m
        del self.v_min
        del self.v_max
        del self.m_min
        del self.m_max
        del self.Bv_max

    def _prep_VM(self, v, m, v_min, v_max, m_min, m_max):
        v_min = abs(v_min)
        v_max = abs(v_max)
        if v_max < v_min:  # inversion
            v_max, v_min = v_min, v_max  # évitons les boucles infinie causé par des problemes non réaliste (du type des max plus petit que des min)
        if m_max < m_min:  # inversion
            m_max, m_min = m_min, m_max

        self.v_min, self.v_max = v_min, v_max
        self.m_min, self.m_max = m_min, m_max
        self.Bv_max = v_max

        if v != 1:
            self.v = v
        else:
            if (v_min == 1) and (v_max == 1):
                self.v = v
            else:
                self.v = stat_p1(self.v_min, self.v_max)
        if m != 0:
            self.m = m
        else:
            if (m_min == 0) and (m_min == 0):
                self.m = m
            else:
                self.m = stat_p1(self.m_min, self.m_max)

    def _data_load(self):
        pass
    def _data_save(self):
        pass

    def _etape2_data(self):
        pass

    #todo: data ##########################################
    def _prep_p1_new(self,**kwargs):

        self.tempon["columns"] = [a for a in kwargs]
        self.tempon["d"] = {a: [] for a in kwargs}
    def _data_new(self, columns=None,
                  d=None):
        """
        version: v0.1.0.0.0.0.0.0.7
        module de gestion de trensefer de données.
        """

        if columns is None:
            columns = ["v", "m", "v_min", "v_max", "m_min", "m_max", "Bv_max", "diver"]
        if d is None:
            d = {"v": [], "m": [], "v_min": [], "v_max": [], "m_min": [], "m_max": [], "Bv_max": [], "diver": []}
        else:
            lt = [c for c in d]
            if lt != columns:
                raise Exception("les columns et les clées du dictionnaire de corespond pas")
        self.save = True


        try:
            df1 = pd.read_csv(self.file)  # todo: optimisation possible ici

            # todo: optention des index ici, pour d'étermner la prochaine ID utiliser (soit son propre id).
            print("\t\t\t reussi")
        except:
            df1 = pd.DataFrame(columns=columns)  # todo: optimisation possible ici



        df_new_row = pd.DataFrame(d)
        while len(df_new_row) > 1:  # todo: sans cette boucle, il aurais un dataFrame de 2 lignes (identique)
            df_new_row = df_new_row.pop(df_new_row.index[1:-1])
        ind_avant = set(df1.index)
        df2 = pd.concat([df1, df_new_row], ignore_index=True)  # todo: optimisation possible ici
        ind_apres = set(df2.index)
        print(len(ind_apres))

        ind_apres.symmetric_difference_update(ind_avant)
        print(len(ind_apres))
        print(df2.index)
        def compa(l_last:list,l_new:list):
            l = list([v for v in l_new if v not in l_last])
            if len(l)==1:
                return l[0]

        self.Id = compa(list(ind_avant),list(ind_apres))  # todo:         l'ID est apliqué ici.
        df2.to_csv(self.file, index=False)  # todo: optimisation possible ici
    #todo: prep ##########################################
    def prepa_p1(self,deadPosibilyty=True, jsonDiver=None, file:str=None,  **kwargs):
        if jsonDiver is None:
            jsonDiver = {}
        self.tempon["saved_data"]=kwargs


        self.prepa_p3_basic_argument(**self.prepa_p2_basic(deadPosibilyty))
        self.prepa_p4_jsonDiver(jsonDiver)
        # ajouté les autres données
        if file is not None:
            self.save = True
            if ".csv" not in file:    #todo: enti-oups
                file += ".csv"
    def prepa_p2_basic(self, deadPosibilyty):
        if deadPosibilyty:
            return {"v_min":1, "v":1, "v_max":1,"m":0, "m_max":0, "m_min":0, "Bv_max":0,"deadPosibilyty":deadPosibilyty}
        else:
            return {"deadPosibilyty": deadPosibilyty}

    def prepa_p3_basic_argument(self, **basic_argument):
        for k,item in basic_argument.items():
            if k not in self.tempon["saved_data"]:
                self.tempon["saved_data"][k] = item
    def prepa_p4_jsonDiver(self, jsonDiver):
        if jsonDiver is None:
            jsonDiver = {}
        jsonDiver = json.dumps(jsonDiver)
        self.saved_data["jsonDiver"]=jsonDiver
    def __init__child(self, pere, mere):
        """
        cette méthode permet de surdéfnire l'ignitialisation dans le cas d'un enfant.
        :param pere:
        :param mere:
        :return:
        """
        self.v_max = stat_p1(mere.Bv_max, pere.Bv_max)
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

    def av(self, dv=0, dv_max=0, dv_min=0, dm=0, dm_max=0, dm_min=0, **kwargs):
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


def test():
    for e in range(100):
        v1 = So_basic(file="test.csv",
                      v_max=random.randint(0, 100),
                      v_min=random.randint(0, 100),
                      m_max=random.randint(0, 10),
                      m_min=random.randint(0, 10))
        print(v1)



test()


def verif_existe(file_name: str):
    s = False
    try:
        with open(file_name, "r") as f:
            s = True
    except:
        s = False
    return s