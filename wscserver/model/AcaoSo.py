from pyramid_restler.model import SQLAlchemyORMContext
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper, relationship, backref
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from wscserver.model import Base, session


class AcaoSo():

    """
    Classe que define a tabela 'acao_so'

    """
    __tablename__ = 'acao_so'
    id_acao_so = Column(Integer, primary_key=True, nullable=False)
    id_acao = Column(String(30), ForeignKey('acao.id_acao'))
    id_rede = Column(Integer, ForeignKey('rede.id_rede'))
    id_so = Column(Integer, ForeignKey('so.id_so'))

    def __init__(self, id_acao_so, id_acao, id_rede, id_so):
        """
        Metodo que chama as colunas
        """
        self.id_acao_so = id_acao_so
        self.id_acao = id_acao
        self.id_rede = id_rede
        self.id_so = id_so

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<AcaoSo('%s, %s, %s, %s')>" % (self.id_acao_so,
                                               self.id_acao,
                                               self.id_rede,
                                               self.id_so
                                               )


class AcaoSoContextFactory(SQLAlchemyORMContext):
    entity = AcaoSo

    def session_factory(self):
        return session

acao_so = Table('acao_so', Base.metadata,
                Column('id_acao_so', Integer, primary_key=True,
                       nullable=False),
                Column('id_acao', String(30), ForeignKey("acao.id_acao")),
                Column('id_rede', Integer, ForeignKey("rede.id_rede")),
                Column('id_so', Integer, ForeignKey("so.id_so")),
                )
mapper(AcaoSo, acao_so)
