import sys, time
from colors import Colors
from data import Tiers, Items


def dia(
    msg,
    color=Colors.BLUE,
    type="print",
    delay=0.03,
):
    for char in msg:
        sys.stdout.write(char if type == "speak" else color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    if type == "print" or type == "speak":
        print("")
    elif type == "ask":
        sys.stdout.write("\n>> ")
        return ""


def imput(prompt, valid_choices, color=Colors.YELLOW):
    """
    Continuously prompts the user until a valid input is given.
    :func imput: IMPORTANT input

    :param prompt: The message to show to the user.
    :param valid_choices: A list or set of valid input choices (case-insensitive).
    :param color: The color for the prompt.
    :return: The valid input choice as uppercase.
    """
    while True:
        choice = input(dia(prompt, color, "ask")).strip().casefold()
        if choice in valid_choices:
            return choice
        dia("Invalid choice. Please try again...", Colors.RED)


def twoToned(
    subject,
    dialogue,
    charColor=Colors.CYAN,
    textColor=Colors.YELLOW,
    delay=0.05,
):
    """
    Prints dialogue with the character's name in a different color.

    :param character: The name of the speaking character.
    :param dialogue: The dialogue to display.
    :param char_color: The color for the character's name.
    :param text_color: The color for the dialogue.
    :param delay: Typing effect delay for dialogue.
    """
    dia(
        charColor + subject + ": " + textColor + dialogue + Colors.RESET,
        type="speak",
        delay=delay,
    )


def charDia(charFile, charName):
    global speaker, data
    if charName in charFile:
        speaker, data = charName, charFile[charName]
        for dialouge in data[0]:
            twoToned(speaker, dialouge, delay=0.05)
            time.sleep(0.6)
        return data[1]


def itemsDesc(items):
    for i in items:
        color = Tiers[Items[i]["tier"]]
        twoToned(i, Items[i]["desc"], color)


def invDesc(inv):
    output = []
    for i in inv:
        color = Tiers[Items[i]["tier"]]
        output.append(f"{color}{i}\033[0m")  # Append colored item name

    dia(
        "Inventory: " + " | ".join(output),
        type="speak",
        color=Colors.RESET,
        delay=0.025,
    )  # Print all items on the same line


# Linebreaker using hyphens
lineBreaker = lambda x=45: dia("-" * x, Colors.MAGENTA)
# # Update message
update = lambda new: dia(f"{new} will be added in the next update", Colors.RED)
