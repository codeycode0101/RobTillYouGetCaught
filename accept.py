import keyboard
from gameSetup import handleOptions, isHash
from dialouges import charDia, dia, twoToned, imput, lineBreaker, update
from playerUtils import getActivePlayer, playerDataSave
from data import Locations
from colors import Colors
from fileUtils import openFile

"""
JSON file format:

{
    "Character": [
        ["Dialogue 1", "Dialogue 2", ...],
        {
            "Choice1": "Result 1",
            "Choice2": "Result 2",
            "Choice3": "Result 3",
            ...
        }
    ],
    ...
"""


def Setup():
    global PLAYER, lpath
    PLAYER = getActivePlayer()
    if PLAYER is None:
        dia("No active player found. Please restart the game.", Colors.RED)
        exit()
    lpath = Locations[PLAYER.PATH]  # l --> location, path --> path


def exitGame(Player):
    # Save data | State: Exit | Update progress (KEY)
    # Param: Player - The player Object of class is passed.
    playerDataSave(Player, state="exit")
    dia(f"Saving and exiting game...", Colors.GREEN)
    exit()


def ADMIN():
    """
    Allows the admin to change the player's location, inventory, or stats dynamically.
    """

    global cloc
    dia("[ADMIN CONTROL ENABLED]", Colors.ORANGE)

    if PLAYER is None:
        dia("No active player found. Please restart the game.", Colors.RED)
        exit()

    while True:
        dia("[ADMIN MODE]", Colors.PINK)
        dia("Available commands:", Colors.BLUE)
        dia("1. changeloc() - Change the player's current location.", Colors.YELLOW)
        dia("2. stats() - Display the player's current stats.", Colors.YELLOW)
        dia("3. exit() or quit() - Exit admin mode.", Colors.YELLOW)
        choice = input(">>> ").strip()
        match choice:
            case "changeloc()":
                dia("[ALL LOCATIONS]", Colors.BLUE)
                acceptLocations = Locations.get("accept")
                if acceptLocations is None:
                    dia("No locations found for the 'accept' path.", Colors.RED)
                    continue

                placesAll = list(acceptLocations.keys())
                placesLower = [place.lower() for place in placesAll]

                for place in placesLower:
                    dia(f"- {place.title()}", Colors.YELLOW)

                newLoc = imput("New Location: ", placesLower)
                newLoc = placesAll[placesLower.index(newLoc)]

                # Update cloc & progress
                PLAYER.progress = cloc = newLoc

                dia(f"[Location changed to {cloc}]", Colors.GREEN)
                lineBreaker()
                PLAYER.__stats__()
                lineBreaker()

            case "stats()":
                lineBreaker()
                PLAYER.__stats__()
                lineBreaker()

            case "exit()" | "quit()":
                dia("[EXIT ADMIN MODE]", Colors.RED)
                lineBreaker()
                break
            case _:
                dia("[INVALID COMMAND. TRY AGAIN.]", Colors.RED)


def gameIntro():
    """
    This function is responsible for introducing the game to the player and
    taking them to meet the frontman. It loads character dialogue options
    from a JSON file and returns these options for further processing.

    Returns:
    A dictionary containing dialogue options for the Frontman character.
    """
    lineBreaker()
    dia("I see you have accepted...")
    dia("Very well then... I'll take you to the frontman.")

    # Load Characters' data from JSON file
    charData = openFile("characters.json")

    # Display the dialogue options for the Frontman character
    options = charDia(charData, "Frontman")
    return options


def gameLoop():
    # cloc = Current Location
    # locProps = Location's properties (desc, options)
    # lpath = Location Path

    global cloc, player
    if PLAYER is None:
        dia("No active player found. Please restart the game.", Colors.RED)
        exit()
    prevLoc = cloc = "Truck" if not PLAYER.progress else PLAYER.progress
    locProps = None
    while True:

        if isHash(cloc):
            # Go into location for relevant desc and options
            locProps = lpath.get(cloc, None)

        # Possible check for no key.
        if not locProps:
            dia("No Location detected. Returning to prevLoc...", Colors.RED)
            cloc = PLAYER.progress = prevLoc
            continue

        PLAYER.progress = cloc  # Save Player's location (progress) in each iteration

        # Debug TODO: Remove after finished with game
        lineBreaker()
        PLAYER.__stats__()
        lineBreaker()

        # Display location and desc
        twoToned("[Current Location]", cloc)
        dia(locProps["desc"])
        loptions = locProps["options"]
        # loptions = Location Options
        option = handleOptions(loptions)

        # option = (index, choice ⭐)
        if option[-1] == "ADMIN":
            ADMIN()
            continue
        elif option == "Exit":
            exitGame(PLAYER)
        else:
            # Save previous location
            prevLoc = cloc
            # Find location of chosen option (OPTION: NEXT_LOCATION)
            # Options = (Index, option 🔑)
            cloc = loptions[option[-1]]
            if isinstance(cloc, (list, tuple)):
                # For item/person: cloc = ["Next Location", "mode"]
                match cloc[-1]:
                    case "item":
                        update("Inventory Algorithm")
                    case "person":
                        update("Conversation Algorithm")
                dia("Returning to prevLoc...", Colors.RED)
                cloc = PLAYER.progress = prevLoc
                continue


def main():
    """
    This function is the entry point of the game. It initializes the player,
    retrieves the dialogue options from the game intro, and then enters the main game loop.

    The function does not return any value. It runs indefinitely until the player
    selects the option to start the mission.
    """
    Setup()

    if PLAYER is None:
        dia("No active player found. Please restart the game.", Colors.RED)
        exit()

    if not PLAYER.progress:
        options = gameIntro()
        charData = openFile("characters.json")
        if charData is None:
            raise FileNotFoundError("characters.json not found")
        while True:
            options = handleOptions(options, "dialog")
            if options == "Exit":
                exitGame(PLAYER)
            elif options[0] == "5":
                dia("STARTING THE MISSION...", Colors.CYAN, delay=0.1)
                lineBreaker()
                gameLoop()
                break
            options = charData["Frontman"][1]

    else:
        dia("Your progressed has been saved!", Colors.GREEN)
        lineBreaker()
        gameLoop()


if __name__ == "__main__":
    main()
