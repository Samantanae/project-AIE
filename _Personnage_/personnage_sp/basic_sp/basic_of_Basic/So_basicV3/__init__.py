import os
print(os.getcwd())
def _get_global_file(file: str = "Perso_v2") -> str:
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
    return (_get_global_file(file=file) + "\ "[0] + new_file)
def _prep_patch(fileBase, file):
    return os.path.join(_get_global_file(file=fileBase), file)
def GRIP(fileBase: str = "Perso_v2", file: str = "infosPersonnages", mode=0o666):
    if _verifie_si_existe(path=_get_global_file(file=fileBase), file=file):
        return _newPatch(file=fileBase, new_file=file)
    else:
        path = _prep_patch(fileBase=fileBase, file=file)
        os.mkdir(path, mode)
        print("Directory '%s' created" % path)
        return path
def OGRIP(oblige=True, fileBase="Perso_v2", file="infosPersonnages", mode=0o666):
    os.makedirs(_prep_patch(fileBase, file), mode)

patch = GRIP()

def reset():
    OGRIP()





