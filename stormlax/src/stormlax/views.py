from os import listdir

from pyramid.view import view_config

from layout import Layouts
from resources import SiteFolder
from resources import Roster

class StormlaxViews(Layouts):

    def __init__(self, request):
        self.request = request

    @view_config(renderer="templates/siteindex.pt", context=SiteFolder)
    def siteindex_view(self):
        class Roster:
            team_name = 'Blue'
        roster = Roster()
        page_title = 'Welcome to STORM 2012'
        return dict(
            page_title=page_title, roster=roster
            )

    @view_config(renderer="templates/roster.pt", context=Roster)
    def roster_view(self):
        class Roster:
            team_name = 'Blue'
        roster = Roster()
        page_title = 'STORM Blue'
        return dict(
            page_title=page_title, roster=roster, subnav=True,
            )