### DO NOT EDIT THIS PART ###
from sys import argv
from constant import *
from enum import Enum
from datetime import timedelta
from typing import Dict, List, Tuple, Callable, Any

import trueskill

DEBUG_MODE = "--debug" in argv[1:]
# type definition
EMOJI = str
LOWERCASE_STR = str
#############################

# Bot credentials
CLIENT_ID = 1075739307144388659
CLIENT_SECRET_PATH = 'private/client_secret'
TOKEN_PATH = "private/token_cplbot"

# General
COMMAND_PREFIX = "."
DEVELOPPER_CONTACT = "<@384274248799223818>"
CPL_GUILD_ID = 1087477187898261605
MODERATOR_ROLE_ID = 291753249361625089
ADMIN_ROLE_ID = 291758290193612811
BOT_PROGRAMMER_ROLE_ID = 489447573736914946
CAN_USE_DBG_COMMAND = [ADMIN_ROLE_ID, BOT_PROGRAMMER_ROLE_ID]
CAN_USE_ADMIN_COMMAND = [ADMIN_ROLE_ID, BOT_PROGRAMMER_ROLE_ID]

# Auto-moderator
NO_COMMANDS_CHANNELS = [1087477187898261605, 413532530268962816]
SPECIFIC_CHANNEL_COMMAND : Dict[str, List[int]] = {
    "vote": [715011144028258334],
    "teamvote": [715011144028258334]
}

# Report
REPORT_CHANNEL_ID = 413532530268962816
HISTORY_CHANNEL_ID = 569705866224467988
#  All text after this will be ignored by report parser
MODERATOR_TAG = "<@&291753249361625089>"

# Register
SERVER_IP = "51.68.123.207"
SERVER_PORT = "31612"
OAUTH_LINK_BASE = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri=http%3A%2F%2F{SERVER_IP}:{SERVER_PORT}&response_type=code&scope=identify%20connections&state="
WELCOME_CHANNEL = 368928122219003904
NEW_REGISTERED_LOG_CHANNEL = 615805208848498688
ROLES_WHEN_REGISTED = [615780983047979008, 628464552882995200, 444330435070132235, 577702305999093763]

# Ban
SUSPENDED_ROLE_ID = 294099361053540353
GREAT_PEOPLE_ROLE_ID = 761095033738362921
SUSPENDED_PLAYER_CHANNEL_ID = 507906789984174090
SUSPENSIONS_TYPE_TIERS = {
    "quit": 1,
    "minor": 1,
    "moderate": 2,
    "major": 4,
}
QUIT_APPLY_BASIC_SUSPENSION = True
QUIT_SUSPENSION_TIME = [1, 2, 3, 5, 8, 13, 21, 34, 55, 180]  # Only Used if QUIT_APPLY_BASIC_SUSPENSION is False
SUSPENSION_TIME = [1, 2, 3, 5, 8, 13, 21, 34, 55, 180]
DAY_TO_PERMA = 180
GAME_TO_DECAY_TIER = 30
TIME_TO_DECAY_TIER = timedelta(days=45)
REPORT_APPLY_QUIT = False
REPORT_APPLY_OVERSUB = True
OVERSUB_PENALTY_TIER = "minor"
GAME_TO_GREAT_PEOPLE = 50

# Ranked
RANKED_ROLE = 615780983047979008
RANKS_ROLES : List[Tuple[str, int, int]] = [
    ("Deity", 628461624524800000, 2000),
    ("Immortal", 628464081346625536, 1800),
    ("Emperor", 628464280118755351, 1600),
    ("King", 628464338985943040, 1500),
    ("Prince", 628464428593184778, 1400),
    ("Warlord", 628464457491939339, 1300),
    ("Chieftain", 628464491129995264, 1200),
    ("Settler", 628464552882995200, 1100),
    ("Builder", 1011972019274920016, 1000),
    ("Scout", 1011972375010611252, 0)
]

# TrueSkill Ranking
MU = 1250
SIGMA = 150
BETA = 400
TAU = 10

QUITTER_MAX_POINT = -50
SUBBED_MAX_POINT = 0
SUB_MINIMUM_POINT = 5
DONT_CHANGE_SIGMA_ON_PENALTIES = True

def SKILL(rating : trueskill.Rating, teamer=False) -> float:
    if teamer:
        return rating.mu - max(rating.sigma - 100, 0) + (rating.mu - MU) * 2
    return rating.mu - max(rating.sigma - 100, 0)

