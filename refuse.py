from colors import Colors
from main import dia
from playerUtils import getActivePlayer

dia("---------------------------------------------")
dia("So... You have REFUSED...")
dia("GUARDS!!!!!")

# Break out of maximum security prison


def main():
    PLAYER = getActivePlayer()
    if PLAYER is None:
        dia("No active player found. Please restart the game.", Colors.RED)
        exit()
    PLAYER.__stats__()


if __name__ == "__main__":
    main()
