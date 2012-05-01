from csv import DictReader
from os import listdir
from os.path import join

class SiteFolder(dict):
    __name__ = ''
    __parent__ = None

    def __init__(self, title):
        self.title = title
        self._imported_csv = None

    def bootstrap(self, import_dir):
        if self._imported_csv is not None:
            # Skip this if we have already loaded the data
            return

        # Setup
        self._imported_csv = dict(
            players={}, adults={}, tournaments={}
            )

        # Players
        players_fn = join(import_dir, 'players.csv')
        for player_row in DictReader(open(players_fn)):
            player = Player(player_row)
            self._imported_csv['players'][player.id] = player

class BasePerson:
    id = None
    last_name = None
    first_name = None
    email = None
    mobile_phone = None
    note = None

    def csv_load(self, csv_data):
        for k,v in csv_data.items():
            setattr(self, k, v)
        self.id = int(self.id)

class Player(BasePerson):
    guardian_ref = None
    uslax = None
    team_ref = None
    is_goalie = None
    grade = None
    school = None
    jersey_number = None
    dues_owed = None

    def __init__(self, csv_data):
        self.csv_load(csv_data)

class Adult(BasePerson):
    other_emails = []
    home_phone = None
    mobile_phone = None
    primary_coach_ref = None
    coach_ref = None
    manager_ref = None

    def __init__(self, csv_data):
        self.csv_load(csv_data)

class Registration:
    id = None
    player_ref = None
    event_ref = None
    status = 0
    paid = None
    note = None

    statuses = {
        0: "Unknown",
        1: "Not playing",
        2: "Maybe",
        3: "Balance due",
        4: "Paid"
    }

    def __init__(self, csv_data):
        self.csv_load(csv_data)


try:
    root
except NameError:
    root = SiteFolder('STORM Dashboard')

def root_factory(request):
    print('in root factory')
    return root