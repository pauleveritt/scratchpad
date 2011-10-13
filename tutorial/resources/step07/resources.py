
class Folder(dict):
    __name__ = ''
    __parent__ = None
    pass

def bootstrap(request):
    root = Folder()
    
    return root
