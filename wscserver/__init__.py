

from sqlalchemy import create_engine
from pyramid_restler import includeme
from pyramid.config import Configurator
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """

    from wscserver.model import initialize_sql

    initialize_sql(settings)
    config = Configurator(settings=settings)
    config.scan('wscserver.model')  # the "important" line

    from wscserver.config.routing import make_routes

    includeme(config)
    make_routes(config)
    config.scan('wscserver')

    return config.make_wsgi_app()
