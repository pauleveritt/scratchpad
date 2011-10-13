from pyramid.renderers import get_renderer
from pyramid.view import view_config

def site_layout():
    renderer = get_renderer("templates/global_layout.pt")
    layout = renderer.implementation().macros['layout']
    return layout


@view_config(renderer="templates/index.pt")
def index_view(request):
    return {"company": COMPANY, "layout": site_layout(),
            "page_title": "Home"}


@view_config(renderer="templates/departments.pt",
             name="departments.html")
def departments_view(request):
    return {"company": COMPANY, "layout": site_layout(),
            "page_title": "Departments", "departments": DEPARTMENTS}


@view_config(renderer="templates/people.pt", name="people.html")
def people_view(request):
    return {"company": COMPANY, "layout": site_layout(),
            "page_title": "People", "people": PEOPLE}


@view_config(renderer="templates/projects.pt", name="projects.html")
def projects_view(request):
    return {"company": COMPANY, "layout": site_layout(),
            "page_title": "Projects", "projects": PROJECTS}

# Dummy data
COMPANY = "ACME, Inc."

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