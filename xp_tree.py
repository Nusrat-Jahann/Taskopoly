class XPSystem:
    def _init_(self):
        self.total_xp = 0

    def add_xp(self, xp):
        if xp > 0:
            self.total_xp += xp

    def get_level(self):
        if self.total_xp >= 300:
            return 3
        elif self.total_xp >= 100:
            return 2
        else:
            return 1

    def get_level_name(self):
        level = self.get_level()

        if level == 3:
            return "Young Tree"
        elif level == 2:
            return "Sprout"
        else:
            return "Seed"

    def get_tree_stage(self):
        level = self.get_level()

        if level == 3:
            return "🌳"
        elif level == 2:
            return "🌿"
        else:
            return "🌱"

    def get_progress(self):
        level = self.get_level()

        if level == 1:
            current_level_xp = self.total_xp
            next_level_xp = 100
        elif level == 2:
            current_level_xp = self.total_xp - 100
            next_level_xp = 200
        else:
            current_level_xp = self.total_xp - 300
            next_level_xp = 0

        return current_level_xp, next_level_xp

    def display_progress(self):
        level = self.get_level()
        level_name = self.get_level_name()
        tree = self.get_tree_stage()

        print(f"Level: {level} - {level_name} {tree}")
        print(f"Total XP: {self.total_xp}")

        if level < 3:
            if level == 1:
                print(f"XP needed for next level: {100 - self.total_xp}")
            else:
                print(f"XP needed for next level: {300 - self.total_xp}")
        else:
            print("Maximum level reached!")