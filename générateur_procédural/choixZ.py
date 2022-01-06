import random
from statistics import median, variance


class P2:
    __slots__ = "x", "y", "z"

    def __init__(self, x, y, z=0.):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if type(other) == P2:
            return (self.x == other.x) and (self.y == other.y)
        elif len(other) == 2:
            return (self.x == other[0]) and (self.y == other[1])

    def Z(self):
        return self.z

    def __hash__(self):
        hash((self.x, self.y))

    def __float__(self):
        return self.z


class MapProceduralGeneretor:
    __slots__ = "xMin", "xMax", "yMin", "yMax", "zMin", "zMax", "M", "tz", "posiX", "posiY"

    def __init__(self, xMin=0, xMax=80, yMin=0, yMax=20, zMin=0., zMax=1.):
        self.xMin = int(xMin)
        self.xMax = int(xMax)
        self.yMin = int(yMin)
        self.yMax = int(yMax)
        self.zMin = zMin
        self.zMax = zMax

        self.M = []

        self.generate()

    def generate(self, retour=False):
        for x in range(self.xMin, self.xMax):
            for y in range(self.yMin, self.yMax):
                z = self.choiceZ(x, y)
                # print(f"{x,}\t{ y,}\t \t{ z}")
                self.M.append(P2(x, y, z))

        if retour:
            return self.M

    def choiceZ(self, x, y) -> float:
        self.tz = []
        self.INM(P2(x + 1, y))
        self.INM(P2(x - 1, y))
        self.INM(P2(x, y + 1))
        self.INM(P2(x, y - 1))

        if len(self.tz) == 0:
            z = self.varianceZ(z=0)
        else:
            z = self.moyenne(data=self.tz)
            try:
                info2Z = median(data=self.tz)
                info3Z = variance(self.tz)
            except:
                pass

            z = self.varianceZ(z=z)
        return z

    def INM(self, c):
        if c in self.M:
            if self.M[self.M.index(c)].z is not None:
                self.tz.append(self.M[self.M.index(c)].z)

    def varianceZ(self, z):
        v1 = (self.zMax - self.zMin)
        chutemax = v1 - (v1 / 2)
        chutemin = -1 * chutemax
        var = random.uniform(chutemin, chutemax)
        if z is None:
            return z
        else:
            z += var
            return z

    def moyenne(self, data: list):
        t = 0
        if len(data) != 0:
            for d in data:
                t += float(d)
            t /= len(data)
            # del d
            return t
        else:
            return 0

    def CTC(self, v, filtre=None):
        if filtre is None:
            if v == 0:
                r = " "
            elif v == 1:
                r = "."
            elif v == 2:
                r = "¨"
            elif v == 3:
                r = "^"
            elif v == 4:
                r = "*"
            elif v == 5:
                r = "!"
            elif v == 6:
                r = "?"
            elif v == 7:
                r = "#"
            elif v == 8:
                r = "%"
            else:
                r = "&"
            return r
        else:
            r = None
            if v == 0:
                if v in filtre:
                    r = " "
            elif v == 1:
                if v in filtre:
                    r = "."
            elif v == 2:
                if v in filtre:
                    r = "¨"
            elif v == 3:
                if v in filtre:
                    r = "^"
            elif v == 4:
                if v in filtre:
                    r = "*"
            elif v == 5:
                if v in filtre:
                    r = "!"
            elif v == 6:
                if v in filtre:
                    r = "?"
            elif v == 7:
                if v in filtre:
                    r = "#"
            elif v == 8:
                if v in filtre:
                    r = "%"
            else:
                if v in filtre:
                    r = "&"

            if r is None:
                r = " "
            return r

    def mode_simple(self, v):
        return int(((v % 1) * 10) // 1)

    def __str__(self):
        result2 = ""
        for y in range(self.yMin, self.yMax):
            result = f"{y}\t"
            for x in range(self.xMin, self.yMax):
                try:
                    p = (x, y)
                    z = self.M[self.M.index(p)].z
                    z = self.mode_simple(z)
                    result += f" {self.CTC(z)}"
                except:
                    result += "*"
            result2 += f"{result}\n"
        return result2
    def __iter__(self):
        self.posiX = 0
        self.posiY = 0
        return self
    def __next__(self):
        if self.posiX >= (self.xMax-1):
            if self.posiY >= (self.yMax-1):
                raise StopIteration
            else:
                self.posiY += 1
                self.posiX = 0
        else:
            self.posiX += 1
        p = (self.posiX,self.posiY)
        return self.M[self.M.index(p)]



a = MapProceduralGeneretor()

print(a)
