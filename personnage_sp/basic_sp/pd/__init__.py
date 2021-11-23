from personnage_sp.basic_sp.pd.pd_Geo import Geo
from personnage_sp.basic_sp.pd.pd_Visuel import visuel




class Geo_and_visual(Geo,visuel):
    def __init__(self,master):
        # Geo -> visual

        self.M_Global = master.attachNewNode("Dummy Node global personnage")

        super(Geo_and_visual, self).__init__(master=self.M_Global)


