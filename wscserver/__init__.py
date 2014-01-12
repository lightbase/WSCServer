from pyramid.config import Configurator
from pyramid_restler import includeme

from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.orm import sessionmaker

from wscserver.config.routing import make_routes
from wscserver.model import initialize_sql, sqlalchemy_url


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.scan('wscserver.model')  # the "important" line
    engine = create_engine(sqlalchemy_url)
    initialize_sql(engine)
    includeme(config)

    make_routes(config)
    config.scan('wscserver')
    return config.make_wsgi_app()
