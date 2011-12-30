from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

engine.execute("select 1").scalar()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name

        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (
            self.name, self.fullname, self.password)

User.__table__
User.__mapper__

Base.metadata.create_all(engine)

ed_user = User('ed', 'Ed Jones', 'edspassword')
ed_user.name
ed_user.password
str(ed_user.id)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

ed_user = User('ed', 'Ed Jones', 'edspassword')
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)
print(ed_user is our_user)

session.add_all([
    User('wendy', 'Wendy Williams', 'foobar'),
    User('mary', 'Mary Contrary', 'xxg527'),
    User('fred', 'Fred Flinstone', 'blah')])

ed_user.password = 'f8s7ccs'
session.dirty
print(session.new)

session.commit()

print(ed_user.id)

ed_user.name = 'Edwardo'
fake_user = User('fakeuser', 'Invalid', '12345')
session.add(fake_user)
print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())
session.rollback()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)