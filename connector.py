from __future__ import print_function
import os
from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from setting import Base


class Connector(with_metaclass(ABCMeta, object)):
    """Abstract class of db connector with sqlalchemy."""

    def __init__(self):
        self.initurl()
        self.initengine()
        self.initsession()

    def initurl(self):
        pass

    def initengine(self):
        self._engine = create_engine(self.url, echo=False)
        Base.metadata.create_all(bind=self._engine)

    @property
    def engine(self):
        return self._engine

    def initsession(self):
        self._session = scoped_session(sessionmaker(bind=self._engine))

    @property
    def session(self):
        return self._session

    def get_all(self, obj):
        return self.session().query(obj).all()

    def get_by_id(self, obj, id):
        return self.session().query(obj).filter(obj.id == id).one()

    def insert(self, data):
        self.session().add(data)
        self.session().commit()

    def update(self, data):
        self.insert(data)


class PostgreSQLConnector(Connector):
    def __init__(self, uri):
        self.url = uri
        super(PostgreSQLConnector, self).__init__()
