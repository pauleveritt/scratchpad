from pyramid.view import view_config

from dummy_data import COMPANY
from dummy_data import PEOPLE
from dummy_data import PROJECTS

from layout import GlobalLayout

class Views(GlobalLayout):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(renderer="templates/index.pt")
    def index_view(self):
        return {"page_title": "Home"}

    @view_config(renderer="templates/about.pt", name="about.html")
    def about_view(self):
        return {"page_title": "About"}

    @view_config(renderer="templates/company.pt",
                 name="acme")
    def company_view(self):
        return {"page_title": COMPANY + " Projects",
                "projects": PROJECTS}

    @view_config(renderer="templates/people.pt", name="people")
    def people_view(self):
        return {"page_title": "People", "people": PEOPLE}


