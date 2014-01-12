from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class Acao():

    """
    Classe que define a tabela 'acao'

    """

    __tablename__ = 'acao'
    id_acao = Column(String(30), primary_key=True, nullable=False)
    te_descricao_breve = Column(String(100))
    te_descricao = Column(String)
    te_nome_curto_modulo = Column(String(20))
    dt_hr_alteracao = Column(DateTime(timezone=False))
    cs_opcional = Column(String(1), nullable=False)

    def __init__(self, id_acao, te_descricao_breve, te_descricao,
                 te_nome_curto_modulo, dt_hr_alteracao, cs_opcional):
        """
        Metodo que chama as colunas
        """
        self.id_acao = id_acao
        self.te_descricao_breve = te_descricao_breve
        self.te_descricao = te_descricao
        self.te_nome_curto_modulo = te_nome_curto_modulo
        self.dt_hr_alteracao = dt_hr_alteracao
        self.cs_opcional = cs_opcional

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<Acao('%s, %s, %s, %s, %s, %s')>" % (self.id_acao,
                                                     self.te_descricao_breve,
                                                     self.te_descricao,
                                                     self.te_nome_curto_modulo,
                                                     self.dt_hr_alteracao,
                                                     self.cs_opcional
                                                     )


class AcaoContextFactory(SQLAlchemyORMContext):
    entity = Acao

    def session_factory(self):
        return session

acao = Table('acao', Base.metadata,
             Column('id_acao', String(30), primary_key=True, nullable=False),
             Column('te_descricao_breve', String(100)),
             Column('te_descricao', String),
             Column('te_nome_curto_modulo', String(20)),
             Column('dt_hr_alteracao', DateTime(timezone=False)),
             Column('cs_opcional', String(1), nullable=False),
             extend_existing=True
             )

mapper(Acao, acao)
