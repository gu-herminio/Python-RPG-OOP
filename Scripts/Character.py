class Character:
    def __init__(self, name, hp, atk, dfs):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfs = dfs

    def __str__(self):
        return f"Name: {self.name}, HP: {self.hp}, ATK: {self.atk}, DEF: {self.dfs}"

    def attack(self, atk):
        self.hp -= atk
        print(f"{self.name} was attacked, your new HP is: {self.hp}")

    def defense(self):
        print(f"{self.name} defended the attack, your HP still: {self.hp}")

    def calculate(self):
        if self.hp <= 0:
            print(f"The character {self.name} is dead.")
        else:
            print("The duel will continue.")
