# from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import create_engine
from pyramid import config
from paste.deploy.loadwsgi import appconfig

sqlalchemy_url = 'postgresql://rest:rest@localhost/cacic'
DBSession = scoped_session(sessionmaker())
Base = declarative_base()
engine = create_engine(sqlalchemy_url)
Session = sessionmaker(bind=engine)
session = Session()


def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    # Base.metadata.create_all(engine)
