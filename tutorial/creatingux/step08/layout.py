from pyramid.renderers import get_renderer
from pyramid.decorator import reify

from dummy_data import COMPANY
from dummy_data import SITE_MENU

class GlobalLayout(object):

    @reify
    def global_template(self):
        renderer = get_renderer("templates/global_layout.pt")
        return renderer.implementation().macros['layout']

    @reify
    def company_name(self):
        return COMPANY

    @reify
    def site_menu(self):
        new_menu = SITE_MENU[:]
        url = self.request.url
        for menu in new_menu:
            # TODO XXX This breaks on root
            if url.endswith(menu['href']):
                menu['current'] = True
            else:
                menu['current'] = False
                # Double-check for Home
            if menu['title'] == "Home" and url.endswith(".html"):
                menu['current'] = False
        return SITE_MENU

