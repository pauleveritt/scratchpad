from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models import User

engine = create_engine('sqlite:///:memory:')



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

ed_user = User('ed', 'Ed Jones', 'edspassword')
session.add(ed_user)

session.add_all([
    User('wendy', 'Wendy Williams', 'foobar'),
    User('mary', 'Mary Contrary', 'xxg527'),
    User('fred', 'Fred Flinstone', 'blah')])


session.commit()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)