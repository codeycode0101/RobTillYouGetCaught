from colors import Colors

"""
Locations = {
    path1: {
        "desc": "Description of the location",
        "options": {
            "Option 1": "Next location path",
            "Option 2": "Next location path",
            ...
        },
    }
    path2: {
        ...
    }
    ...
}
"""
Locations = {
    "accept": {
        "Truck": {
            "desc": "You are in the truck... Outside you see the city slipping away moving into the dark woods where the base is located...",
            "options": {
                "Stop at base": "Base",
                "Drive onto dropoff point": "Harbor",
            },
        },
        "Base": {
            "desc": "You are at the central base... In the distance, you can hear the creaking of the woods. You are directed to your quarters, but have the choice to look around...",
            "options": {
                "Go to quarters": "Quarters",
                "Explore base": "basePlaces",
            },
        },
        "Quarters": {
            "desc": "You arrived at quarters and you meet two roommates. Their names are Sam and Veronica...",
            "options": {
                "Stay at quarters": "quarterBed",
                "Talk to Sam": ["Sam", "person"],  # TODO: CONVO
                "Talk to Veronica": ["Veronica", "person"],  # TODO: CONVO
                "Go outside to base": "Base",
            },
        },
        "quarterBed": {
            "desc": "You lied down on the bed... thump! You felt something hard lying down your back.. opening up the covers you find a sticky bomb hidden underneath...",
            "options": {
                "Steal the bomb": [
                    {"Bomb", "collect"},
                    "item",
                ],  # TODO: ITEM COLLECTION
                "Talk to Sam about the bomb": ["Sam", "person"],  # TODO: CONVO
                "Talk to Veronica about the bomb": [
                    "Veronica",
                    "person",
                ],  # TODO: CONVO
                "Go outside to base": "Base",
            },
        },
        "basePlaces": {
            "desc": "You stroll around and observe many camps, storage, and cabins around the base. One warehouse particularly caught your eye. Curious, you look around the vicinity to find it empty...",
            "options": {
                "Check out warehouse": "Warehouse",
                "Don't creep around": "Base",
            },
        },
        "Warehouse": {
            "desc": "You enter the warehouse... It's empty except for a wooden box on the floor, It is locked by the metal padlock...",
            "options": {
                "Attempt to break the box open": "Woods",
                "Leave warehouse": "basePlaces",
            },
        },
        "Woods": {
            "desc": "You attempt to break the wooden box open... ALARM suddenly rings out loud attracting guards so you ran to the woods for cover.",
            "options": {
                "Leave the woods": "Guards",  # TODO: Continue this route with new key
                "Continue deeper into the woods": "deepWoods",  # TODO: Continue this route with new key
            },
        },
        "Vault": {
            "desc": "You are at the Time Vault... The vault is guarded by a massive door.",
            "options": {
                # TODO: Continuation of story
                "Board truck back to base": "Base",
            },
        },
        "Harbor": {
            "desc": "You have reached the furthest point on land within 1.5 km in proximity of the Vault... the waters are rough and lightning is prone to hit the sea every so often... In the distance you can make out a shimmering object floating on the water.",
            "options": {
                "Explore Harbor": "harborPlaces",  # TODO: Continue this route with new key
                "Board ship": "Ship",
            },
        },
        "Ship": {
            "desc": "You are on a ship... The ship is filled with a variety of junk and items... it took off and swayed dangerously on the rough seas, wind shook the sails and blew through the seven seas...",
            "options": {
                "Explore ship": "shipPlaces",
                "Talk to captain": ["Captain", "person"],  # TODO: CONVO
            },
        },
        "shipPlaces": {
            "desc": "You walk around and see many rooms and storage facilities in the lower level of the ship. And decide to go take look...",
            "options": {
                "Go to Kitchen": "Kitchen",  # TODO: Continue this route with new key
                "Go to Weapon's vault": "weaponVault",  # TODO: Continue this route with new key
                "Go to toliet": "Toliet",  # TODO: Continue this route with new key
                "Go to cabin": "Cabin",  # TODO: Continue this route with new key
            },
        },
        "Kitchen": {},
        "Toliet": {},
        "Cabin": {},
        "weaponVault": {},
    },
    "refuse": {},
}

Items = {
    "Grapple": {
        "tier": "uncommon",
        "desc": "Tool for scaling walls. (Works for only brick and wooden walls)",
    },
    "Decoder": {
        "tier": "uncommon",
        "desc": "Device for decoding gate passcodes. (Up to MAX 8 digits)",
    },
    "Stealth Suit": {
        "tier": "epic",
        "desc": "Suit designed to blend in with the crowd.",
    },
    "Small Blade": {
        "tier": "common",
        "desc": "Blade forged from pure steel. (Can cut ropes and wires)",
    },
}

Tiers = {
    "common": Colors.LIGHT_GRAY,
    "uncommon": Colors.GREEN,
    "rare": Colors.DARK_BLUE,
    "epic": Colors.PURPLE,
    "legendary": Colors.YELLOW,
    "mythical": Colors.RED,
}
