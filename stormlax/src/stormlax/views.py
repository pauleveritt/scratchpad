from pyramid.view import view_config

@view_config(renderer="templates/site_index.pt")
def siteindex_view(request):
    return {}

