from dialouges import invDesc, twoToned
from colors import Colors


class PlayerSetup:
    def __init__(
        self,
        PATH,
        username="Guest",
        health=100,
        cash=0,
        inv=["Grapple", "Decoder", "Stealth Suit", "Small Blade"],
        progress=None,
    ):
        self.username = username
        self.health = health
        self.cash = cash
        self.inv = inv
        self.PATH = PATH
        self.progress = progress

    def __toDict__(self):
        return {
            "username": self.username,
            "health": self.health,
            "cash": self.cash,
            "inv": self.inv,
            "PATH": self.PATH,
            "progress": self.progress,
        }

    def __stats__(self):
        stats = self.__toDict__()
        for stat, value in stats.items():
            if type(value) == list:
                value = " | ".join(value)
            twoToned(str(stat), str(value), Colors.ORANGE, Colors.GREEN, 0.01)

    def __inv__(self):
        invDesc(self.inv)
