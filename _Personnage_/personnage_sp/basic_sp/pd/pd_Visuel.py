#pd_Visuel
from direct.actor.Actor import Actor
from direct.task import Task


class visuel:
    def __init__(self,master):





        print("noeux (visuel) ajouté")
        self.M_visuel = master.attachNewNode("Dummy Node Visuel")

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.M_visuel)
