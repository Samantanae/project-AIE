import json
import os

print(os.getcwd())


def _get_global_file(file: str = "Perso_v2") -> str:
    """
    :param file:
    :return:
    """
    exP = os.getcwd()
    exP = exP.split("\ "[0])
    r = ""
    print(exP)
    s = True
    for e in exP:
        if not s:
            break
        else:
            if e == file:
                r += e
                break
            else:
                r += e + "\ "[0]
    print(r)
    return r


def _verifie_si_existe(path, file: str = "infosPersonnages") -> bool:
    """

    :param path:
    :param file:
    :return:
    """
    dir_list = os.listdir(path=path)
    # todo: passeras par un autre chemain pour évité de
    #    perdre de la mémoire en ne suppriment pas la liste
    #   encien chemin:
    #   return file in dir_list
    if file in dir_list:
        del dir_list
        return True
    else:
        del dir_list
        return False


def _newPatch(file: str, new_file: str) -> str:
    """

    :param file:
    :param new_file:
    :return:
    """
    return (_get_global_file(file=file) + "\ "[0] + new_file)


def _prep_patch(fileBase, file):
    """

    :param fileBase:
    :param file:
    :return:
    """
    return os.path.join(_get_global_file(file=fileBase), file)


def _GRIP_(fileBase: str = "Perso_v2", file: str = "infosPersonnages", mode=0o666):
    """

    :param fileBase:
    :param file:
    :param mode:
    :return:
    """
    if _verifie_si_existe(path=_get_global_file(file=fileBase), file=file):
        return _newPatch(file=fileBase, new_file=file)
    else:
        path = _prep_patch(fileBase=fileBase, file=file)
        os.mkdir(path, mode)
        print("Directory '%s' created" % path)
        return path


def OGRIP(oblige=True, fileBase="Perso_v2", file="infosPersonnages", mode=0o666):
    """

    :param oblige:
    :param fileBase:
    :param file:
    :param mode:
    :return:
    """
    os.makedirs(_prep_patch(fileBase, file), mode)


patch = _GRIP_()


def reset():
    OGRIP()


###################################################
###################################################
def newTEXT(file=None):
    """

    :param file:
    :return:
    """
    pass


def newCSV():
    pass


def newJSON(data=None, file=None, ID=None)->str:
    """

    :param data:
    :param file:
    :param ID:
    :return:
    """
    if data is None:
        data = {}
    info = os.listdir(path=patch)
    prefix = ".json"
    p = 0
    if file is not None:
        if prefix in file:
            file = file.replace(prefix, "")
        t = f"{file}{p}{prefix}"
        while t in info:
            p += 1
            t = f"{file}{p}{prefix}"
    else:
        t = f"{p}{prefix}"
        while t in info:
            p += 1
            t = f"{p}{prefix}"
    rf = os.path.join(patch, t)
    with open(rf, "w") as f:
        json.dump(f, data, indent=4, sort_keys=True)
    return rf


def get_patch(ID, file, prefix=".json"):
    """

    :param ID:
    :param file:
    :param prefix:
    :return:
    """
    ID += prefix
    file += ID
    return os.path.join(patch, file)

# class DocData:
#    def __init__(self):
#        self.patch=patch
#        self.ID={}
#
#    def newTEXT(self,file=None):
#        """
#
#        :param file:
#        :return:
#        """
#        pass
#    def newCSV(self):
#        pass
#    def newJSON(self, data=None, file=None, ID=None):
#        """
#
#        :param data:
#        :param file:
#        :param ID:
#        :return:
#        """
#        if data is None:
#            data = {}
#        info = os.listdir(path=self.patch)
#        prefix = ".json"
#        p = 0
#        if file is not None:
#            if prefix in file:
#                file = file.replace(prefix,"")
#            t = f"{file}{p}{prefix}"
#            while t in info:
#                p += 1
#                t = f"{file}{p}{prefix}"
#        else:
#            t = f"{p}{prefix}"
#            while t in info:
#                p += 1
#                t = f"{p}{prefix}"
#        rf = os.path.join(self.patch,t)
#        with open(rf,"w") as f:
#            json.dump(f,data, indent=4, sort_keys=True)
#    def get_patch(self,ID,file,prefix=".json"):
#        """
#
#        :param ID:
#        :param file:
#        :param prefix:
#        :return:
#        """
#        ID += prefix
#        file += ID
#        return os.path.join(self.patch,file)
#
