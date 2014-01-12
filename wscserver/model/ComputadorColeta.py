from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class ComputadorColeta():

    """
    Classe que define a tabela 'computador_coleta'

    """

    __tablename__ = 'computador_coleta'
    id_computador_coleta = Column(Integer, primary_key=True, nullable=False)
    id_computador = Column(Integer, ForeignKey('computador.id_computador'))
    id_class = Column(Integer)
    te_class_values = Column(String, nullable=False)

    def __init__(self, id_computador_coleta, id_computador, id_class,
                 te_class_values, dt_hr_inclusao):
        """
        Metodo que chama as colunas
        """
        self.id_computador_coleta = id_computador_coleta
        self.id_computador = id_computador
        self.id_class = id_class
        self.te_class_values = te_class_values

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<ComputadorColeta('%s, %s, %s, %s')>" %\
            (self.id_computador_coleta,
             self.id_computador,
             self.id_class,
             self.te_class_values
             )


class ComputadorColetaContextFactory(SQLAlchemyORMContext):
    entity = ComputadorColeta

    def session_factory(self):
        return session

computador_coleta = Table('computador_coleta', Base.metadata,
                          Column('id_computador_coleta', Integer,
                                 primary_key=True, nullable=False),
                          Column('id_computador', Integer,
                                 ForeignKey('computador.id_computador')),
                          Column('id_class', Integer),
                          Column('te_class_values', String, nullable=False),
                          extend_existing=True
                          )

mapper(ComputadorColeta, computador_coleta)
