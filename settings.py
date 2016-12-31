import os

## Search Filters
PARKING = ['carport', 'attached garage', 'detached garage', 'off-street parking', 'street parking', 'valet parking']

SEARCH_FILTERS = {"max_price": 2000,
                  "min_price": 0,
                  "parking": PARKING}

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'losangeles'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["wst", "sfv", "lac", "sgv", "lgb", "ant"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    # "la": [
    #   [33.788279, -118.547974],
    #   [34.066312, -118.155289]
    # ],
    "Marina Del Rey": [
        [33.959878, -118.47888],
        [33.992192, -118.430214]
    ],
    "Venice": [
        [33.987068, -118.501453],
        [34.007206, -118.445406]
    ],
    "Santa Monica": [
        [34.006317, -118.51686],
        [34.048535, -118.432789]
    ],
    "Culver City": [
        [33.978812, -118.43914],
        [34.049299, -118.348696]
    ],
    "Playa Vista": [
        [33.943974, -118.458785],
        [33.977816, -118.397598]
    ],
    "Inglewood": [
        [33.927978, -118.405876],
        [34.003293, -118.278637]
    ],
    "DTLA": [
        [34.00742, -118.282585],
        [34.081633, -118.210521]
    ],
    "Hollywood": [
        [34.029918, -118.470538],
        [34.104112, -118.275032]
    ],
    "El Segundo": [
        [33.900199, -118.442526],
        [33.934735, -118.368931]
    ],
    "Hawthorne": [
        [33.898886, -118.37071],
        [33.933422, -118.257694]
    ],
    "Manhattan Beach": [
        [33.872839, -118.423722],
        [33.90251, -118.370476],
    ],
    "Gardena": [
        [33.871968, -118.37135],
        [33.90164, -118.263531]
    ],
    "Hermosa Beach": [
        [33.847449, -118.415116],
        [33.87713, -118.250656]
    ],
    "Redondo Beach": [
        [33.786236, -118.412189],
        [33.851472, -118.35331]
    ],
    "Torrance": [
        [33.787151, -118.354755],
        [33.852387, -118.279187]
    ],
    "Carson": [
        [33.786885, -118.29679],
        [33.871122, -118.202307]
    ],
    "Long Beach": [
        [33.730575, -118.2148],
        [33.873782, -118.118869]
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["marina del rey", "venice", "santa monica", "culver city", "mar vista", "playa vista",
                 "inglewood", "la", "downtown", "el segundo", "gardena", "hawthorne", "manhattan",
                 "manhattan beach", "hermosa", "hermosa beach", "torrance", "long beach", "signal hill"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
}

## The location
WORK_LOCATION = [33.9205867, -118.3271398]

TIME_TO_WORK = "8:30"
TIME_FROM_WORK = "19:00"

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 10 * 60 # 10 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# The token that allows us to connect to walkscore.
# Should be put in private.py, or set as an environment variable.
WS_API_KEY = os.getenv('WS_API_KEY', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass