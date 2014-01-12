from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class SoftwareEstacao():

    """
    Classe que define a tabela 'software_estacao'

    """

    __tablename__ = 'software_estacao'
    id_computador = Column(Integer, ForeignKey('computador.id_computador'))
    id_software = Column(Integer, ForeignKey('software.id_software'))
    id_aquisicao = Column(Integer)
    nr_patrimonio = Column(String(20), primary_key=True, nullable=False)
    dt_autorizacao = Column(DateTime)
    dt_expiracao_instalacao = Column(DateTime)
    id_aquisicao_particular = Column(Integer)
    dt_desinstalacao = Column(DateTime)
    te_observacao = Column(String(90))
    nr_patr_destino = Column(String(20))

    def __init__(self, id_computador, id_software, id_aquisicao,
                 nr_patrimonio, dt_autorizacao, dt_expiracao_instalacao,
                 id_aquisicao_particular, dt_desinstalacao, te_observacao,
                 nr_patr_destino):
        """
        Metodo que chama as colunas
        """
        self.id_computador = id_computador
        self.id_software = id_software
        self.id_aquisicao = id_aquisicao
        self.nr_patrimonio = nr_patrimonio
        self.dt_autorizacao = dt_autorizacao
        self.dt_expiracao_instalacao = dt_expiracao_instalacao
        self.id_aquisicao_particular = id_aquisicao_particular
        self.dt_desinstalacao = dt_desinstalacao
        self.te_observacao = te_observacao
        self.nr_patr_destino = nr_patr_destino

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<SoftwareEstacao('%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                                 %s')>" % (self.id_computador,
                                           self.id_software,
                                           self.id_aquisicao,
                                           self.nr_patrimonio,
                                           self.dt_autorizacao,
                                           self.dt_expiracao_instalacao,
                                           self.id_aquisicao_particular,
                                           self.dt_desinstalacao,
                                           self.te_observacao,
                                           self.nr_patr_destino
                                           )


class SoftwareEstacaoContextFactory(SQLAlchemyORMContext):
    entity = SoftwareEstacao

    def session_factory(self):
        return session

software_estacao = Table('software_estacao', Base.metadata,
                         Column('id_computador', Integer,
                                ForeignKey('computador.id_computador')),
                         Column('id_software', Integer,
                                ForeignKey('software.id_software')),
                         Column('id_aquisicao', Integer),
                         Column('nr_patrimonio', String(20),
                                primary_key=True, nullable=False),
                         Column('dt_autorizacao', Date),
                         Column('dt_expiracao_instalacao', Date),
                         Column('id_aquisicao_particular', Integer),
                         Column('dt_desinstalacao', Date),
                         Column('te_observacao', String(90)),
                         Column('nr_patr_destino', String(20)),
                         extend_existing=True
                         )

mapper(SoftwareEstacao, software_estacao)