LEADERBOARDS : Dict[str, Dict[str, Any]]= {
    'FFA': {'channel_id': 587158329877331969,
            'message_id': [867550377036480512, 867550377809674250, 867550378526900286, 867550379440603146, 867550380437798993,
                            867550398939398174, 867550399250563113, 867550400600604682, 867550401434746880, 867550402169274368]},
    'Teamer': {'channel_id': 587158165309751300,
                'message_id': [867563113527640064, 867563114308304916, 867563115167219762, 867563115776311337, 867563119047082005,
                            867563135253610536, 867563136025886720, 867563136860815420, 867563137758265355, 867563138551250974]},
    'PBC': {'channel_id': 697619298507554826,
            'message_id': [942586227289358396, 942586228082090044, 942586228866416670, 942586229667557407, 942586230187630623,
                            942586248881647646, 942586249674371092, 942586250869743697, 942586251658268742, 942586252388081734]}
}
SEASON_LEADERBOARDS : Dict[str, Dict[str, Any]]= {
    'FFA': {
        'channel_id': 1090625022739107961,
        'message_id': [
            1121145181438218312, 1121145186760802384, 1121145189159948398, 1121145191349358642, 1121145193278738492,
            1121145194826432512, 1121145197322047680, 1121145199322742865, 1121145201042395186, 1121145338569425027
        ]
    },
    'Teamer': {
        'channel_id': 1121535918126415902,
        'message_id': [
            1121536481144614913, 1121536483820576869, 1121536486760779871, 1121536491114483842, 1121536493983367198,
            1121536495996645436, 1121536498492264448, 1121536502074191932, 1121536504846614670, 1121536507132510228
        ]
    },
    'PBC': {
        'channel_id': 1121536103359455332,
        'message_id': [
            1121536243461783736, 1121536305050947715, 1121536306187608226, 1121536308196691978, 1121536310776188988,
            1121536312260972705, 1121536314311983185, 1121536316216193065, 1121536318573391902, 1121536353168015410
        ]
    }    
}

# leaders
LEADER_CSV_PATH = "public_data/leaders.csv"
AMBIGOUS_QUERY : Dict[LOWERCASE_STR, List[str]] = {
    "america": ["Teddy-RR", "Teddy-BM"],
    "teddy": ["Teddy-RR", "Teddy-BM"],
    "england": ["Victoria", "Eleanor-En"],
    "france": ["Catherine-BQ", "Catherine-Magnificent", "Eleanor-Fr"],
    "greece": ["Pericles", "Gorgo"],
    "india": ["Gandhi", "Chandragupta"],
    "china": ["Qin-Shi", "Kublai-China"],
    "mongolia": ["Genghis-Khan", "Kublai-Mongolia"],
    "kublai": ["Kublai-Mongolia", "Kublai-China"],
    "eleanor": ["Eleanor-En", "Eleanor-Fr"]
}
USE_FIRST_LEADER_IF_AMBIGOUS = False

# Draft / VOTE
MINUTES_BEFORE_REMOVING_VOTE = 15
DRAFT_MODE_TITLE = "Draft Mode"
class DraftMode(Enum):
    WITH_TRADE = "Trade Allowed"
    NO_TRADE = "Trade Forbidden"
    BLIND = "Blind"
    RANDOM = "All Random"
    DRAFT_2 = "Draft 2"
    CWC = "CWC"
    DDRAFT_9_3_1 = "Dynamic 9 3 1"

