class P2V2:
    __slots__ = "x","y","c","active","vide","test"
    def __init__(self,x,y,c=0,vide=False):
        self.x=x
        self.y=y
        self.c=c
        self.active=True
        self.vide=vide
        self.test=[]
    def print_(self):
        print(self.test)
        self.test.clear()
    def r(self):
        self.test.clear()
    def infovide(self):
        return self.vide
    def activide(self):
        self.vide=True
    def unacvide(self):
        self.vide=False
    def __getitem__(self, item):
        if item==0:
            return self.x
        elif item==1:
            return self.y
        elif item==2:
            return self.c
        else:
            raise IndexError
    def __setitem__(self, key, value):
        if key==0:
            self.x=value
        elif key==1:
            self.y=value
        elif key==2:
            self.c=value
        else:
            raise IndexError
    def __eq__(self, other):
        self.test.append(other)
        if type(other)==P2V2:
            if self.active:
                return (self.x==other.x)and(self.y==other.y)
            else:
                return False
        elif type(other)==int:
            return other==self.c
    def inactivation(self):
        self.active=False
    def activation(self):
        self.active=True
    def up(self):
        return P2V2(self.x,self.y+1,self.c)
    def down(self):
        return P2V2(self.x,self.y-1,self.c)
    def gauche(self):
        return P2V2(self.x-1,self.y,self.c)
    def droite(self):
        return P2V2(self.x+1,self.y,self.c)
    def __del__(self):
        del self.x
        del self.y
        del self.c
        del self.active
    def __str__(self):
        return f"(({self.x},\t{self.y}),\tc:{self.c},\tactive:{self.active},\tvide:{self.vide})"


class Patchv2:
    __slots__ = "data","ci","cf","floor",\
                "not_floor","_patch",\
                "l","t"
    def __init__(self,ci,cf,data,floor:list,not_floor:list):
        """
        :param ci:
        :param cf:
        :param data:
        :param floor:
        :param not_floor:
        """
        if -1 in floor:
            floor.remove(-1)
        if -1 not in not_floor:
            not_floor.append(-1)


        self.data = data[:]
        self.ci=self.conv_p2v2(ci)
        self.cf=self.conv_p2v2(cf)
        print(type(self.ci))
        self.floor=floor
        self.not_floor=not_floor
        self._patch=[]
        self.l=[]
        self.l.append(ci)
        self.t=[]
        self.findPatch()
    def conv_p2v2(self,c):
        if type(c)==tuple:
            if len(c)<=1:
                raise Exception("ceci n'ais pas une coordonner")
            elif len(c)==2:
                c = P2V2(c[0],c[1])
            else:
                c = P2V2(c[0],c[1],c[2])
        return c
    def findPatch(self):
        if self.ci==self.cf:
            return [[self.ci]]
        if 0 in self.floor:
            self.Pzero()
        else:
            self.PNotZero()

    def PNotZero(self):
        s = True
        print(self.l)
        self.l.append(self.cf)
        while s:
            if len(self.l)==0:
                print("fall")
                print(type(self.cf))
                break
            self.t.append(self.l[:])
            self.l.clear()
            co = self.t[-1]

            for c in co:
                c = self.conv_p2v2(c)
                print("c")
                print(type(c))
                print(c)
                c1 = self._testNotZero(P2V2(c[0],c[1]+1,c[2]))
                print(type(c1))
                if c1==self.cf:
                    s=False
                    break
                c2 = self._testNotZero(P2V2(c[0]+1,c[1],c[2]))
                print(type(c2))
                if c2==self.cf:
                    s=False
                    break
                c3 = self._testNotZero(P2V2(c[0],c[1]-1,c[2]))
                if c3==self.cf:
                    s=False
                    break
                c4 = self._testNotZero(P2V2(c[0]-1,c[1],c[2]))
                if c4==self.cf:
                    s=False
                    break
        self._patch=self.t[:]

    def Pzero(self):
        pass


    def _testNotZero(self,c):
        print(c)
        if c in self.data:      #bool in(const P2V2 c,const std::vector<P2V2>&data){bool s=false;for(P2V2 e:data){if(e==c){s=true;}}bool&rs=s;return rs;}
            print(c.test)
            if self.data[self.data.index(c)] not in self.not_floor:      # not_floor: [-1]
                if self.data[self.data.index(c)] in self.floor:
                    self.data[self.data.index(c)].inactivation()
                    self.l.append(c)
                    return c.unacvide()  # pourais aussi juste être: return c
                else:
                    print("not in floor")
            else:
                print("in not_floor")
        else:
            print("not in data")
        c.vide=True
        return c




    def _testZero(self,c):
        if c in self.data:
            if self.data[self.data.index(c)] not in self.not_floor:
                self.data[self.data.index(c)].inactivation()
                self.l.append(c)
                return c
        return c.activide()
    def _getUniquePatch(self):
        pass

    def __str__(self):
        r = ""
        for e1 in self.t:
            for e2 in e1:
                r += str(e2)
            r+="\n"
        return r

def genereted_line_type1(ci, cf, TYPE=1, epaiseur=1,M=None):
    a = float
    if M is None:
        M=[]
    a = (cf[1] - ci[1]) / (cf[0] - ci[0])
    for e in range(epaiseur):

        b = (cf[1] + e) - ((cf[0] + e) * a)  # b=y-ax
        for x in range(ci[0], cf[0]):
            y = int(a * x + b)
            M.append(P2V2(x=x,y=y,c=TYPE))
    return M

ma = genereted_line_type1(P2V2(1,5),P2V2(43,43),epaiseur=500)
ma = genereted_line_type1(P2V2(53,32),P2V2(4,0),epaiseur=500,M=ma)
print(Patchv2((53,32),(4,0),ma,[1],[8]))