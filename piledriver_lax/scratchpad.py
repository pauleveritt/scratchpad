from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from piledriver_lax.models import Base
from piledriver_lax.models import Guardian
from piledriver_lax.models import Player

from piledriver_lax.importer import sla

def load_sla(session):
    guardians = sla()
    for g in guardians.values():
        guardian = Guardian(g['first_name'], g['last_name'], g['sla_rid'])
        guardian.addr1 = g['addr1']
        guardian.addr2 = g['addr2']
        guardian.city = g['city']
        guardian.zip = g['zip']
        guardian.home_phone = g['home_phone']
        guardian.cell_phone = g['cell_phone']

        for p in g['players']:
            player = Player(p['first_name'], p['last_name'], p['sla_rid'])
            player.cell_phone = p['cell_phone']
            player.email = p['email']
            player.birthday = p['birthday']
            player.grade = p['grade']
            player.sla_team_name = p['sla_team_name']
            guardian.players.append(player)
        session.add(guardian)

    for player in session.query(Player):
        print(player)

    g_sla_rids = [a.sla_rid for a in session.query(Guardian)]
    p_sla_rids = [a.sla_rid for a in session.query(Player)]
    print(len(g_sla_rids) + len(p_sla_rids))

def get_session():

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    load_sla(session)
    session.commit()

    return session

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)



if __name__ == '__main__':
    session = get_session()
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()