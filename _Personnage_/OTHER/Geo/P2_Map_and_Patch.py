import random
from random import randint
import matplotlib as plt

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

class compt_étape:
    __slots__ = "n"
    def __init__(self):
        self.n = 0
    def av(self):
        self.n+=1
        print(f"étape: \t{self.n}")

global cc
cc = compt_étape()
def my_scatter(ax,datax, datay,c, param_dict):
    """
    A helper function to make a graph.
    """
    #out = ax.scatter(datax, datay, c=c, **param_dict)
    out = ax.scatter(datax, datay, **param_dict)
    out.set_label(s="y")
    return out

fig, ax = plt.subplots()




class p2:
    __slots__ = "x","y","c"
    def __init__(self,x,y,c=None):
        self.x = x
        cc.av()
        self.y = y
        cc.av()
        self.c = c
        cc.av()
    def nulifier(self):
        cc.av()
        self.c=-1
        cc.av()
        return p2(self.x,self.y,self.c)

    def null(self):
        cc.av()
        return self.c==-1
    def set(self,x=None,y=None,c=None):
        if x:
            cc.av()
            self.x = x
        if y:
            cc.av()
            self.y = y
        if c:
            cc.av()
            self.c = c
    def add(self,x=None,y=None,c=None):
        if x:
            self.x += x
        if y:
            self.y += y
        if c:
            self.c += c
    def __iadd__(self, other):
        cc.av()
        self.x += other.x
        cc.av()
        self.y += other.y
        if other.c:
            cc.av()
            if self.c:
                self.c += other.c
    def __str__(self):
        return f"[({self.x},{self.y}),{self.c}]"
    def __getitem__(self, item):
        cc.av()
        if type(item)==int:
            if item == 0:
                return self.x
            elif item == 1:
                return self.y
            elif item == 2:
                return self.c
            else:
                raise IndexError
        elif type(item)==str:
            if item=="x":
                return self.x
            elif item=="y":
                return self.y
            elif item=="c":
                return self.c
            else:
                raise IndexError
        else:
            raise IndexError
    def __setitem__(self, key, value):
        cc.av()
        if key == 0:
            self.x=value
        elif key == 1:
            self.y=value
        elif key == 2:
            self.c=value
        else:
            raise IndexError
    def up(self):
        return p2(self.x,self.y+1,self.c)
    def zup(self):
        return p2(self.x, self.y + 1)
    def dow(self):
        return p2(self.x, self.y - 1, self.c)
    def zdow(self):
        return p2(self.x, self.y - 1)
    def gauche(self):
        return p2(self.x-1, self.y, self.c)
    def zgauche(self):
        return p2(self.x-1, self.y)
    def droit(self):
        return p2(self.x+1,self.y,self.c)
    def zdroit(self):
        return p2(self.x+1,self.y)
    def __hash__(self):
        return hash((self.x,self.y,self.c))
    def __eq__(self, other):
        if type(other)==int:
            return self.c==other
        elif len(other)<2:
            raise IndexError("trops petit pour être une coordonner")
        elif type(other)==p2:
            other=other
        elif len(other)==2:
            other=(p2(other[0],other[1]))
        elif len(other)>2:
            other=(p2(other[0],other[1],other[2]))
        return (self.x==other.x)and(self.y==other.y)
    def Type(self,c):
        return c==self.c
    def __len__(self):
        if self.c:
            return 3
        else:
            return 2
    def __del__(self):
        try:
            del self.x
        except AttributeError:
            raise AttributeError
        try:
            del self.y
        except AttributeError:
            raise AttributeError
        try:
            del self.c
        except AttributeError:
            raise AttributeError
