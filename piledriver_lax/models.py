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
    addr1 = Column(String)
    addr2 = Column(String)
    city = Column(String)
    zip = Column(String)
    home_phone = Column(String)
    cell_phone = Column(String)
    email = Column(String)

    def __init__(self, first_name, last_name, sla_rid):
        self.first_name = first_name
        self.last_name = last_name
        self.sla_rid = sla_rid

    def __repr__(self):
        fmt = "Guardian(%r, %r, %r players)"
        c = len(self.players)
        return fmt % (self.first_name, self.last_name, c)

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    sla_rid = Column(Integer)
    cell_phone = Column(String)
    email = Column(String)
    birthday = Column(String)
    grade = Column(Integer)
    sla_team_name = Column(String)

    guardian_id = Column(Integer, ForeignKey('guardians.id'))

    guardian = relationship("Guardian", backref=backref('players', order_by=id))

    def __init__(self, first_name, last_name, sla_rid):
        self.first_name = first_name
        self.last_name = last_name
        self.sla_rid = sla_rid

    def __repr__(self):
        fmt = "Player(%r, %r, %r)"
        guardian_first = self.guardian.first_name
        return fmt % (self.first_name, self.last_name, guardian_first)

