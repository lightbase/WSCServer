from wscserver.model.Coleta import ColetaContextFactory
from wscserver.view.restfulview import CustomRESTfulView
from wscserver.model.So import SoContextFactory

def make_routes(config):
    """
    Cria rotas
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_restful_routes(
            'rest/coleta', ColetaContextFactory, view=CustomRESTfulView)
    config.add_restful_routes('rest/coleta2', ColetaContextFactory)
    config.add_route('download','zip/coleta')
    config.add_restful_routes('rest/so', SoContextFactory)
    config.enable_POST_tunneling()
