from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class So():

    """
    Classe que define a tabela 'so'

    """
    __tablename__ = 'so'
    id_so = Column(Integer, primary_key=True, nullable=False)
    te_desc_so = Column(String(255))
    sg_so = Column(String(20))
    te_so = Column(String(50), nullable=False)
    in_mswindows = Column(String(1), nullable=False)

    def __init__(self, id_so, te_desc_so, sg_so, te_so, in_mswindows):
        """
        Metodo que chama as colunas
        """
        self.id_so = id_so
        self.te_desc_so = te_desc_so
        self.sg_so = sg_so
        self.te_so = te_so
        self.in_mswindows = in_mswindows

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<So('%s, %s, %s, %s, %s')>" % (self.id_so, self.te_desc_so,
                                               self.sg_so, self.te_so,
                                               self.in_mswindows
                                               )


class SoContextFactory(SQLAlchemyORMContext):
    entity = So

    def session_factory(self):
        return session

so = Table('so', Base.metadata,
           Column('id_so', Integer, primary_key=True, nullable=False),
           Column('te_desc_so', String(255)),
           Column('sg_so', String(20)),
           Column('te_so', String(50), nullable=False),
           Column('in_mswindows', String(1), nullable=False),
           extend_existing=True
           )

mapper(So, so)
