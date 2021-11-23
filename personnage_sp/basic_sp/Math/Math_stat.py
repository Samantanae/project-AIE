import random
from math import pi, exp
import math

def ecart(v1,v2):
    return abs((v1-v2))
def ecart_type(v1,v2)->float:
    m = (v1 + v2)/2
    cv = (((ecart(v1,m))**0.5 + (ecart(v2,m))**0.5)/2)**0.5
    # étape par étape:
    #
    #

    return cv
def moyenne(l:list):
    t = len(l)
    print(t.conjugate())
    v = 0
    for e in l:
        v += e
    v /= t
    return v
def gauss(v1=0.0,v2=0.0):
    """
    :param mu: moyenne
    :param sigma: écart type
    :return:
    """
    mu = (v1 + v2)/2
    sigma = ecart_type(v1,v2)
    x = random.uniform(v1,v2)
    x -= mu
    x /= sigma
    x **= 2
    x *= -(1/2)
    x = exp(x)
    x *= 1/(sigma*(2*pi))
    r = [v1,v2]
    r = min(r)
    v4 = mu-r
    v4 *= x
    r += v4
    return r
print(gauss(5.9,8.9))



def stat_p1(v1,v2):
    """
    calcule une valeur alléatoire (suivant une fonction) entre les deux valeur.
    :param v1: valeur 1 ( vas devenir le min)
    :param v2: valeur 2 ( vas devenir le max)
    :return: valeur *aléatoire* entre les deux borne
    """
    if v2 < v1:
        v1, v2 = v2, v1
    v1, v2 = v1 - 5, v2 + 5 # todo: écat (pour permetre à certain individue de sortire du lot.
    return (v2/(1+exp(-random.random()*10+5)))+v1   # random.random() == x






def max_min(v_min,v_max,size=1000):
    v2 = random.random()
    v = v2 * size
    while (v < v_min) or (v > v_max):
        v2 = random.random()
        v = v2 * size
    return v


