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
