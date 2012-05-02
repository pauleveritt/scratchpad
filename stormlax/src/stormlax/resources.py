from csv import DictReader
from os.path import join

class SiteFolder(dict):
    __name__ = ''
    __parent__ = None

    def __init__(self, name, parent, title):
        self.__name__ = name
        self.__parent__ = parent
        self.title = title
        self._imported_csv = None

    def bootstrap(self, var_dir):

        # Make some rosters
        self['blue'] = Roster('blue', root, 'Blue')
        self['orange'] = Roster('orange', root, 'Orange')
        self['white'] = Roster('white', root, 'White')
        self['black'] = Roster('black', root, 'Black')
        self['silver'] = Roster('silver', root, 'Silver')

        # Load some CSV data
        if self._imported_csv is not None:
            # Skip this if we have already loaded the data
            return

        # Setup
        self._imported_csv = dict(
            players={}, adults={}, registrations={}
            )

        # Players
        players_fn = join(var_dir, 'players.csv')
        for player_row in DictReader(open(players_fn)):
            player = Player(player_row)
            self._imported_csv['players'][player.id] = player


        # Adults
        adults_fn = join(var_dir, 'adults.csv')
        for adult_row in DictReader(open(adults_fn)):
            adult = Adult(adult_row)
            self._imported_csv['adults'][adult.id] = adult

        # Registrations
        registrations_fn = join(var_dir, 'registrations.csv')
        for registration_row in DictReader(open(registrations_fn)):
            registration = Registration(registration_row)
            self._imported_csv['registrations'][registration.id] = registration

    @property
    def rosters(self):
        return [
            dict(title='Blue', id='blue'),
            dict(title='Orange', id='orange'),
            dict(title='White', id='white'),
            dict(title='Black', id='black'),
            dict(title='Silver', id='silver'),
        ]

class BaseResource:
    def csv_load(self, csv_data):
        for k,v in csv_data.items():
            setattr(self, k, v)
        self.id = int(self.id)

class BasePerson(BaseResource):
    id = None
    last_name = None
    first_name = None
    email = None
    mobile_phone = None
    note = None


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
    address_1 = None
    address_2 = None
    city = None
    state = None
    zip = None
    other_emails = []
    home_phone = None
    mobile_phone = None
    primary_coach_ref = None
    coach_ref = None
    manager_ref = None

    def __init__(self, csv_data):
        self.csv_load(csv_data)

class Registration(BaseResource):
    id = None
    player_ref = None
    full_name = None
    event_ref = None
    status = 0
    balance = None
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

class Roster:
    __name__ = ''
    __parent__ = None

    id = None
    title = None

    def __init__(self, name, parent, title):
        self.__name__ = name
        self.__parent__ = parent
        self.id = name
        self.title = title

try:
    root
except NameError:
    root = SiteFolder('', None, 'STORM Dashboard')

def root_factory(request):
    return root