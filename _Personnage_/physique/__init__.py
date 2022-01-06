from direct.showbase.ShowBase import ShowBase




def test(loader):
    return loader.loadModel("/c/Users/Samuel Gauthier/Desktop/python/Perso_v2/_Personnage_/physique/head/head.bam")


class MyApp(ShowBase):

    def __init__(self):
        super(MyApp, self).__init__()
        #ShowBase.__init__(self)

        # Load the environment model.

        "/c/Users/Samuel Gauthier/Desktop/python/Perso_v2/_Personnage_/physique/head/head.bam"
        self.scene = test(self.loader)
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(25, 25, 25)
        self.scene.setPos(-8, 42, 0)


app = MyApp()
app.run()