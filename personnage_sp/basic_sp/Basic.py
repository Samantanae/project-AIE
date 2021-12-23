from personnage_sp.basic_sp.basic_of_Basic.So_basic import So_basic


class Basic(So_basic):
    __slots__ = "v_min", "v", "v_max", \
                "m", "m_max", "m_min", \
                "Bv_max", "save", "Id", "file"

    def __init__(self, file=None, Id=None, pere=None,
                 mere=None, v_max=1, v_min=1, v=1, m=0,
                 m_max=0, m_min=0, size=100):
        super(Basic, self).__init__(
            file=file, Id=Id,
            pere=pere, mere=mere,
            v_max=v_max, v_min=v_min,
            m_max=m_max, m_min=m_min,
            v=v, m=m, size=size)

    def dead(self) -> bool:
        return self.v <= 0
