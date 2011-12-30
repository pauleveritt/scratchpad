from time import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from piledriver_lax.models import Base
from piledriver_lax.models import Guardian
from piledriver_lax.models import Player
from piledriver_lax.models import all_guardians

from piledriver_lax.importer import sla

def main():
    guardians = sla()

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

    for g in guardians.values():
        guardian = Guardian(g['first_name'], g['last_name'], g['sla_rid'])
        for p in g['players']:
            player = Player(p['first_name'], p['last_name'], p['sla_rid'])
            guardian.players.append(player)
        session.add(guardian)
    session.commit()

    for player in session.query(Player):
        print(player)

    print("Elapsed time:", time() - start)

if __name__ == '__main__':
    main()
