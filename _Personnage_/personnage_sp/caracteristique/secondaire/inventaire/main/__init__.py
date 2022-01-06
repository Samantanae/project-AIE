from _Personnage_.personnage_sp.basic_sp.Basic import Basic

class main(Basic):
    def __init__(self,file,pere=None,mere=None):
        super(main, self).__init__(file=file,pere=pere,mere=mere)


    def __init__(self, file=None, Id=None, pere=None,
                 mere=None, v_max=1, v_min=1, v=1, m=0,
                 m_max=0, m_min=0, size=100):
