import json

def getVersion():
    with open('versao.json') as versao:
        _info = json.load(versao)

    __version__ = _info['versao']
    return __version__

def setVersion(nVersao):
    with open('versao.json', 'r+') as f:
        data = json.load(f)
        data['versao'] = nVersao # <--- add `id` value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)