class Map:
    __slots__ = "M","n"
    def __init__(self,M=None,randmize=False,option2=False,**kwargs):
        randmize = randmize
        if randmize:
            nrandomize=700
            x_min = 0
            x_max = 100
            y_min = 0
            y_max = 100
            c_min = 1
            c_max = 4
        if M == None:
            self.M = []
        else:
            self.M = M
        for k, i in kwargs.items():
            if k == "x_min":
                x_min = i
            elif k == "x_max":
                x_max = i
            elif k == "y_min":
                y_min = i
            elif k == "y_max":
                y_max = i
            elif k == "nrandomize":
                nrandomize = i
            elif k == "M":
                self.M = i[:]
        with open("data.txt", "w") as da:
            if randmize and option2:
                for y in range(y_min,y_max,1):
                    for x in range(x_min,x_max,1):
                        for c in range(c_min,c_max,2):

                            self.M.append(p2(x,y,c))
                            da.writelines(f"\tx:{x},\ty:{y},\tc:{c}\n")
            elif randmize and not option2:
                for e in range(nrandomize):
                    print(e)
                    p = p2(randint(x_min,x_max),randint(y_min,y_max),randint(c_min,c_max))
                    while p in self.M:
                        if p[2] in self.M:
                            p = p2(randint(x_min, x_max), randint(y_min, y_max), randint(c_min, c_max))
                        else:
                            break
                    self.M.append(p)
            s=0
    def __iadd__(self, other):
        if type(other)==p2:self.M.append(other)
        elif type(other)==Map:self.M.extend(other.M)
        elif len(other)<2:raise IndexError("trops petit pour être une coordonner")
        elif len(other)==2:self.M.append(p2(other[0],other[1]))
        elif len(other)>2:self.M.append(p2(other[0],other[1],other[2]))
        else:raise TypeError("un type nom valide?")
        return self
    def __isub__(self, other):
        if type(other)==Map:
            for e in other:
                if e in self.M:
                    self.M.remove(e)
        elif type(other)==p2:
            if other in self.M:
                self.M.remove(other)
        else:raise TypeError
        return self
    def randmize(self,n=1000,xMin=0,xMax=100,yMin=0,yMax=100):
        self.M.extend([[randint(xMin,xMax),randint(yMin,yMax)] for e in range(n)])

    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <len(self.M):
            p = self.M[self.n]
            self.n += 1
            return p
        else:
            self.n = 0
            raise StopIteration
    def conv_MATPLOTcoord(self):
        x=[]
        y=[]
        c=[]
        Max = -99999999999999999999999999999999
        Min = 99999999999999999999999999999999


        for e in self.M:
            x.append(e.x)
            y.append(e.y)
            if e.c==0:
                c.append([0,0,0])
            elif e.c==1:
                c.append([100,100,0])
            elif e.c==2:
                c.append([0,100,100])
            elif e.c==3:
                c.append([200,100,50])
        return {"x":x,"y":y,"c":c}

    def __copy__(self):
        return Map(M=self.M)
    def __getitem__(self, item):
        return self.M[item]
    def __del__(self):
        for e in self.M:
            e.__del__()
        del self.M
    def __len__(self):
        return len(self.M)
    def __abs__(self):
        MaxX = -99999999999999999999999999999999999
        MinX = 99999999999999999999999999999999999
        MaxY = -99999999999999999999999999999999999
        MinY = 99999999999999999999999999999999999
        MaxC = -99999999999999999999999999999999999
        MinC = 99999999999999999999999999999999999
        nodes = []
        # todo: max et min
        for e in self.M:
            if e.x is not None:
                if e.x < MinX:
                    MinX = e.x
                if e.x > MaxX:
                    MaxX = e.x
            if e.y is not None:
                if e.y < MinY:
                    MinY = e.y
                if e.y > MaxY:
                    MaxY = e.y
            if e.c is not None:
                if e.c < MinC:
                    MinC = e.c
                if e.c > MaxC:
                    MaxC = e.c
        MinaY = abs(MinY)
        MinaC = abs(MinC)
        Minax = abs(MinX)
        MaxY += abs(MinY)
        MaxX += abs(MinX)
        MaxC += abs(MinC)  # todo: pour dépacer le 0 au point le plus petit.
        for e in self.M:
            if type(e) == p2:
                self.M[self.M.index(e)].add(x=Minax,y=MinaY,c=MinaC)

    def expand_c(self)->list:
        l = []
        for e in self.M:
            l.append(e.c)
        return l
    def expand_x(self)->list:
        l=[]
        for e in self.M:
            l.append(e.x)
        return l
    def expand_y(self)->list:
        l = []
        for e in self.M:
            l.append(e)
        return l


