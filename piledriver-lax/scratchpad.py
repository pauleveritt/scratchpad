from time import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from models import Address
from models import User
from models import all_users

def main():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    start = time()

    Session = sessionmaker(bind=engine)
    session = Session()

    ed_user = User('ed', 'Ed Jones', 'edspassword')
    session.add(ed_user)
    session.add_all(all_users)
    session.commit()

    jack = User('jack', 'Jack Bean', 'gjffdd')
    jack.addresses = [
        Address(email_address='jack@google.com'),
        Address(email_address='j25@yahoo.com')]
    session.add(jack)
    session.commit()

    print("Elapsed time:", time() - start)

if __name__ == '__main__':
    main()
