import sys, subprocess
from colors import Colors
from gameSetup import checkExistingAccount
from dialouges import dia

"""
ColorCodes:
Blue --> Dialouge/Messgaes 💬💬
Yellow --> Prompts/Asking ❓❓
Orange --> FileHandling
Green/Lime --> Acknowledge/Postive
Red --> Serious/Negative
"""


def main():

    dia("Welcome to RobTillYouGetCaught...")
    PLAYER = checkExistingAccount()
    if not PLAYER:
        dia("No active player found. Please create a new account.", Colors.RED)
        return
    if PLAYER.PATH == "accept":
        subprocess.run(["python", "accept.py"])
    elif PLAYER.PATH == "refuse":
        subprocess.run(["python", "refuse.py"])
    elif PLAYER.PATH == "quit":
        dia("Exiting...", Colors.RED)
        sys.exit()
    else:
        dia("Invalid choice.", Colors.RED)


if __name__ == "__main__":
    main()

# {
#     "Peak": {
#         "username": "Peak",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": "shipPlaces"
#     },
#     "Ease": {
#         "username": "Ease",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": "Truck"
#     },
#     "Guest_0000": {
#         "username": "Guest_0000",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": "Truck"
#     },
#     "Guest_0001": {
#         "username": "Guest_0001",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": "Ship"
#     },
#     "Nahm": {
#         "username": "Nahm",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": null
#     },
#     "Guest_0002": {
#         "username": "Guest_0002",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": "Harbor"
#     },
#     "Guest_0003": {
#         "username": "Guest_0003",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": null
#     },
#     "Guest_0004": {
#         "username": "Guest_0004",
#         "health": 100,
#         "cash": 0,
#         "inv": [
#             "Grapple",
#             "Decoder",
#             "Stealth Suit",
#             "Small Blade"
#         ],
#         "PATH": "accept",
#         "progress": null
#     }
# }
