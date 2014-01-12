from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class AcaoExcecao():

    """
    Classe que define a tabela 'acao_excecao'

    """

    __tablename__ = 'acao_excecao'
    id_acao_excecao = Column(Integer, primary_key=True, nullable=False)
    te_node_address = Column(String(17), nullable=False)
    id_acao = Column(String(30), ForeignKey('acao.id_acao'))
    id_rede = Column(Integer, ForeignKey('rede.id_rede'))

    def __init__(self, te_node_address, id_acao, id_rede):
        """
        Metodo que chama as colunas
        
        """

        self.te_node_address = te_node_address
        self.id_acao = id_acao
        self.id_rede = id_rede

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
         
        """
        return "<AcaoExcecao('%s, %s, %s')>" % (self.te_node_address,
                                                self.id_acao,
                                                self.id_rede,
                                                )


class AcaoExcecaoContextFactory(SQLAlchemyORMContext):
    entity = AcaoExcecao

    def session_factory(self):
        return session

acao_excecao = Table('acaoExcecao', Base.metadata,
                     Column('id_acao_excecao', Integer, primary_key=True,
                            nullable=True),
                     Column('te_node_address', String(17), nullable=False),
                     Column('id_acao', String(30), ForeignKey('acao.id_acao')),
                     Column('id_rede', Integer, ForeignKey('rede.id_rede')),
                     extend_existing=True
                     )

mapper(AcaoExcecao, acao_excecao)
