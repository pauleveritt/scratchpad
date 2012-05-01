from os import listdir

from pyramid.view import view_config

from layout import Layouts

class StormlaxViews(Layouts):

    def __init__(self, request):
        self.request = request

    @view_config(renderer="templates/siteindex.pt")
    def siteindex_view(self):
        return {"page_title": "Home"}