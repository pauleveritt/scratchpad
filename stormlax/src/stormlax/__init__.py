
from pyramid.config import Configurator

from resources import root_factory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=root_factory,settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    from resources import root
    root.bootstrap(settings['var_dir'])

    return config.make_wsgi_app()
