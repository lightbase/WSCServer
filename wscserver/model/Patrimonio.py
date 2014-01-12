from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class Patrimonio():

    """
    Classe que define a tabela 'patrimonio'

    """

    __tablename__ = 'patrimonio'
    id_patrimonio = Column(Integer, primary_key=True, nullable=False)
    id_usuario = Column(Integer)
    id_unid_organizacional_nivel1a = Column(Integer)
    id_computador = Column(Integer, ForeignKey('computador.id_computador'))
    id_unid_organizacional_nivel2 = Column(Integer)
    dt_hr_alteracao = Column(DateTime(timezone=False))
    te_localizacao_complementar = Column(String(100))
    te_info_patrimonio1 = Column(String(20))
    te_info_patrimonio2 = Column(String(20))
    te_info_patrimonio3 = Column(String(20))
    te_info_patrimonio4 = Column(String(20))
    te_info_patrimonio5 = Column(String(20))
    te_info_patrimonio6 = Column(String(20))
    id_unid_organizacional_nivel1 = Column(Integer, nullable=False)

    def __init__(self, id_patrimonio, id_usuario,
                 id_unid_organizacional_nivel1a, id_computador,
                 id_unid_organizacional_nivel2, dt_hr_alteracao,
                 te_localizacao_complementar, te_info_patrimonio1,
                 te_info_patrimonio2, te_info_patrimonio3,
                 te_info_patrimonio4, te_info_patrimonio5,
                 te_info_patrimonio6, id_unid_organizacional_nivel1):
        """
        Metodo que chama as colunas
        """
        self.id_patrimonio = id_patrimonio
        self.id_usuario = id_usuario
        self.id_unid_organizacional_nivel1a = id_unid_organizacional_nivel1a
        self.id_computador = id_computador
        self.id_unid_organizacional_nivel2 = id_unid_organizacional_nivel2
        self.dt_hr_alteracao = dt_hr_alteracao
        self.te_localizacao_complementar = te_localizacao_complementar
        self.te_info_patrimonio1 = te_info_patrimonio1
        self.te_info_patrimonio2 = te_info_patrimonio2
        self.te_info_patrimonio3 = te_info_patrimonio3
        self.te_info_patrimonio4 = te_info_patrimonio4
        self.te_info_patrimonio5 = te_info_patrimonio5
        self.te_info_patrimonio6 = te_info_patrimonio6
        self.id_unid_organizacional_nivel1 = id_unid_organizacional_nivel1

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<Patrimonio('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                            %s, %s')>" % (self.id_patrimonio,
                                          self.id_usuario,
                                          self.id_unid_organizacional_nivel1a,
                                          self.id_computador,
                                          self.id_unid_organizacional_nivel2,
                                          self.dt_hr_alteracao,
                                          self.te_localizacao_complementar,
                                          self.te_info_patrimonio1,
                                          self.te_info_patrimonio2,
                                          self.te_info_patrimonio3,
                                          self.te_info_patrimonio4,
                                          self.te_info_patrimonio5,
                                          self.te_info_patrimonio6,
                                          self.id_unid_organizacional_nivel1
                                          )


class PatrimonioContextFactory(SQLAlchemyORMContext):
    entity = Patrimonio

    def session_factory(self):
        return session

patrimonio = Table('patrimonio', Base.metadata,
                   Column('id_patrimonio', Integer, primary_key=True,
                          nullable=False),
                   Column('id_usuario', Integer),
                   Column('id_unid_organizacional_nivel1a', Integer),
                   Column('id_computador', Integer,
                          ForeignKey('computador.id_computador')),
                   Column('id_unid_organizacional_nivel2', Integer),
                   Column('dt_hr_alteracao', DateTime(timezone=False)),
                   Column('te_localizacao_complementar', String(100)),
                   Column('te_info_patrimonio1', String(20)),
                   Column('te_info_patrimonio2', String(20)),
                   Column('te_info_patrimonio3', String(20)),
                   Column('te_info_patrimonio4', String(20)),
                   Column('te_info_patrimonio5', String(20)),
                   Column('te_info_patrimonio6', String(20)),
                   Column('id_unid_organizacional_nivel1',
                          Integer, nullable=False),
                   extend_existing=True
                   )

mapper(Patrimonio, patrimonio)
