import json
from colors import Colors
from dialouges import update, dia, twoToned
from fileUtils import openFile


def handleConvo(npc):
    characters = openFile("characters.json")
    if not characters:
        dia("No characters found in characters.json", Colors.RED)
        return None

    npcData = characters.get(npc, None)
    if not npcData or npcData.get("branches") is None:
        update(f"Dialouges for {npc.title()} will be added in the next update")
        return None

    # * Character's introduction
    intro = npcData["branches"].get("introduction", None)
    if intro:
        diaIntro = intro.get("dialouges", [])
        for dialogue in diaIntro:
            twoToned(npc, dialogue)
        return intro.get("options")
