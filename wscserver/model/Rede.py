from pyramid_restler.model import SQLAlchemyORMContext

from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from wscserver.model import Base, session
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


class Rede():

    """
    Classe que define a tabela 'rede'

    """

    __tablename__ = 'rede'
    id_rede = Column(Integer, primary_key=True, nullable=False)
    id_local = Column(Integer)
    id_servidor_autenticacao = Column(Integer)
    te_ip_rede = Column(String(15), nullable=False)
    nm_rede = Column(String(100))
    te_observacao = Column(String(100))
    nm_pessoa_contato1 = Column(String(50))
    nm_pessoa_contato2 = Column(String(50))
    nu_telefone1 = Column(String(11))
    te_email_contato2 = Column(String(50))
    nu_telefone2 = Column(String(11))
    te_email_contato1 = Column(String(50))
    te_serv_cacic = Column(String(60), nullable=False)
    te_serv_updates = Column(String(60), nullable=False)
    te_path_serv_updates = Column(String(255))
    nm_usuario_login_serv_updates = Column(String(20))
    te_senha_login_serv_updates = Column(String(20))
    nu_porta_serv_updates = Column(String(4))
    te_mascara_rede = Column(String(15))
    dt_verifica_updates = Column(DateTime)
    nm_usuario_login_serv_updates_gerente = Column(String(20))
    te_senha_login_serv_updates_gerente = Column(String(20))
    nu_limite_ftp = Column(Integer, nullable=False)
    cs_permitir_desativar_srcacic = Column(String(1), nullable=False)
    te_debugging = Column(String)
    dt_debug = Column(String(8))

    def __init__(self, id_rede, id_local, id_servidor_autenticacao,
                 te_ip_rede, nm_rede, te_observacao, nm_pessoa_contato1,
                 nm_pessoa_contato2, nu_telefone1, te_email_contato2,
                 nu_telefone2, te_email_contato1, te_serv_cacic,
                 te_serv_updates, te_path_serv_updates,
                 nm_usuario_login_serv_updates, te_senha_login_serv_updates,
                 nu_porta_serv_updates, te_mascara_rede, dt_verifica_updates,
                 nm_usuario_login_serv_updates_gerente,
                 te_senha_login_serv_updates_gerente,
                 nu_limite_ftp, cs_permitir_desativar_srcacic, te_debugging,
                 dt_debug):
        """
        Metodo que chama as colunas
        """
        self.id_rede = id_rede
        self.id_local = id_local
        self.id_servidor_autenticacao = id_servidor_autenticacao
        self.te_ip_rede = te_ip_rede
        self.nm_rede = nm_rede
        self.te_observacao = te_observacao
        self.nm_pessoa_contato1 = nm_pessoa_contato1
        self.nm_pessoa_contato2 = nm_pessoa_contato2
        self.nu_telefone1 = nu_telefone1
        self.te_email_contato2 = te_email_contato2
        self.nu_telefone2 = nu_telefone2
        self.te_email_contato1 = te_email_contato1
        self.te_serv_cacic = te_serv_cacic
        self.te_serv_updates = te_serv_updates
        self.te_path_serv_updates = te_path_serv_updates
        self.nm_usuario_login_serv_updates = nm_usuario_login_serv_updates
        self.te_senha_login_serv_updates = te_senha_login_serv_updates
        self.nu_porta_serv_updates = nu_porta_serv_updates
        self.te_mascara_rede = te_mascara_rede
        self.dt_verifica_updates = dt_verifica_updates
        self.nm_usuario_login_serv_updates_gerente = nm_usuario_login_serv_updates_gerente
        self.te_senha_login_serv_updates_gerente = te_senha_login_serv_updates_gerente
        self.nu_limite_ftp = nu_limite_ftp
        self.cs_permitir_desativar_srcacic = cs_permitir_desativar_srcacic
        self.te_debugging = te_debugging
        self.dt_debug = dt_debug

    def __repr__(self):
        """
        Metodo que passa a lista de parametros da classe
        """
        return "<Rede('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)>" %\
            (self.id_rede,
             self.id_local,
             self.id_servidor_autenticacao,
             self.te_ip_rede,
             self.nm_rede,
             self.te_observacao,
             self.nm_pessoa_contato1,
             self.nm_pessoa_contato2,
             self.nu_telefone1,
             self.te_email_contato2,
             self.nu_telefone2,
             self.te_email_contato1,
             self.te_serv_cacic,
             self.te_serv_updates,
             self.te_path_serv_updates,
             self.nm_usuario_login_serv_updates,
             self.te_senha_login_serv_updates,
             self.nu_porta_serv_updates,
             self.te_mascara_rede,
             self.dt_verifica_updates,
             self.nm_usuario_login_serv_updates_gerente,
             self.te_senha_login_serv_updates_gerente,
             self.nu_limite_ftp,
             self.cs_permitir_desativar_srcacic,
             self.te_debugging,
             self.dt_debug
             )


class RedeContextFactory(SQLAlchemyORMContext):
    entity = Rede

    def session_factory(self):
        return session

rede = Table('rede', Base.metadata,
             Column('id_rede', Integer, primary_key=True, nullable=False),
             Column('id_local', Integer),
             Column('id_servidor_autenticacao', Integer),
             Column('te_ip_rede', String(15), nullable=False),
             Column('nm_rede', String(100)),
             Column('te_observacao', String(100)),
             Column('nm_pessoa_contato1', String(50)),
             Column('nm_pessoa_contato2', String(50)),
             Column('te_email_contato2', String(50)),
             Column('nu_telefone2', String(11)),
             Column('te_email_contato1', String(50)),
             Column('te_serv_cacic', String(60), nullable=False),
             Column('te_serv_updates', String(60), nullable=False),
             Column('te_path_serv_updates', String(255)),
             Column('nm_usuario_login_serv_updates', String(20)),
             Column('te_senha_login_serv_updates', String(20)),
             Column('nu_porta_serv_updates', String(4)),
             Column('te_mascara_rede', String(15)),
             Column('dt_verifica_updates', DateTime),
             Column('nm_usuario_login_serv_updates_gerente', String(20)),
             Column('te_senha_login_serv_updates_gerente', String(20)),
             Column('nu_limite_ftp', Integer, nullable=False),
             Column('cs_permitir_desativar_srcacic', String(1),
                    nullable=False),
             Column('te_debugging', String),
             Column('dt_debug', String(8)),
             extend_existing=True
             )

mapper(Rede, rede)
