import os, time, sys
from playerObj import PlayerSetup
from colors import Colors
from dialouges import dia, imput
from playerUtils import playerDataSave, playerDataLoad
from fileUtils import openFile


#  ================================================ STORYLINE FUNCTIONS  ================================================
def game_story(Choice):
    story_line = [
        "In a dimly lit city, where shadows hold secrets, and danger lurks around every corner...",
        "You are a master thief, infamous for your audacious heists and unmatched skills.",
        "But this time, you've set your sights on the grandest prize of all: the Time Vault.",
        "Rumored to hold riches beyond this world, it lies heavily guarded in the heart of an ancient city.",
        "But this won't be easy...",
        "The stakes are high. One wrong move, and you're as good as dead or worse...",
        "So are you up for the challenge, outsmart the guards, and claim the fortune? Or will you fall victim to the traps that await?",
        "The night awaits you young one, and the choice is yours.",
        "IF you ACCEPT, you will be known as the most respected theives of all time and will be rewarded beyond your dreams...",
        "HOWEVER, IF you BACK OUT... well... you wouldn't want to know what happens.. >:)",
        "So do you accept the pact...",
    ]
    if not Choice or Choice == "n":
        for line in story_line:
            dia(line, Colors.LIGHT_PURPLE)
            time.sleep(0.6)
    else:
        for line in story_line[8:]:
            dia(line, Colors.LIGHT_PURPLE)
            time.sleep(0.6)


# ================================================ ACCOUNT FUNCTIONS ================================================
def checkExistingAccount():
    PLAYER = None  # Initialize empty player object
    playerData = openFile("player_data.json")
    if playerData and isinstance(playerData, dict) and len(playerData) > 0:
        dia("Existing account(s) detected...", Colors.GREEN)
        dia("Do you want to continue your progress?", Colors.ORANGE)
        while True:
            acc = imput(
                "LOAD | ADD | DELETE | START OVER",
                ("load", "add", "delete", "start over"),
                Colors.ORANGE,
            )

            if acc == "load":
                PLAYER = playerDataLoad()
                if PLAYER == "Exit":
                    continue
                else:
                    playerDataSave(PLAYER)
                    break

            elif acc == "add":
                dia("Adding a new account...", Colors.LIGHT_BLUE)
                PLAYER = newAccount()
                playerDataSave(PLAYER)  # Save without deleting others
                break
            elif acc == "delete":
                PLAYER = playerDataLoad("delete")
                if PLAYER and PLAYER != "Exit":
                    playerData.pop(PLAYER.username, None)
                    openFile("player_data.json", mode="w", dump=playerData)
                continue

            elif acc == "start over":
                dia(
                    "Starting fresh... All previous accounts will be erased.",
                    Colors.RED,
                )
                confirmDeleteAcc = imput(
                    "Do you confirm to proceed with permenant deletion of accounts? (Y/N)",
                    ("y", "n"),
                    Colors.RED,
                )

                if confirmDeleteAcc == "y":
                    os.remove("player_data.json")  # Deletes existing accounts
                    dia("Accounts removed...", Colors.RED)
                    dia("Creating new accounts...", Colors.LIGHT_BLUE)
                    PLAYER = newAccount()
                    playerDataSave(PLAYER)
                    break
                else:
                    dia("Cancelling operation...", Colors.GREEN)
                    continue

    else:
        dia(
            "No existing accounts found. Please create a new account...",
            Colors.RED,
        )
        PLAYER = newAccount()
        playerDataSave(PLAYER)

    return PLAYER


def newAccount():

    Choice = imput("NAME | GUEST:", ("name", "guest"))
    Player_name = "null"
    if Choice == "name":
        while True:
            Player_name = (
                input(dia("Enter your name:", Colors.YELLOW, "ask")).strip().title()
            )

            if Player_name:
                break
            dia("Name cannot be blank!", Colors.RED)

    elif Choice == "guest":
        playerData = openFile("player_data.json")
        if not playerData:
            playerData = {}
        i = 0
        while True:
            Player_name = f"Guest_{i:04d}"  # Formats as Guest_0000, Guest_0001, etc.
            if Player_name not in playerData:
                break
            i += 1

    Story = input(dia("Skip story (Y/N)?", Colors.YELLOW, "ask")).strip().casefold()

    game_story(Story)

    Choice = imput("ACCEPT | REFUSE | QUIT", ("accept", "refuse", "quit"))
    PLAYER = None
    if Choice == "accept":
        PLAYER = PlayerSetup(Choice, Player_name)
    elif Choice == "refuse":
        PLAYER = PlayerSetup(
            Choice, Player_name, inv=[]
        )  # TODO: work on refuse storyline later and possbily change inv
    return PLAYER


# ================================================ EVENT HANDLER FUNCTIONS =============================================
def handleOptions(options, mode="action"):
    # Make a temporary dict to hold the index and options.
    actionDict = {}
    index = 0
    for index, choices in enumerate(options, start=1):
        dia(f"{index}. {choices}", Colors.LIGHT_BLUE)
        actionDict[str(index)] = choices
    # Add an exit option
    index += 1
    actionDict[str(index)] = "Exit Game"
    dia(f"{str(index)}. Exit Game 📤", Colors.RED)

    # Add hidden administrator option
    actionDict["admin()"] = "ADMIN"

    # Prompt for input and get the chosen key
    optionIndex = imput("Option:", actionDict)
    if optionIndex == str(index):
        return "Exit"

    optionChoice = actionDict[optionIndex]
    if mode == "dialog":
        # Display the dialogue for the chosen option
        for optionDesc in options[optionChoice]:
            dia(optionDesc)

    # Return the index and choice so the caller knows which option was chosen
    return (optionIndex, optionChoice)


def isHash(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False
