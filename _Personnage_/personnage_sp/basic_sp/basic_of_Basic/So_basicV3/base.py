import json, os

class modeText:
    def __init__(self,directory=None,file=None):
        self.ABSdirectory = None
        self.directory = None
        if file is not None:
            if ".txt" not in file:
                file += ".txt"
            if directory is not None:
                if file not in directory:
                    self.ABSdirectory = os.path.join(directory,file)
                    self.directory = file
                else:
                    self.ABSdirectory = directory
            else:
                self.directory = file
                self.ABSdirectory = os.path.join(os.getcwd(), self.directory)
        else:
            l = os.listdir()







class modeJson:
    pass



class modeCSV:
    pass



