from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class AplicativoRede():

    """
    Classe que define a tabela 'aplicativo_rede'

    """

    __tablename__ = 'aplicativo_rede'
    id_rede = Column(Integer, ForeignKey('rede.id_rede'), primary_key=True)
    id_aplicativo = Column(Integer, ForeignKey('aplicativo.id_aplicativo'),
                           primary_key=True)

    def __init__(self, id_rede, id_aplicativo):
        """
        Metodo que chama as colunas
        """
        self.id_rede = id_rede
        self.id_aplicativo = id_aplicativo

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<AplicativoRede('%s, %s')>" % (self.id_rede,
                                               self.id_aplicativo
                                               )


class AplicativoRedeContextFactory(SQLAlchemyORMContext):
    entity = AplicativoRede

    def session_factory(self):
        return session

aplicativo_rede = Table('aplicativoRede', Base.metadata,
                        Column('id_rede', Integer, ForeignKey('rede.id_rede'),
                               primary_key=True),
                        Column('id_aplicativo', Integer,
                               ForeignKey('aplicativo.id_aplicativo'),
                               primary_key=True),
                        extend_existing=True
                        )

mapper(AplicativoRede, aplicativo_rede)
