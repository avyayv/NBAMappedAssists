from . import constants
import requests
import json
from os import path

def get_all_players_dict():
    player_to_id_dict = {}
    players_json = requests.get(constants.all_players_url, headers=constants.headers).json()
    for player in players_json['resultSets'][0]['rowSet']:
        player_to_id_dict[player[2]] = player[0]
    with open('all_ids.json', 'w') as fp:
        json.dump(player_to_id_dict, fp)

def get_stats_for_season(url, filename, season):
    id_to_stats_dict = {}
    stats_json = requests.get(url % season, headers=constants.headers).json()
    headers = stats_json['resultSets'][0]['headers']
    for player in stats_json['resultSets'][0]['rowSet']:
        id_to_stats_dict[player[0]] = dict(zip(headers[1:], player[1:]))
    with open(season+filename, 'w') as fp:
        json.dump(id_to_stats_dict, fp)
        
def get_bio_stats_for_season(season):
    get_stats_for_season(constants.bio_stats_url, "bio_stats.json", season)

def get_basic_stats_for_season(season):
    get_stats_for_season(constants.summary_stats_url, "all_stats.json", season)

def get_name_from_id(player_id):
    if path.exists("all_ids.json") == False:
       get_all_players_dict()
    
    player_to_id = json.loads(open('all_ids.json').read())
    id_to_player = {value:key for key, value in player_to_id.items()}
    if player_id in id_to_player: 
        return id_to_player[player_id]
    return player_id

def get_id_from_name(name):
    if path.exists("all_ids.json") == False:
       get_all_players_dict()
    
    player_to_id = json.loads(open('all_ids.json').read())
    if name in player_to_id: 
        return player_to_id[name]
    
    return None

def get_stats_by_player(season, filename, name=None, player_id=None):
    if path.exists("all_ids.json") == False:
       get_all_players_dict()
    if path.exists(season+filename) == False: 
       get_basic_stats_for_season(season)
    player_stats = json.loads(open(season+filename).read())
    if name == None and player_id != None:
       return player_stats[player_id]
    elif name!=None and player_id==None:
       player_to_id = json.loads(open('all_ids.json').read())
       return player_stats[str(player_to_id[name])]
    return None                                 

def get_basic_stats_by_player(season, name=None, player_id=None): 
    if path.exists("all_ids.json") == False:
       get_all_players_dict()
    if path.exists(season+"all_stats.json") == False: 
       get_basic_stats_for_season(season)
    player_stats = json.loads(open(season+"all_stats.json").read())
    if name == None and player_id != None:
       return player_stats[player_id]
    elif name!=None and player_id==None:
       player_to_id = json.loads(open('all_ids.json').read())
       return player_stats[str(player_to_id[name])]
    return None 

def get_bio_stats_by_player(season, name=None, player_id=None):
    if path.exists("all_ids.json") == False:
       get_all_players_dict()
    if path.exists(season+"bio_stats.json") == False: 
       get_bio_stats_for_season(season)
    player_stats = json.loads(open(season+"bio_stats.json").read())
    if name == None and player_id != None:
       return player_stats[player_id]
    elif name!=None and player_id==None:
       player_to_id = json.loads(open('all_ids.json').read())
       return player_stats[str(player_to_id[name])]
    return None 
       
                                     
    