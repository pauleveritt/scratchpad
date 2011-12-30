from time import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from piledriver_lax.models import Base
from piledriver_lax.models import Guardian
from piledriver_lax.models import Player
from piledriver_lax.models import all_guardians

def main():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    start = time()

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all(all_guardians)
    session.commit()

    kirsten = Guardian('Kirsten', 'Baylor', 99)
    kirsten.players = [
        Player('Kennedy', 'Baylor', 87),
        Player('Kayla', 'Baylor', 52),
        ]
    session.add(kirsten)
    session.commit()

    print(kirsten.players)

    print("Elapsed time:", time() - start)

if __name__ == '__main__':
    main()
