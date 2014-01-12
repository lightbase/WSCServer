from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class TipoSoftware():

    """
    Classe que define a tabela 'tipo_software'

    """
    __tablename__ = 'tipo_software'
    id_tipo_software = Column(Integer, primary_key=True, nullable=False)
    te_descricao_tipo_software = Column(String(30), nullable=False)

    def __init__(self, id_tipo_software, te_descricao_tipo_software):
        """
        Metodo que chama as colunas
        """
        self.id_tipo_software = id_tipo_software
        self.te_descricao_tipo_software = te_descricao_tipo_software

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<TipoSoftware('%s, %s')>" % (self.id_tipo_software,
                                             self.te_descricao_tipo_software
                                             )


class TipoSoftwareContextFactory(SQLAlchemyORMContext):
    entity = TipoSoftware

    def session_factory(self):
        return session

tipo_software = Table('tipo_software', Base.metadata,
                      Column('id_tipo_software', Integer, primary_key=True,
                             nullable=False),
                      Column('te_descricao_tipo_software', String(30),
                             nullable=False),
                      extend_existing=True
                      )

mapper(TipoSoftware, tipo_software)
