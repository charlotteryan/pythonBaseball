import re
import sys, os

#output all players' batting average across the season
def find_player(name):
	for player in players:
		if player['name'] == name:
			return player
def update_player(name, hits, chances):
    player = find_player(name)
    #if player doesn't exist, add new player
    if player is None:
        new_player = {'name':name, 'hits':hits, 'chances':chances}
        players.append(new_player)
    #player exists, update stats
    else: 
        player['hits'] += hits
        player['chances'] += chances 
	
def format_avg(hits, chances):
    #can't divide by 0 --> theoretical error
    if chances != 0:
        return '{:.3f}'.format(hits/chances)
    else:
        return '{:.3f}'.format(0)

#file name is stored in argv[1], no path --> usage message
#command line arguments from 330 Wiki
if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

with open(filename) as f:
    #list
    players = []
    #set
    set = {}
    line = f.readline()
    while line:
        l = re.compile(r"(?P<name>[\w\s]+)\sbatted\s(?P<chances>\d)[\w\s]+with\s(?P<hits>\d)")
        match = re.match(l,line)
        if match:
            name = match.group('name')
            hits = int(match.group('hits'))
            chances = int(match.group('chances'))
            update_player(name,hits,chances)
        #update line, new line being read
        line = f.readline()

    for person in players:
        avg = format_avg(person['hits'], person['chances'])
        #if set is empty, fill
        if set == {}:
            set = {person['name']:avg}
        #update set
        else:
            set[person['name']] = avg

    #from 330 wiki
    for name,avg in sorted(set.items(), key=lambda v: v[1], reverse=True):
        print(name, ':', avg)
  
		



		

