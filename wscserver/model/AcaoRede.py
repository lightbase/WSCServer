from pyramid_restler.model import SQLAlchemyORMContext
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper, relationship, backref
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session
from sqlalchemy.ext.declarative import declarative_base


class AcaoRede():

    """
    Classe que define a tabela 'acao_rede'
    """

    __tablename__ = 'acao_rede'
    id_acao_rede = Column(Integer, primary_key=True, nullable=False)
    id_acao = Column(String(30), ForeignKey('acao.id_acao'))
    id_rede = Column(Integer, ForeignKey('rede.id_rede'))
    dt_hr_coleta_forcada = Column(DateTime(timezone=False))

    def __init__(self, id_acao, id_rede, dt_hr_coleta_forcada):
        """
        Metodo que chama as colunas
        """
        self.id_acao_rede = id_acao_rede
        self.id_acao = id_acao
        self.id_rede = id_rede
        self.dt_hr_coleta_forcada = dt_hr_coleta_forcada

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<AcaoRede('%s, %s, %s, %s')>" % (self.id_acao_rede,
                                                 self.id_acao,
                                                 self.id_rede,
                                                 self.dt_hr_coleta_forcada
                                                 )


class AcaoRedeContextFactory(SQLAlchemyORMContext):
    entity = AcaoRede

    def session_factory(self):
        return session

acao_rede = Table('acao_rede', Base.metadata,
                  Column('id_acao_rede', Integer, primary_key=True,
                         nullable=False),
                  Column('id_acao', ForeignKey('acao.id_acao')),
                  Column('id_rede', ForeignKey('rede.id_rede')),
                  Column('dt_hr_coleta_forcada', DateTime(timezone=False)),
                  extend_existing=True
                  )

mapper(AcaoRede, acao_rede)
