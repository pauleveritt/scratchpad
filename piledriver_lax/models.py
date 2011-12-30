from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Guardian(Base):
    __tablename__ = 'guardians'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    sla_rid = Column(Integer)

    def __init__(self, first_name, last_name, sla_rid):
        self.first_name = first_name
        self.last_name = last_name
        self.sla_rid = sla_rid

    def __repr__(self):
        fmt = "Guardian(%r, %r)"
        return fmt % (self.first_name, self.last_name)


class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    sla_rid = Column(Integer)

    guardian_id = Column(Integer, ForeignKey('guardians.id'))

    guardian = relationship("Guardian", backref=backref('players', order_by=id))

    def __init__(self, first_name, last_name, sla_rid):
        self.first_name = first_name
        self.last_name = last_name
        self.sla_rid = sla_rid

    def __repr__(self):
        fmt = "Player(%r, %r)"
        return fmt % (self.first_name, self.last_name)

all_guardians = [
    Guardian('Paul', 'Everitt', 12),
    Guardian('Stacey', 'Smith', 34),
    Guardian('Jim', 'Harrel', 56),
    ]