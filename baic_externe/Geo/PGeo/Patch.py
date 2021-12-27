class P2V2:
    __slots__ = "x","y","c","active"
    def __init__(self,x,y,c=0):
        self.x=x
        self.y=y
        self.c=c
        self.active=True

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
        if self.active:
            return (self.x==other.x)and(self.y==other.y)
        return False
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
        print("delete")



class Patchv2:
    __slots__ = "data","ci","cf","floor",\
                "not_floor","_patch",\
                "l","t"
    def __init__(self,ci,cf,data:list,floor:list,not_floor:list):
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

        self.data = data
        self.ci=ci
        self.cf=cf
        self.floor=floor
        self.not_floor=not_floor
        self._patch=[]
        self.l=[]
        self.l.append(ci)
        self.t=[]

    def findPatch(self):
        if self.ci==self.cf:
            return [[self.ci]]