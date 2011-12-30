import csv

def sla():
    fn = '/Users/paul/Downloads/SLA-Girls-2011.csv'
    guardians = {}
    players = {}

    records = csv.DictReader(open(fn))
    for record in records:
        person = dict(
            first_name=record['First Name'],
            last_name=record['Last Name'],
            sla_rid=record['RecordID'],
            addr1=record['Address 1'],
            addr2=record['Address 2'],
            city=record['City'],
            zip=record['Zip'],
            home_phone=record['Home Phone'],
            cell_phone=record['Cell Phone'],
            email=record['Email'],
            gender=record['Gender'],
            birthday=record['Birthday'],
            grade=record['Grade'],
            guardian1_id=record['Guardian1 ID'],
            guardian2_id=record['Guardian2 ID'],
            sla_team_name=record['Team Name'],
            players=[],
            #checksum = 999
            #create_date
            #modified_date
        )
        # Now add them to the correct dict
        type = record['Type']
        if type == 'Parent':
            guardians[person['sla_rid']] = person
        else:
            players[person['sla_rid']] = person

    # Now we store players on guardians
    for player in players.values():
        g1_id = player['guardian1_id']
        guardians[g1_id]['players'].append(player)

    return guardians


