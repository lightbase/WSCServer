from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session


class Computador():

    """
    Classe que define a tabela 'computador'
    
    """
    __tablename__ = 'computador'
    id_computador = Column(Integer, primary_key=True, nullable=False)
    id_usuario_exclusao = Column(Integer)
    id_so = Column(Integer, ForeignKey('so.id_so'))
    id_rede = Column(Integer, ForeignKey('rede.id_rede'))
    nm_computador = Column(String(50))
    te_node_address = Column(String(17), nullable=False)
    te_ip_computador = Column(String(15))
    dt_hr_inclusao = Column(DateTime(timezone=False))
    dt_hr_exclusao = Column(DateTime(timezone=False))
    dt_hr_ult_acesso = Column(DateTime(timezone=False))
    te_versao_cacic = Column(String(15))
    te_versao_gercols = Column(String(15))
    te_palavra_chave = Column(String(30), nullable=False)
    dt_hr_coleta_forcada_estacao = Column(DateTime(timezone=False))
    te_nomes_curtos_modulos = Column(String(255))
    id_conta = Column(Integer)
    te_debugging = Column(String)
    te_ultimo_login = Column(String(100))
    dt_debug = Column(String(8))

    def __init__(self, id_computador, id_usuario_exclusao, id_so, id_rede,
                 nm_computador, te_node_address, te_ip_computador,
                 dt_hr_inclusao, dt_hr_exclusao, dt_hr_ultimo_acesso,
                 te_versao_cacic, te_versao_gercols, te_palavra_chave,
                 dt_hr_coleta_forcada_estacao, te_nomes_curtos_modulos,
                 id_conta, te_debugging, te_ultimo_login, dt_debug):
        """
        Metodo que chama as colunas
        """
        self.id_computador = id_computador
        self.id_usuario_exclusao = id_usuario_exclusao
        self.id_so = id_so
        self.id_rede = id_rede
        self.nm_computador = nm_computador
        self.te_node_address = te_node_address
        self.te_ip_computador = te_ip_computador
        self.dt_hr_inclusao = dt_hr_inclusao
        self.dt_hr_exclusao = dt_hr_exclusao
        self.dt_hr_ult_acesso = dt_hr_ult_acesso
        self.te_versao_cacic = te_versao_cacic
        self.te_versao_gercols = te_versao_gercols
        self.te_palavra_chave = te_palavra_chave
        self.dt_hr_coleta_forcada_estacao = dt_hr_coleta_forcada_estacao
        self.te_nomes_curtos_modulos = te_nomes_curtos_modulos
        self.id_conta = id_conta
        self.te_debugging = te_debugging
        self.te_ultimo_login = te_ultimo_login
        self.dt_debug = dt_debug

    def __repr__(self, id_computador, id_usuario_exclusao, id_so, id_rede,
                 nm_computador, te_node_address, te_ip_computador,
                 dt_hr_inclusao, dt_hr_exclusao, dt_hr_ult_acesso,
                 te_versao_cacic, te_versao_gercols, te_palavra_chave,
                 dt_hr_coleta_forcada_estacao, te_nomes_curtos_modulos,
                 id_conta, te_debugging, te_ultimo_login, dt_debug):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<Computador('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                            %s, %s, %s, %s, %s, %s, %s')>" %\
            (self.id_computador,
             self.id_usuario_exclusao,
             self.id_so,
             self.id_rede,
             self.nm_computador,
             self.te_node_address,
             self.te_ip_computador,
             self.dt_hr_inclusao,
             self.dt_hr_exclusao,
             self.dt_hr_ult_acesso,
             self.te_versao_cacic,
             self.te_versao_gercols,
             self.te_palavra_chave,
             self.dt_hr_coleta_forcada_estacao,
             self.te_nomes_curtos_modulos,
             self.id_conta,
             self.te_debugging,
             self.te_ultimo_login,
             self.dt_debug
             )


class ComputadorContextFactory(SQLAlchemyORMContext):
    entity = Computador

    def session_factory(self):
        return session

computador = Table('computador', Base.metadata,
                   Column('id_computador', Integer, primary_key=True,
                          nullable=False),
                   Column('id_usuario_exclusao', Integer),
                   Column('id_so', Integer, ForeignKey('so.id_so')),
                   Column('id_rede', Integer, ForeignKey('rede.id_rede')),
                   Column('nm_computador', String(50)),
                   Column('te_node_address', String(17), nullable=False),
                   Column('te_ip_computador', String(15)),
                   Column('dt_hr_inclusao', DateTime(timezone=False)),
                   Column('dt_hr_exclusao', DateTime(timezone=False)),
                   Column('dt_hr_ult_acesso', DateTime(timezone=False)),
                   Column('te_versao_cacic', String(15)),
                   Column('te_versao_gercols', String(15)),
                   Column('te_palavra_chave', String(30), nullable=False),
                   Column('dt_hr_coleta_forcada_estacao',
                          DateTime(timezone=False)),
                   Column('te_nomes_curtos_modulos', String(255)),
                   Column('id_conta', Integer),
                   Column('te_debugging', String),
                   Column('te_ultimo_login', String(100)),
                   Column('dt_debug', String(8)),
                   extend_existing=True
                   )
mapper(Computador, computador)