class Patch:
    def __init__(self ,ci ,cf ,Map_,floor=[] ,not_floor=[]):
        if type(Map_)==Map:
            self.findPatch(ci=ci ,cf=cf ,Map_=Map_ ,floor=floor ,not_floor=not_floor)
            self.pat = []
        elif type(Map_)==list:
            if type(Map_[0]) == p2:
                self.FinPatchPL(ci=ci,cf=cf,Map_=Map_,floor=floor,not_floor=not_floor)
            elif(type(Map_[0])) in (list, tuple, set):
                pass


    def __del__(self):
        pass
    def FinPatchPL(self,ci,cf,Map_,floor=[],not_floor=[]):
        pass

    def FindPathl2(self,ci,cf,data:dict,floor=[],not_floor=[]):
        if ci == cf:
            return [[ci]]
        l = [ci]
        t = []
        s = True
        while s:
            t.append(l[:])
            l.clear()
            for e in t[-1]:

                c1 = (e[0] - 1, e[1])
                c2 = (e[0] + 1, e[1])
                c3 = (e[0], e[1] - 1)
                c4 = (e[0], e[1] + 1)

                if c1 == cf:
                    l.append(c1)
                    s = False
                    break
                else:
                    if c1 in data:
                        if data[c1] != -1:
                            if(data[c1] not in not_floor) and (data[c1] in floor):
                                data[c1]=-1
                                l.append(c1)
                    else:
                        if 0 in floor:
                            data[c1] = -1
                            l.append(c1)
                if c2 == cf:
                    l.append(c2)
                    s=False
                    break
                else:
                    if c2 in data:
                        if data[c2]!=-1:
                            if (data[c2]not in not_floor) and (data[c2] in floor):
                                data[c2]=-1
                                l.append(c2)
                    else:
                        if 0 in floor:
                            data[c2] = -1
                            l.append(c2)

                if c3 == cf:
                    l.append(c3)
                    s=False
                    break
                else:
                    if c3 in data:
                        if data[c3]!=-1:
                            if (data[c3]not in not_floor) and (data[c3] in floor):
                                data[c3]=-1
                                l.append(c3)
                    else:
                        if 0 in floor:
                            data[c3] = -1
                            l.append(c3)

                if c4 == cf:
                    l.append(c4)
                    s=False
                    break
                else:
                    if c4 in data:
                        if data[c4] != -1:
                            if (data[c4] not in not_floor) and (data[c4] in floor):
                                data[c4] = -1
                                l.append(c4)
                    else:
                        if 0 in floor:
                            data[c4] = -1
                            l.append(c4)

    #def FinPatchl(self,ci,cf,Map_,floor=[],not_floor=[]):
    #    if ci == cf:
    #        return [[ci]]
    #    l=[ci]
    #    t=[]
    #    s = True
    #    #todo: mode vide
    #    while s:
    #        t.append(l[:])
    #        l.clear()
    #        XY = t[-1]
    #        E = True
    #        for e in XY:
    #            c1 = [e[0] - 1, e[1],e[2]]
    #            c2 = [e[0] + 1, e[1],e[2]]
    #            c3 = [e[0], e[1] - 1,e[2]]
    #            c4 = [e[0], e[1] + 1,e[2]]
    #            if c1 == cf:
    #                s = False
    #                break
    #            else:
    #                if c1 in Map_:
    #                    cc1 = [c1[0],c1[1],Map_[Map_.index([c1[0],c1[1]])][2]]
    #
    #                    Map_.remove(c1)
    #                    l.append(c1)
    #                else:
    #                    if (0 in floor) and (0 not in not_floor):
    #
    #
    #
    #    else:
    #        while s:
    #            t.append(l[:])
    #            l.clear()
    #            XY = t[-1]
    #            for e in XY:
    #                c1 = [e[0] - 1, e[1]]
    #                c2 = [e[0] + 1, e[1]]
    #                c3 = [e[0], e[1] - 1]
    #                c4 = [e[0], e[1] + 1]
    #
    #
    #
    #
    #
    #
    #


    def FinPatch(self,ci,cf,Map_,floor=[],not_floor=[]):
        i = int
        z = False
        if 0 in floor:
            z = True
        l = []
        for e in Map_:
            if (e[2] not in not_floor) and (e[2] in floor):
                l.append(e)
            else:
                if z and (e[2]not in not_floor):
                    l.append(e)
        Map_ = l[:]
        l.clear()
        t=[]
        s=True
        i=0
        E=True
        while s:
            t.append(l[:])
            l.clear()
            L = t[-1]
            for c in L:
                c1=c.up()
                c2=c.dow()
                c3=c.gauche()
                c4=c.droit()
                if c1 in Map_:
                    l.append(c1)
                    Map_.remove(c1)

                if c2 in Map_:

                    l.append(c2)
                    Map_.remove(c2)

                if c3 in Map_:
                    l.append(c3)
                    Map_.remove(c3)

                if c4 in Map_:
                    l.append(c4)
                    Map_.remove(c4)


    def findPatch(self ,ci ,cf ,Map_ ,floor=[] ,not_floor=[]):
        i=int
        z=False
        if 0 in floor:
            z=True
        if len(ci)==3:ci=[ci[0], ci[1]]
        if len(cf)==3:cf=[cf[0], cf[1]]
        l=[]
        for e in Map_:
            if len(e)==3:
                if(e[2] not in not_floor) and (e[2] in floor):
                    if len(e)==3:
                        e = p2(e[0],e[1],e[2])
                    elif len(e)==2:
                        e = p2(e[0],e[1])
                    l.append(e)
            else:
                if len(e)==2:
                    l.append(e)
        Map = l.copy()
        l.clear()
        if type(ci)==list:
            if len(ci)==2:
                ci = p2(ci[0],ci[1])
            elif len(ci)==3:
                ci = p2(ci[0],ci[1],ci[2])
            else:
                raise SyntaxError("'ci' not corect syntaxt")
        if type(cf)==list:
            if len(cf)==2:
                cf = p2(cf[0],cf[1])
            elif len(cf)==3:
                cf = p2(cf[0],cf[1],cf[2])
            else:
                raise SyntaxError("'ci' not corect syntaxt")
        l.append(ci)
        t=[]
        s = True
        i = 0
        E=True
        while s and(i<3):
            E = True
            t.append(l[:])
            l.clear()
            L = t[-1]
            print(L)
            if len(L)==0:
                L = t[-2]
                if len(L)==0:
                    raise Exception("chemain non trouver")

            for e in L:
                c1 = p2(e[0]-1,e[1])
                c2 = p2(e[0]+1,e[1])
                c3 = p2(e[0],e[1]-1)
                c4 = p2(e[0],e[1]+1)
                if c1 == cf:
                    s=False
                    E = False
                    break
                else:
                    if c1 in Map:
                        if not Map[Map.index(c1)].null():
                            E = False
                            Map.remove(c1)
                            Map.append(c1.nulifier())
                            l.append(c1)
                    else:
                        if z:
                            if e[2]not in not_floor:
                                E = False
                                Map.append(c1.nulifier())
                                l.append(c1)
                if c2==cf:
                    s = False
                    E = False
                    break
                else:
                    if c2 in Map:
                        if not Map[Map.index(c2)].null():
                            E = False
                            Map.remove(c2)
                            Map.append(c2.nulifier())
                            l.append(c2)
                    else:
                        if z:
                            if e[2]not in not_floor:
                                E = False
                                Map.append(c2.nulifier())
                                l.append(c2)
                if c3==cf:
                    s = False
                    E = False
                    break
                else:
                    if c3 in Map:
                        if not Map[Map.index(c3)].null():
                            E = False
                            Map.remove(c3)
                            Map.append(c3.nulifier())
                            l.append(c3)
                    else:
                        if z:
                            if e[2]not in not_floor:
                                E = False
                                Map.append(c3.nulifier())
                                l.append(c3)
                if c4 == cf:
                    E = False
                    s = False
                    break
                else:
                    if c4 in Map:
                        if not Map[Map.index(c4)].null():
                            E = False
                            Map.remove(c4)
                            Map.append(c4.nulifier())
                            l.append(c4)
                    else:
                        if z:
                            if e[2]not in not_floor:
                                E = False
                                Map.append(c1.nulifier())
                                l.append(c1)
                if E:
                    i += 1
        for e in t:
            for i in e:
                print(i)
import random
def genered(n=600,xMax=100,xMin=0,yMax=100,yMin=0):
    M=0
import numpy as np
M=Map(randmize=True,option2=True,nrandomize=800,x_min=-9,x_max=100,y_min=-10,y_max=100,c_min=1,c_max=3)


data=M.conv_MATPLOTcoord()
xpoints = np.array(data["x"])
ypoints = np.array(data["y"])

# out = ax.scatter(datax, datay, c=c, **param_dict)


plt.scatter(xpoints, ypoints,marker="x")
plt.show()



Patch ([4,7,5],[16,9,5],M,[1,2,3,4,5,6,7,8,9],[5 ,4])
