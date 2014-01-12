from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class DescricaoColunaComputador():

    """
    Classe que define a tabela 'descricao_coluna_computador'

    """

    __tablename__ = 'descricao_coluna_computador'
    te_source = Column(String(100), primary_key=True, nullable=False)
    te_target = Column(String(100), primary_key=True, nullable=False)
    te_description = Column(String(100), nullable=False)
    cs_condicao_pesquisa = Column(String(1), nullable=False)

    def __init__(self, te_source, te_target, te_description,
                 cs_condicao_pesquisa):
        """
        Metodo que chama as colunas
        """
        self.te_source = te_source
        self.te_target = te_target
        self.te_description = te_description
        self.cs_condicao_pesquisa = cs_condicao_pesquisa

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<DescricaoColunaComputador('%s, %s, %s, %s')>" %\
            (self.te_source,
             self.te_target,
             self.te_description,
             self.cs_condicao_pesquisa
             )


class DescricaoColunaComputadorContextFactory(SQLAlchemyORMContext):
    entity = DescricaoColunaComputador

    def session_factory(self):
        return session

descricao_coluna_computador = Table(
    'descricao_coluna_computador', Base.metadata,
    Column('te_source', String(100),
           primary_key=True, nullable=False),
    Column('te_target', String(100),
           primary_key=True, nullable=False),
    Column('te_description', String(100),
           nullable=False),
    Column('cs_condicao_pesquisa', String(1),
           nullable=False),
    extend_existing=True
)
mapper(DescricaoColunaComputador, descricao_coluna_computador)