VOTE_SETTINGS : Dict[str, List[Tuple[EMOJI, str]]] = {
    "Communication": [(EMOJI_NO_ENTRY, "None"), (LETTER.F, "Private between Friends and Allies"), (LETTER.P, "All Private Allowed"), (EMOJI_PLUS, "All Public Only")],
    "Official Friends/Allies": [(NB[0], "None"), (NB[1], "One"), (NB[2], "Two"), (EMOJI_INFINITY, "Unlimited")],
    "BYC Enabled (Capitals Only)": [(EMOJI_OK, "Yes "), (EMOJI_NO_ENTRY, "No")],
    "Game Duration": [(NB[4], "4 Hours"), (NB[6], "6 Hours"), (EMOJI_INFINITY, "Unlimited")],
    "Map": [(LETTER.P, "Pangea"), ("🏝", "Contient & Island"), (NB[7], "7 seas"), (LETTER.H, "Highland"), (LETTER.L, "Lakes"), ("🗾", "Archipelago"),
            (LETTER.F, "Fractal"), ("🗺️", "Small Continents"), ("🌋", "Primordial"), (LETTER.T, "Tilted Axis"), ("🌊", "Inland Sea"), ("💦", "Wetlands"), ("❓", "Random")],
    "Disasters": [(NB[0], "0"), (NB[1], "1"), (NB[2], "2"), (NB[3], "3"), (NB[4], "4")],
    "CC Voting": [(EMOJI_DOWN, "10 Turns Earlier"), (EMOJI_NEUTRAL, "No Change"), (EMOJI_UP, "10 Turns Later"), (EMOJI_DOUBLE_UP, "20 Turns Later")],
    DRAFT_MODE_TITLE: [("✅", DraftMode.WITH_TRADE.value), ("🚫", DraftMode.NO_TRADE.value), ("🙈", DraftMode.BLIND.value), ("❓", DraftMode.RANDOM.value)]
}
DEFAULT_VOTE_SETTINGS: Dict[str, str] = {
    "Gold Trading ": 'Not Allowed',
    "Luxuries Trading ": 'Allowed',
    "Strategics Trading ": 'Not Allowed',
    "Military Alliance ": 'Not Allowed',
    "Timer ": 'Competitive',
    'Resources ': 'Abundant',
    'Strategics ': 'Abundant',
    'Ridges Definition ': 'Classic',
    'Wonders ': 'Standard'
}
TEAM_VOTE_SETTINGS : Dict[str, List[Tuple[EMOJI, str]]] = {
    "1 Remap Token Per Team (T10)": [(EMOJI_OK, "Yes "), (EMOJI_NO_ENTRY, "No")],
    "BYC Enabled (Capitals Only)": [(EMOJI_OK, "Yes "), (EMOJI_NO_ENTRY, "No")],
    "Map": [(LETTER.P, "Pangea"), ("🏝", "Contient & Island"), (NB[7], "7 seas"), (LETTER.H, "Highland"), (LETTER.L, "Lakes"), ("🗾", "Archipelago"),
            (LETTER.F, "Fractal"), ("🗺️", "Small Continents"), ("🌋", "Primordial"), (LETTER.T, "Tilted Axis"), ("🌊", "Inland Sea"), ("💦", "Wetlands"), ("❓", "Random")],
    "Timer": [("🐌", "Casual"), ("🕑", "Dynamic"), ("⏩", "Competitive")],
    "Ressources": [(LETTER.S, "Standard"), (LETTER.A, "Abundant")],
    "Strategics": [(LETTER.S, "Standard"), (LETTER.A, "Abundant"), (LETTER.E, "Epic"), (LETTER.G, "Guaranteed")],
    "Ridges definition": [(LETTER.S, "Standard"), (LETTER.C, "Classic"), (LETTER.L, "Large opening"), (LETTER.I, "Impenetrable")],
    "Disasters": [(NB[0], "0"), (NB[1], "1"), (NB[2], "2"), (NB[3], "3"), (NB[4], "4")],
    "Wonders": [(EMOJI_NO_ENTRY, "None"), (EMOJI_DOWN, "Scarse"), (EMOJI_NEUTRAL, "Standard"), (EMOJI_UP, "Abundant")],
    DRAFT_MODE_TITLE: [(NB[2], DraftMode.DRAFT_2.value), ("🌍", DraftMode.CWC.value), (NB[9], DraftMode.DDRAFT_9_3_1.value), ("❓", DraftMode.RANDOM.value)]
}
SECRET_CC_VOTE_SETTINGS : Dict[str, List[Tuple[EMOJI, str]]] = {
    "CC to": 
    [(EMOJI_OK, "Yes"), (EMOJI_NO, "No")],
}
SECRET_IRREL_VOTE_SETTINGS : Dict[str, List[Tuple[EMOJI, str]]] = {
    "Irrel": 
    [(EMOJI_OK, "Yes"), (EMOJI_NO, "No")],
}
SECRET_SCRAP_VOTE_SETTINGS : Dict[str, List[Tuple[EMOJI, str]]] = {
    "Scrap": 
    [(EMOJI_OK, "Yes"), (EMOJI_NO, "No")],
}
SECRET_REMAP_VOTE_SETTING : Dict[str, List[Tuple[EMOJI, str]]] = {
    "Remap" :
    [(EMOJI_OK, "Yes"), (EMOJI_NO, "No")]
}


if DEBUG_MODE:
    CLIENT_ID = 427867039135432714
    CLIENT_SECRET_PATH = 'private/client_secret_eldenbot'
    TOKEN_PATH = "private/token_eldenbot"
    COMMAND_PREFIX = "cpl/"
    SERVER_IP = "127.0.0.1"
    OAUTH_LINK_BASE = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri=http%3A%2F%2F{SERVER_IP}:{SERVER_PORT}&response_type=code&scope=identify%20connections&state="
    REPORT_CHANNEL_ID = 834418663674740767
    HISTORY_CHANNEL_ID = 507906789984174090
