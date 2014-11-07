from wscserver.model.Coleta import ColetaContextFactory
#from wscserver.view.restfulview import CustomRESTfulView
from wscserver.model.So import SoContextFactory

from wscserver.view.restfulview import viewcoleta

def make_routes(config):
    """
    Cria rotas
    """


    config.add_route('the_big_colect', 'rest/coleta', request_method='GET')
    config.add_view(view=viewcoleta, route_name='the_big_colect', request_method='GET')

    config.add_static_view('static', 'static', cache_max_age=3600)
    #config.add_restful_routes(
    #        'rest/coleta', ColetaContextFactory, view=CustomRESTfulView)
    config.add_restful_routes('rest/coleta2', ColetaContextFactory)
    config.add_route('download','zip/coleta')
    config.add_restful_routes('rest/so', SoContextFactory)
    config.enable_POST_tunneling()
