from keywords import detect_category_and_xp


class QuestNode:
    def __init__(self, name, category, xp):
        self.name = name
        self.category = category
        self.xp = xp
        self.completed = False
        self.next = None


class QuestList:
    def __init__(self):
        self.head = None

    def add_quest(self, name):
        category, xp = detect_category_and_xp(name)

        new_node = QuestNode(name, category, xp)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def view_quests(self):
        if self.head is None:
            print("No quests available.")
            return

        current = self.head
        number = 1

        while current is not None:
            status = "✓ Completed" if current.completed else "○ Not Completed"

            print(f"{number}. {current.name}")
            print(f"   Category: {current.category}")
            print(f"   XP: {current.xp}")
            print(f"   Status: {status}")
            print()

            current = current.next
            number += 1

    def edit_quest(self, quest_number, new_name):
        current = self.head
        current_number = 1

        while current is not None:
            if current_number == quest_number:
                category, xp = detect_category_and_xp(new_name)

                current.name = new_name
                current.category = category
                current.xp = xp
                current.completed = False

                return True

            current = current.next
            current_number += 1

        return False

    def delete_quest(self, quest_number):
        if self.head is None:
            return False

        if quest_number == 1:
            self.head = self.head.next
            return True

        current = self.head
        current_number = 1

        while current.next is not None:
            if current_number + 1 == quest_number:
                current.next = current.next.next
                return True

            current = current.next
            current_number += 1

        return False

    def complete_quest(self, quest_number):
        current = self.head
        current_number = 1

        while current is not None:
            if current_number == quest_number:
                if current.completed:
                    return None

                current.completed = True
                return current.xp

            current = current.next
            current_number += 1

        return False