from pyramid.view import view_config
from pyramid.renderers import get_renderer
from pyramid.decorator import reify

class Views(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

        renderer = get_renderer("templates/global_layout.pt")
        self.template = renderer.implementation().macros['layout']

    @reify
    def company_name(self):
        return COMPANY

    @reify
    def site_menu(self):
        new_menu = SITE_MENU[:]
        url = self.request.url
        for menu in new_menu:
            if url.endswith(menu['href']):
                menu['current'] = True
            else:
                menu['current'] = False
            # Double-check for Home
            if menu['title'] == "Home" and url.endswith(".html"):
                menu['current'] = False
        return SITE_MENU

    @view_config(renderer="templates/index.pt")
    def index_view(self):
        return {"page_title": "Home"}


    @view_config(renderer="templates/departments.pt",
                 name="departments.html")
    def departments_view(self):
        return {"page_title": "Departments", "departments": DEPARTMENTS}


    @view_config(renderer="templates/people.pt", name="people.html")
    def people_view(self):
        return {"page_title": "People", "people": PEOPLE}


    @view_config(renderer="templates/projects.pt", name="projects.html")
    def projects_view(self):
        return {"page_title": "Projects", "projects": PROJECTS}

# Dummy data
DEPARTMENTS = [
        {'name': 'marketing', 'title': 'Marketing'},
        {'name': 'operations', 'title': 'Operations'},
]

PEOPLE = [
        {'name': 'sstanton', 'title': 'Susan Stanton'},
        {'name': 'bbarker', 'title': 'Bob Barker'},
]

PROJECTS = [
        {'name': 'sillyslogans', 'title': 'Silly Slogans'},
        {'name': 'meaninglessmissions', 'title': 'Meaningless Missions'},
]

COMPANY = "ACME, Inc."

SITE_MENU = [
        {'href': '', 'title': 'Home'},
        {'href': 'departments.html', 'title': 'Departments'},
        {'href': 'people.html', 'title': 'People'},
        {'href': 'projects.html', 'title': 'Projects'},
]
