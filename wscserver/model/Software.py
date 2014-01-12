from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class Software():

    """
    Classe que define a tabela 'software'

    """

    __tablename__ = 'software'
    id_software = Column(Integer, primary_key=True, nullable=False)
    id_tipo_software = Column(Integer)
    nm_software = Column(String(150), nullable=False)
    te_descricao_software = Column(String(255))
    qt_licenca = Column(Integer)
    nr_midia = Column(String(10))
    te_local_midia = Column(String(30))
    te_obs = Column(String(200))

    def __init__(self, id_software, id_tipo_software, nm_software,
                 te_descricao_software, qt_licenca, nr_midia, te_local_midia,
                 te_obs):
        """
        Metodo que chama as colunas
        """
        self.id_software = id_software
        self.id_tipo_software = id_tipo_software
        self.nm_software = nm_software
        self.te_descricao_software = te_descricao_software
        self.qt_licenca = qt_licenca
        self.nr_midia = nr_midia
        self.te_local_midia = te_local_midia
        self.te_obs = te_obs

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<Software('%s, %s, %s, %s,\
                          %s, %s %s, %s,')>" % (self.id_software,
                                                self.id_tipo_software,
                                                self.nm_software,
                                                self.te_descricao_software,
                                                self.qt_licenca,
                                                self.nr_midia,
                                                self.te_local_midia,
                                                self.te_obs
                                                )


class SoftwareContextFactory(SQLAlchemyORMContext):
    entity = Software

    def session_factory(self):
        return session

software = Table('software', Base.metadata,
                 Column('id_software', Integer, primary_key=True,
                        nullable=False),
                 Column('id_tipo_software', Integer),
                 Column('nm_software', String(150), nullable=False),
                 Column('te_descricao_software', String(255)),
                 Column('qt_licenca', Integer),
                 Column('nr_midia', String(10)),
                 Column('te_local_midia', String(30)),
                 Column('te_obs', String(200)),
                 extend_existing=True
                 )

mapper(Software, software)
