import json
from colors import Colors
from dialouges import update, dia, twoToned
from fileUtils import openFile
from gameSetup import handleOptions


def handleConvo(npc):
    characters = openFile("characters.json")
    if not characters:
        dia("No characters found in characters.json", Colors.RED)
        return None

    npcData = characters.get(npc, None)
    if not npcData or npcData.get("branches") is None:
        update(f"Dialouges for {npc.title()} will be added in the next update")
        return None

    # ! Character's dialouges
    # ? pBranches = Possible convo branches
    pBranches = npcData["branches"]
    intro = pBranches.get("introduction", None)
    if intro:
        diaIntro = intro.get("dialouges", [])
        for dialogue in diaIntro:
            twoToned(npc, dialogue)
        print(intro.get("options", {}))
        branch = handleOptions(intro.get("options", {}), "npc")
        # * Conversation loop
        while True:
            dia(f"Next Scene Key: {branch}")
            branchMetaData = pBranches.get(branch, None)
            if branchMetaData:
                diaBranch = branchMetaData.get("dialouges", [])
                for dialogue in diaBranch:
                    twoToned(npc, dialogue)
                if branch == "Exit Conversation":
                    return
            else:
                update(
                    f"Dialouges for this path hasn't been added yet. Please wait for the next update ^^"
                )
                return
            branch = handleOptions(branchMetaData.get("options", {}), "npc")
