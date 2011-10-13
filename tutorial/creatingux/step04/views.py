from pyramid.view import view_config

@view_config(renderer="index.pt")
def index_view(request):
    return {"company": COMPANY}


@view_config(renderer="departments.pt", name="departments.html")
def departments_view(request):
    return {"company": COMPANY, "departments": DEPARTMENTS}


@view_config(renderer="people.pt", name="people.html")
def people_view(request):
    return {"company": COMPANY, "people": PEOPLE}

@view_config(renderer="projects.pt", name="projects.html")
def projects_view(request):
    return {"company": COMPANY, "projects": PROJECTS}

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