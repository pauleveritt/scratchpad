from pyramid.renderers import get_renderer
from pyramid.decorator import reify

class Layouts(object):

    @reify
    def global_template(self):
        renderer = get_renderer("templates/global_layout.pt")
        return renderer.implementation().macros['layout']

    @reify
    def project_name(self):
        return 'STORM Dashboard'

    @reify
    def site_root(self):
        return self.request.root

    @reify
    def site_nav(self):
        results = list(self.request.root.rosters)
        name = self.request.context.__name__
        for result in results:
            if result['id'] == name:
                result['active'] = 'active'
            else:
                result['active'] = ''

        return results