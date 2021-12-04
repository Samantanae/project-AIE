from personnage_sp.basic_sp.Math.Math_stat import stat_p1
import random

import pandas as pd
import csv


class So_basic:
    __slots__ = "v_min", "v", "v_max",\
                "m", "m_max", "m_min",\
                "Bv_max", "save", "Id"

    def __init__(self, file=None, Id=None, pere=None, mere=None, v_max=1, v_min=1, v=1, m=0, m_max=0, m_min=0,
                 size=100):

        self.save = False
        self.Id = Id

        if (pere is not None) and (mere is not None):  # todo: alors, il y a des parents
            self.__init__child(pere=pere, mere=mere)
        else:
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

        if file is not None:
            self.save = True
            columns = ["v", "m", "v_min", "v_max", "m_min", "m_max", "Bv_max"]
            try:

                df1 = pd.read_csv(file)    #todo: optimisation possible ici

                #todo: optention des index ici, pour d'étermner la prochaine ID utiliser (soit son propre id).

                ind = df1.index


                print("\t\t\t reussi")
            except:
                ind = []
                df1 = pd.DataFrame(columns=columns)    #todo: optimisation possible ici
                print(df1.index)

            d = {"v": [self.v], "m": [self.m], "v_min": [self.v_min], "v_max": [self.v_max],
                 "m_min": [self.m_min], "m_max": [self.m_max], "Bv_max": [self.Bv_max]}
            df_new_row = pd.DataFrame(d)
            while len(df_new_row) > 1:                                  #todo: sans cette boucle, il aurais un dataFrame de 2 lignes (identique)
                df_new_row = df_new_row.pop(df_new_row.index[1:-1])
            df2 = pd.concat([df1, df_new_row], ignore_index=True)    #todo: optimisation possible ici
            print(df2)
            try:
                ind = df1.compare(df2)
                print(ind)
            except:
                self.Id = 0
            df2.to_csv(file, index=False)    #todo: optimisation possible ici

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
                      v_max=random.randint(0,100),
                      v_min=random.randint(0,100),
                      m_max=random.randint(0,10),
                      m_min=random.randint(0,10))
test()

def verif_existe(file_name: str):
    s = False
    try:
        with open(file_name, "r") as f:
            s = True
    except:
        s = False
    return s


import csv
import pandas as pd
import os



class so_basic_data:
    """
    version: v0.0.0.0.0.9.0.0.1
    module de gestion de trensefer de données.
    """

    def __init__(self, file="basic_file.csv", id=-1, *args,
                 **kwargs):  # -1 pour (automatique), mais il vas pouras renvoyer l'id quand il seras demander
        self.file = file
        if file not in os.listdir():
            # todo: faire la maneuvre pour créer le fichier .csv
            l = []
            for e in args:
                if e not in {"v", "m", "v_max", "v_min", "m_max", "m_min", "Bv_max"}:
                    l.append(e)
            df = pd.DataFrame(columns=l)

        l = []
        for e in args:
            if e not in {"v", "m", "v_max", "v_min", "m_max", "m_min", "Bv_max"}:
                l.append(e)

        df = pd.DataFrame(columns=l)
