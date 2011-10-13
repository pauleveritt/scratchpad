
class Folder(dict):
    __name__ = ''
    __parent__ = None
    pass

class Document(object):

    def __init__(self, name, parent):
        self.__name__ = name
        self.__parent__ = parent


def bootstrap(request):
    root = Folder()
    doc1 = Document('doc1', root)
    root['doc1'] = doc1
    
    return root
