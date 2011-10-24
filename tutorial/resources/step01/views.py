from pyramid.view import view_config

from resources import SiteFolder
from resources import Folder
from resources import Document

@view_config(renderer="templates/site_view.pt",
             context=SiteFolder)
def site_view(request):
    return {"content_type": "Site"}


@view_config(renderer="templates/folder_view.pt",
             context=Folder)
def folder_view(request):
    return {"content_type": "Folder"}


@view_config(renderer="templates/document_view.pt",
             context=Document)
def document_view(request):
    return {"content_type": "document"}
