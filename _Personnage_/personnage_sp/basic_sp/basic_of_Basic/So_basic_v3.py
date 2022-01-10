class atr:
    def __init__(self,value,_type_,**kwargs):
        self.value = value
        self._type_ = _type_
        for k,i in kwargs.items():
            self.__setattr__(k,i)

class trensDataBase:
    def __init__(self):
        pass
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass
    def __contains__(self, item):
    def resetAll(self):
        pass
    def resetAtr(self,val):
        pass
    def clearAtr(self,val):
        pass
    def deleteAtr(self,val):
        pass
    def deleteAll(self,val):
        pass

class trensDataCSV:




class soo_basic:
    def __init__(self,**kwargs):
        self.d = kwargs

    def av(self):
        pass
    def getAll(self):
        return self.__dict__

    def getD(self):
        return self.d

    def getCD(self):
        return self.d.copy()
    def getCAll(self):
        return self.__dict__.copy()
    def reset(self):
        pass
    def dead(self):
        pass



class so_basic(soo_basic):
    def __init__(self,mere=None,pere=None,**kwargs):
        super(so_basic, self).__init__(**kwargs)
