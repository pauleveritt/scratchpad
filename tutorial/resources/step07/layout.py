from pyramid.decorator import reify
from pyramid.events import subscriber
from pyramid.events import BeforeRender
from pyramid.renderers import get_renderer
from pyramid.url import static_url

class Layout(object):
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


@subscriber(BeforeRender)
def add_renderer_globals(event):
    request, context = event['request'], event['context']
    event['layout'] = Layout(context, request)

# Dummy data
COMPANY = "ACME, Inc."

SITE_MENU = [
        {'href': '', 'title': 'Home'},
        {'href': 'departments.html', 'title': 'Departments'},
        {'href': 'people.html', 'title': 'People'},
        {'href': 'projects.html', 'title': 'Projects'},
]