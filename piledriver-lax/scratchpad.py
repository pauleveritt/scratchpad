from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from models import User
from models import all_users

def main():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    ed_user = User('ed', 'Ed Jones', 'edspassword')
    session.add(ed_user)
    session.add_all(all_users)
    session.commit()

    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)

if __name__ == '__main__':
    main()