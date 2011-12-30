from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (
            self.name, self.fullname, self.password)

more_users = [
    User(
        name='wendy', fullname='Wendy Williams', password='foobar'),
    User(
        name='mary', fullname='Mary Contrary', password='xxg527'),
    User(
        name='fred', fullname='Fred Flinstone', password='blah'),
    ]