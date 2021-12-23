from personnage_sp.basic_sp.Basic import Basic

class Soif(Basic):
    #__slots__ = "v_min", "v", "v_max",\
    #            "m", "m_max", "m_min",\
    #            "Bv_max", "save", "Id","file"
    def __init__(self, Id=None, pere=None, mere=None, v_max=100, v_min=20, m_max=10, m_min=0.00001,   #todo: psoblement à refaire (il manque de réel donnée!)
                 size=100):
        super(Soif, self).__init__(
            file="Soif.csv", Id=Id,
            pere=pere, mere=mere,
            v_max=v_max, v_min=v_min,
            m_max=m_max, m_min=m_min,
            size=size)


