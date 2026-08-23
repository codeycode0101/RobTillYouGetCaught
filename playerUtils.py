import json
from playerObj import PlayerSetup
from colors import Colors
from fileUtils import openFile
from dialouges import dia, imput


def playerDataSave(PLAYER, state="join"):
    """
    Save players' data in a JSON file.

    :param PLAYER: A Class Object representing the player.
    :type PLAYER: Class Object
    :param state: The state of the player, either "join" or "exit".
    :type state: str

    This function saves the data of a player in a JSON file named "player_data.json". If the file does not exist, it will be created with an empty dictionary. The function updates the player's data based on the provided state and writes the updated data back to the file.

    :return: None
    :rtype: None
    """

    # Try to load existing player data, or start with an empty dictionary
    try:
        playerData = openFile("player_data.json")
    except (FileNotFoundError, json.JSONDecodeError):
        playerData = {}

    if not playerData:
        playerData = {}

    # EXPECTS param: PLAYER - as Class Object
    if state == "join":
        playerData["ACTIVE_PLAYER"] = PLAYER.username
    elif state == "exit":
        playerData.pop("ACTIVE_PLAYER")

    playerData[PLAYER.username] = PLAYER.__toDict__()

    # Write updated data back to file
    openFile("player_data.json", "w", dump=playerData)


def playerDataLoad(Type="login"):
    """
    Load an account from the JSON file and let the player choose.

    :param None: No parameters are required for this function.
    :return: A PlayerSetup object containing the chosen player's data.
    :rtype: PlayerSetup

    This function loads the player data from a JSON file named "player_data.json". If the file does not exist, it will report back an error. The function updates the player's data based on the provided state and writes the updated data back to the file.

    The function then displays the available accounts in the JSON file and prompts the player to choose one. The chosen player's data is then returned as a PlayerSetup object.

    :return: A PlayerSetup object containing the chosen player's data.
    :rtype: PlayerSetup
    """

    playerData = openFile("player_data.json")

    if not playerData:
        dia("No saved accounts found!", Colors.RED)
        return None

    # Remove active player from dict, if it exists
    playerData.pop("ACTIVE_PLAYER", None)

    # Show available accounts
    dia("Available accounts:", Colors.ORANGE)
    choices = list(playerData.keys())
    # Make temp dictionary to store players and index
    playersDict = {}
    index = 0
    for index, username in enumerate(choices, start=1):
        dia(f"{index}. {username}")
        playersDict[str(index)] = choices
    index += 1
    playersDict[str(index)] = "Exit"
    dia(f"{str(index)}. Exit 📤", Colors.RED)

    choiceIndex = imput("Choose an account: ", playersDict)

    if choiceIndex == str(index):
        return "Exit"
    else:
        chosenUser = choices[int(choiceIndex) - 1]

    if Type == "login":
        dia(f"Welcome back, {chosenUser}!", Colors.GREEN)
    elif Type == "delete":
        dia("Account sucessfully deleted!", Colors.GREEN)

    return PlayerSetup(
        playerData[chosenUser]["PATH"],
        chosenUser,
        playerData[chosenUser]["health"],
        playerData[chosenUser]["cash"],
        playerData[chosenUser]["inv"],
        playerData[chosenUser]["progress"],
    )


def getActivePlayer(type="login"):
    """Retrieve the currently playing account from player_data.json."""
    playerData = openFile("player_data.json")
    if not playerData:
        dia("Account bank is empty!", Colors.RED)
        return None

    activeUser = playerData.get("ACTIVE_PLAYER", False)

    # Error Handling
    if not activeUser:
        dia("No active player found!", Colors.RED)
        return None
    elif activeUser not in playerData:
        dia("Active player data not found!", Colors.RED)
        return None

    return PlayerSetup(
        playerData[activeUser]["PATH"],
        activeUser,
        playerData[activeUser]["health"],
        playerData[activeUser]["cash"],
        playerData[activeUser]["inv"],
        playerData[activeUser]["progress"],
    )
