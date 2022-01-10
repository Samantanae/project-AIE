import json
from _Personnage_.error import NotInCategory
#from _Personnage_.personnage_sp.basic_sp.Math.Math_stat import stat_p1
import random
import pandas as pd
import csv
from json import dump,load,dumps,loads
class so_Basic_File_Dead_Posibility:
    __slots__ = "ID","file"
    def __init__(self, arg_basic=None, file:str=None, **kwargs):
        pass
class so_Basic_File_None_Dead_Posibility:
    __slots__ = "ID","file"
    def __init__(self,file:str=None, **kwargs):
        pass
class so_Basic_Dead_Posibility:
    __slots__ = "ID", "file"

    def __init__(self, arg_basic=None, file: str = None, **kwargs):
        pass
class so_Basic_None_Dead_Posibility:
    __slots__ = "ID", "file"
    def __init__(self, file: str = None, **kwargs):
        pass
class _dataExterne:
    def __init__(self,file:str,print_=True,**kwargs):
        """
        version: v0.1.0.0.0.0.0.0.8
        module de gestion de trensefer de données.
        :param file: le fichier
        :param kwargs: tout les données
        """
        self.print_ = print_
        if print_:
            print(file)
            print(kwargs)
            print(self.__dict__)
        self.file = file
        self._file = str(file)

        self._prep_p1_new(**kwargs)

        # open data frame
        try:
            self.df1 = pd.read_csv(self.file)  # todo: optimisation possible ici
        except:
            print(Exception)
            self.df1 = pd.DataFrame(columns=self.columns)

        self.df_new_row = pd.DataFrame(self.d)
        print("----")
        print(self.df1)
        print("====")
        print(self.df_new_row)
        print("----")
        while len(self.df_new_row) > 1:  # todo: sans cette boucle, il aurais un dataFrame de 2 lignes (identique)
            self.df_new_row = self.df_new_row.pop(self.df_new_row.index[1:-1])
        ind_avant = set(self.df1.index)
        df2 = pd.concat([self.df1, self.df_new_row], ignore_index=True)  # todo: optimisation possible ici
        ind_apres = set(df2.index)
        ind_apres.symmetric_difference_update(ind_avant)

        if print_:
            print(len(ind_apres))
            print(len(ind_apres))
            print(df2.index)

        self._prep_menage()


        def compa(l_last:list,l_new:list):
            l = list([v for v in l_new if v not in l_last])
            if len(l)==1:
                return l[0]
        self.Id = compa(list(ind_avant),list(ind_apres))  # todo:         l'ID est apliqué ici.
        if type(self.file)!=str:    #todo: enti-bug
            del self.file
            self.file = self._file
        #print(f"name file:{self.file}\t type variable:{type(self.file)}")
        print(df2)
        df2.to_csv(self.file, index=False)
        # df2.close()
    def _prep_menage(self):
        del self.df_new_row
        del self.d
        del self.df1
    def _prep_p1_new(self,**kwargs):
        self.columns = [a for a in kwargs]
        self.d = {a: [] for a in kwargs}
    def __del__(self):
        """
        dat = self.__dict__
        for e in dat:
            dat = self.__getattribute__(e)
            if type(dat)in(list,set,dict,tuple):
                self.__getattribute__(e).clear()
            else:
                if type(dat) == str:
                    if "__" in dat:
                        pass
                    else:
                        self.__delattr__(e)
                else:
                    self.__delattr__(e)

        """
    def _open_(self):
        self.df = pd.read_csv(self.file)
    def _close_(self):
        self.df.to_csv(self.file,index=False)
        self.df.close()
    def getAll(self):
        """
        todo: non tester
        :return:
        """
        self._open_()
        self.d = self.df.loc[[self.Id]]
        self._close_()
        return self.d
    def replaceAll(self,data:pd.DataFrame):
        """
        todo: non tester
        :param data:
        :return:
        """
        self._open_()
        self.df.loc[[self.Id]] = data
        self._close_()
    def replace(self,**kwargs):
        self._open_()
        for k,i in kwargs.items():
            self.df.at[self.Id, k] = i
        self._close_()
    def __str__(self):
        return str(self.getAll())
    def __setitem__(self, key, value):
        self._open_()
        try:
            self.df.at[self.Id, key] = value
        except:
            raise NotInCategory((key))
        self._close_()
    def __getitem__(self, item):
        self._open_()
        self.d = self.df.loc[[self.Id],[item]]
        self._close_()
        return self.d
class _dataInterne:
    def __init__(self, info_var=None, **kwargs):
        if info_var is None:
            info_var = {}
        for key, value in kwargs.items():
            if key not in info_var:
                info_var[key] = ""
        self.__slots__ = info_var
        for key, value in kwargs.items():
            self.__setattr__(key, value)
    def allvalue(self):
        return self.__dict__
    def replaceAll(self,**kwargs):
        pass
    def getAll(self):
        return self.__dict__
    def replace(self,**kwargs):
        self.replaceAll(**kwargs)
    def __str__(self):
        return str(self.__dict__)
    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.__setattr__(key,value)
        else:
            raise NotInCategory
    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__getattribute__(item)
        else:
            raise NotInCategory
    def __delitem__(self, key):
        if key in self.__dict__:
            self.__delattr__(key)
        else:
            raise NotInCategory
class So_basic(_dataExterne,_dataInterne):
    __slots__ = "arg_basic","saved_data","file","Id","save"
    def __init__(self, deadPosibilyty=True, file:str=None, jsonDiver=None, **kwargs):
        """
        :type karg:
                "v_min", "v", "v_max", \
                "m", "m_max", "m_min", \
                "Bv_max",
        :param file:
        :param Id:
        :param pere:
        :param mere:

        :param jsonDiver: atribue variable de la class. (ex: les items d'un sac à dos)
        :param kwargs: atribue
        """

        self.saved_data = kwargs


        self.prepa_p3_basic_argument(**self.prepa_p2_basic(deadPosibilyty))
        self.prepa_p4_jsonDiver(jsonDiver)
        # ajouté les autres données
        if file is not None:
            self.save = True
            if ".csv" not in file:    #todo: enti-oups
                file += ".csv"
            super(So_basic, self).__init__(_dataExterne(file,**self.saved_data))
        else:
            self.save = False
            print("non enregistrer (les données passent par la ram et non pas un fichier csv)")
            super(So_basic, self).__init__(_dataInterne(None,**self.saved_data))
    def prepa_p2_basic(self, deadPosibilyty):
        if deadPosibilyty:
            return {"v_min":1, "v":1, "v_max":1,"m":0, "m_max":0, "m_min":0, "Bv_max":0,"deadPosibilyty":deadPosibilyty}
        else:
            return {"deadPosibilyty": deadPosibilyty}
    def prepa_p3_basic_argument(self, **basic_argument):
        for k,item in basic_argument.items():
            if k not in self.saved_data:
                self.saved_data[k] = item
    def prepa_p4_jsonDiver(self, jsonDiver):
        if jsonDiver is None:
            jsonDiver = {}
        jsonDiver = json.dumps(jsonDiver)
        self.saved_data["jsonDiver"]=jsonDiver
    def av(self):
        pass
    """
    def allvalue(self):
        return super().allvalue()
    
    def replaceAll(self,**kwargs):
        super().replaceAll(**kwargs)
    
    def getAll(self):
        return super().getAll()
    
    def __str__(self):
        super().__str__()
    """
b = So_basic(file="test.csv")