class Basic_m1:
    """mode argument de class"""
    def __init__(self,**kwargs):
        for k,i in kwargs.items():
            if type(k)!=str:
                print(f"valeur '{k} n'est pas de type string, la conversion serras effectuer pour le placé en argument")
                k = str(k)
            if " " in k:
                print(f"un ou des espace (' ') est contenue dans: {k},remplacement par '_' des espace")
                while " " in k:
                    k = k.replace(" ","_")

            self.__setattr__(k,i)

    def __getitem__(self, item):
        return self.__getattribute__(item)



class Basic_m2:
    """mode dictionnaire"""
    __slots__ = "d"
    def __init__(self,**kwargs):
        print(self)
        self.d = kwargs    # l'omision de '.copy()' est volontaire.
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass
    def __copy__(self):
        pass
    def getAll(self):
        pass

    def __del__(self):
        pass
    def __delitem__(self, key):
        pass

