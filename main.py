from direct.showbase.ShowBase import ShowBase
from Personnages import Personnages

class MyApp(ShowBase):

    def __init__(self):
        super(MyApp, self).__init__()

        self.Man = Personnages(self.render)

app = MyApp()
app.run()