from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class Aplicativo():

    """
    Classe que define a tabela 'aplicativo'

    """

    __tablename__ = 'aplicativo'
    id_aplicativo = Column(Integer, primary_key=True, nullable=False)
    id_so = Column(Integer, ForeignKey('so.id_so'))
    nm_aplicativo = Column(String(100), nullable=False)
    cs_car_inst_w9x = Column(String(2))
    te_car_inst_w9x = Column(String(255))
    cs_car_ver_w9x = Column(String(2))
    te_car_ver_w9x = Column(String(255))
    cs_car_inst_wnt = Column(String(2))
    te_car_inst_wnt = Column(String(255))
    cs_car_ver_wnt = Column(String(2))
    te_car_ver_wnt = Column(String(255))
    cs_ide_licenca = Column(String(2))
    te_ide_licenca = Column(String(255))
    dt_atualizacao = Column(DateTime(timezone=False))
    te_arq_ver_eng_w9x = Column(String(100))
    te_arq_ver_pat_w9x = Column(String(100))
    te_arq_ver_eng_wnt = Column(String(100))
    te_arq_ver_pat_wnt = Column(String(100))
    te_dir_padrao_w9x = Column(String(100))
    te_dir_padrao_wnt = Column(String(100))
    te_descritivo = Column(String)
    in_disponibiliza_info = Column(String(1), nullable=False)
    in_disponibiliza_info_usuario_comum = Column(String(1), nullable=False)
    dt_registro = Column(DateTime(timezone=False))

    def __init__(self,):
        """
        Metodo que chama as colunas
        """
        self.id_aplicativo = id_aplicativo
        self.id_so = id_so
        self.nm_aplicativo = nm_aplicativo
        self.cs_car_inst_w9x = cs_car_inst_w9x
        self.te_car_inst_w9x = te_car_inst_w9x
        self.cs_car_ver_w9x = cs_car_ver_w9x
        self.te_car_ver_w9x = te_car_ver_w9x
        self.cs_car_inst_wnt = cs_car_inst_wnt
        self.te_car_inst_wnt = te_car_inst_wnt
        self.cs_car_ver_wnt = cs_car_ver_wnt
        self.te_car_ver_wnt = te_car_ver_wnt
        self.cs_ide_licenca = cs_ide_licenca
        self.te_ide_licenca = te_ide_licenca
        self.dt_atualizacao = dt_atualizacao
        self.te_arq_ver_eng_w9x = te_arq_ver_eng_w9x
        self.te_arq_ver_pat_w9x = te_arq_ver_pat_w9x
        self.te_arq_ver_eng_wnt = te_arq_ver_eng_wnt
        self.te_arq_ver_pat_wnt = te_arq_ver_pat_wnt
        self.te_dir_padrao_w9x = te_dir_padrao_w9x
        self.te_dir_padrao_wnt = te_dir_padrao_wnt
        self.te_descritivo = te_descritivo
        self.in_disponibiliza_info = in_disponibiliza_info
        self.in_disponibiliza_info_usuario_comum = in_disponibiliza_info_usuario_comum
        self.dt_registro = dt_registro

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<Aplicativo('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s')>"\
                % (self.id_aplicativo,
                   self.id_so,
                   self.nm_aplicativo,
                   self.cs_car_inst_w9x,
                   self.te_car_inst_w9x,
                   self.cs_car_ver_w9x,
                   self.te_car_ver_w9x,
                   self.cs_car_inst_wnt,
                   self.te_car_inst_wnt,
                   self.cs_car_ver_wnt,
                   self.te_car_ver_wnt,
                   self.cs_ide_licenca,
                   self.te_ide_licenca,
                   self.dt_atualizacao,
                   self.te_arq_ver_eng_w9x,
                   self.te_arq_ver_pat_w9x,
                   self.te_arq_ver_eng_wnt,
                   self.te_arq_ver_pat_wnt,
                   self.te_dir_padrao_w9x,
                   self.te_dir_padrao_wnt,
                   self.te_descritivo,
                   self.in_disponibiliza_info,
                   self.in_disponibiliza_info_usuario_comum,
                   self.dt_registro
                   )


class AplicativoContextFactory(SQLAlchemyORMContext):
    entity = Aplicativo

    def session_factory(self):
        return session

aplicativo = Table('aplicativo', Base.metadata,
                   Column('id_aplicativo', Integer, primary_key=True,
                          nullable=False),
                   Column('id_so', Integer, ForeignKey('so.id_so')),
                   Column('nm_aplicativo', String(100), nullable=False),
                   Column('cs_car_inst_w9x', String(2)),
                   Column('te_car_inst_w9x', String(255)),
                   Column('cs_car_ver_w9x', String(2)),
                   Column('te_car_ver_w9x', String(255)),
                   Column('cs_car_inst_wnt', String(2)),
                   Column('te_car_inst_wnt', String(255)),
                   Column('cs_car_ver_wnt', String(2)),
                   Column('te_car_ver_wnt', String(255)),
                   Column('cs_ide_licenca', String(2)),
                   Column('te_ide_licenca', String(255)),
                   Column('dt_atualizacao', DateTime(timezone=False)),
                   Column('te_arq_ver_eng_w9x', String(100)),
                   Column('te_arq_ver_pat_w9x', String(100)),
                   Column('te_arq_ver_eng_wnt', String(100)),
                   Column('te_arq_ver_pat_wnt', String(100)),
                   Column('te_dir_padrao_w9x', String(100)),
                   Column('te_dir_padrao_wnt', String(100)),
                   Column('te_descritivo', String),
                   Column('in_disponibiliza_info', String(1), nullable=False),
                   Column('in_disponibiliza_info_usuario_comum', String(1),
                          nullable=False),
                   Column('dt_registro', DateTime(timezone=False)),
                   extend_existing=True
                   )

mapper(Aplicativo, aplicativo)
