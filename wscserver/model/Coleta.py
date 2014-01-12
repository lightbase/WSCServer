from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property, mapper, join
from sqlalchemy.schema import ForeignKey, Column, Table
from sqlalchemy.types import *

from wscserver.model import Base, session


computador_coleta_historico = Table(
    'computador_coleta_historico', Base.metadata,
    Column('id_computador_coleta_historico',
           Integer, primary_key=True, nullable=False),
    Column('id_computador_coleta', Integer,
           ForeignKey('computador_coleta.id_computador_coleta')),
    Column('dt_hr_inclusao', DateTime(timezone=False), nullable=False)
)

computador_coleta = Table('computador_coleta', Base.metadata,
                          Column('id_computador_coleta', Integer,
                                 primary_key=True, nullable=False),
                          Column('id_computador', Integer),
                          Column('id_class_property', Integer,
                                 ForeignKey(
                                     'class_property.id_class_property')),
                          Column('te_class_property_value',
                                 String, nullable=False),
                          )

class_property = Table('class_property', Base.metadata,
                       Column('id_class_property', Integer, nullable=False),
                       Column('id_class', Integer,
                              ForeignKey('classe.id_class')),
                       Column('nm_property_name', String, nullable=False),
                       )

classe = Table('classe', Base.metadata,
               Column('id_class', Integer, primary_key=True, nullable=False),
               Column('nm_class_name', String, nullable=False),
               )


classe_and_class_property = join(classe, class_property)
pc_coleta_and_classe_and_class_property = join(
    computador_coleta, classe_and_class_property)
coleta = join(computador_coleta_historico,
              pc_coleta_and_classe_and_class_property)


class ClasseAndClassProperty(Base):

    """Classe de join entre 'classe' e 'class_property'"""
    __table__ = classe_and_class_property
    id_class = column_property(classe.c.id_class, class_property.c.id_class)


class PcColetaAndClasseAndClassProperty(Base):

    """
    Classe de join entre 'computador_coleta' e
    'classe_and_class_property'
    """
    __table__ = pc_coleta_and_classe_and_class_property
    id_class = column_property(classe.c.id_class, class_property.c.id_class)
    id_computador_coleta = column_property(
        computador_coleta.c.id_computador_coleta,
        computador_coleta_historico.c.id_computador_coleta)
    id_class_property = column_property(class_property.c.id_class_property,
                                        computador_coleta.c.id_class_property)


class Coleta(Base):

    """Classe de join entre as quatro tabelas"""
    __table__ = coleta
    id_class = column_property(classe.c.id_class, class_property.c.id_class)
    id_class_property = column_property(class_property.c.id_class_property,
                                        computador_coleta.c.id_class_property)
    id_computador_coleta = column_property(
        computador_coleta.c.id_computador_coleta,
        computador_coleta_historico.c.id_computador_coleta)


class ColetaContextFactory(SQLAlchemyORMContext):
    entity = Coleta

    def session_factory(self):
        return session

# mapper(Coleta, coleta)
