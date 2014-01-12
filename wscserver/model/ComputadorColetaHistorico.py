from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class ComputadorColetaHistorico():

    """
    Classe que define a tabela 'computador_coleta_historico'

    """
    __tablename__ = 'computador_coleta_historico'
    id_computador_coleta_historico = Column(Integer, primary_key=True,
                                            nullable=False)
    id_computador_coleta = Column(
        Integer, ForeignKey('computador_coleta.id_computador_coleta'))
    id_computador = Column(Integer, ForeignKey('computador.id_computador'))
    id_class_property = Column(Integer)
    te_class_property_value = Column(String, nullable=False)
    dt_hr_inclusao = Column(DateTime(timezone=False))

    def __init__(self, id_computador_coleta_historico, id_computador_coleta,
                 id_computador, id_class_property, te_class_property_values,
                 dt_hr_inclusao):
        """
        Metodo que chama as colunas
        """
        self.id_computador_coleta_historico = id_computador_coleta_historico
        self.id_computador_coleta = id_computador_coleta
        self.id_computador = id_computador
        self.id_class_property = id_class_property
        self.te_class_property_value = te_class_property_value
        self.dt_hr_inclusao = dt_hr_inclusao

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<ComputadorColetaHistorico('%s, %s, %s, %s, %s, %s')>" %\
            (self.id_computador_coleta_historico,
             self.id_computador_coleta,
             self.id_computador,
             self.id_class_property,
             self.te_class_property_value,
             self.dt_hr_inclusao
             )


class ComputadorColetaHistoricoContextFactory(SQLAlchemyORMContext):
    entity = ComputadorColetaHistorico

    def session_factory(self):
        return session

computador_coleta_historico = Table(
    'computador_coleta_historico', Base.metadata,
    Column('id_computador_coleta_historico', Integer, primary_key=True,
           nullable=False),
    Column('id_computador_coleta', Integer, ForeignKey(
                                    'computador_coleta.id_computador_coleta')),
    Column('id_computador', Integer, ForeignKey('computador.id_computador')),
    Column('id_class_property', Integer),
    Column('te_class_property_value', String, nullable=False),
    Column('dt_hr_inclusao', DateTime(timezone=False)),
    extend_existing=True
)

mapper(ComputadorColetaHistorico, computador_coleta_historico)
