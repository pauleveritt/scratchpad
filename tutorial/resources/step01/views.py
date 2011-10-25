from pyramid.response import Response
from pyramid.view import view_config

from resources import SiteFolder

class ProjectorViews(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(context=SiteFolder)
    def site_view(self):
        body = "This SiteFolder is named: " + self.context.title
        return Response(body)

