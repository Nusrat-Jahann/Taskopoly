from quest import QuestList
from search_sort import search_quests, sort_quests_by_name, sort_quests_by_xp
from queue import QuestQueue
from xp_tree import XPSystem
from undo import UndoStack


def get_quest_by_number(quest_list, quest_number):
    current = quest_list.head
    number = 1

    while current is not None:
        if number == quest_number:
            return current
        current = current.next
        number += 1

    return None


def save_quests(quest_list):
    """Save the current quest state for undo."""
    states = []
    current = quest_list.head

    while current is not None:
        states.append({
            "name": current.name,
            "category": current.category,
            "xp": current.xp,
            "completed": current.completed
        })
        current = current.next

    return states


def restore_quests(quest_list, states):
    """Restore quests from a saved state."""
    quest_list.head = None

    for state in states:
        new_node = type("RestoredNode", (), {})()
        new_node.name = state["name"]
        new_node.category = state["category"]
        new_node.xp = state["xp"]
        new_node.completed = state["completed"]
        new_node.next = None

        if quest_list.head is None:
            quest_list.head = new_node
        else:
            current = quest_list.head

            while current.next is not None:
                current = current.next

            current.next = new_node


def display_header(xp_system):
    print("\n" + "=" * 45)
    print("              TASKOPOLY")
    print("=" * 45)

    level = xp_system.get_level()
    level_name = xp_system.get_level_name()
    tree = xp_system.get_tree_stage()

    print(f"Level: {level} - {level_name} {tree}")
    print(f"Total XP: {xp_system.total_xp}")
    print("=" * 45)


def add_quest(quest_list, undo_stack, undo_history):
    name = input("Enter task name: ").strip()

    if not name:
        print("Task name cannot be empty.")
        return

    previous_state = save_quests(quest_list)

    quest_list.add_quest(name)

    undo_stack.push("Add task")
    undo_history.append(previous_state)

    print("Task added successfully!")


def view_quests(quest_list):
    print("\n--- Your Tasks ---")
    quest_list.view_quests()


def edit_quest(quest_list, undo_stack, undo_history):
    view_quests(quest_list)

    try:
        number = int(input("Enter task number to edit: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    new_name = input("Enter new task name: ").strip()

    if not new_name:
        print("Task name cannot be empty.")
        return

    previous_state = save_quests(quest_list)

    if quest_list.edit_quest(number, new_name):
        undo_stack.push("Edit task")
        undo_history.append(previous_state)
        print("Task updated successfully!")
    else:
        print("Task not found.")


def delete_quest(quest_list, undo_stack, undo_history):
    view_quests(quest_list)

    try:
        number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    previous_state = save_quests(quest_list)

    if quest_list.delete_quest(number):
        undo_stack.push("Delete task")
        undo_history.append(previous_state)
        print("Task deleted successfully!")
    else:
        print("Task not found.")


def complete_quest(quest_list, xp_system, completion_queue,
                   undo_stack, undo_history):
    view_quests(quest_list)

    try:
        number = int(input("Enter task number to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    previous_state = save_quests(quest_list)
    previous_xp = xp_system.total_xp

    quest = get_quest_by_number(quest_list, number)

    if quest is None:
        print("Task not found.")
        return

    xp = quest_list.complete_quest(number)

    if xp is None:
        print("This task is already completed.")
        return

    if xp is False:
        print("Task not found.")
        return

    xp_system.add_xp(xp)
    completion_queue.enqueue(quest.name)

    undo_stack.push("Complete task")
    undo_history.append((previous_state, previous_xp))

    print(f"Task completed! You earned {xp} XP.")
    print(f"Total XP: {xp_system.total_xp}")


def search_task(quest_list):
    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    results = search_quests(quest_list.head, search_term)

    if not results:
        print("No matching tasks found.")
        return

    print("\n--- Search Results ---")

    for number, quest in enumerate(results, start=1):
        status = "Completed" if quest.completed else "Not Completed"

        print(f"{number}. {quest.name}")
        print(f"   Category: {quest.category}")
        print(f"   XP: {quest.xp}")
        print(f"   Status: {status}")
        print()


def sort_tasks(quest_list):
    print("\n1. Sort by Name")
    print("2. Sort by XP (Low to High)")
    print("3. Sort by XP (High to Low)")

    choice = input("Choose an option: ")

    if choice == "1":
        sort_quests_by_name(quest_list.head)
        print("Tasks sorted by name.")

    elif choice == "2":
        sort_quests_by_xp(quest_list.head, descending=False)
        print("Tasks sorted by XP.")

    elif choice == "3":
        sort_quests_by_xp(quest_list.head, descending=True)
        print("Tasks sorted by XP from highest to lowest.")

    else:
        print("Invalid choice.")


def show_queue(completion_queue):
    print("\n--- Completed Task Queue ---")
    completion_queue.display()


def undo_last_action(quest_list, xp_system,
                     undo_stack, undo_history):
    if undo_stack.is_empty():
        print("Nothing to undo.")
        return

    action = undo_stack.pop()
    previous_state = undo_history.pop()

    if isinstance(previous_state, tuple):
        quest_state, previous_xp = previous_state
        restore_quests(quest_list, quest_state)
        xp_system.total_xp = previous_xp
    else:
        restore_quests(quest_list, previous_state)

    print(f"Undone: {action}")


def main():
    quest_list = QuestList()
    completion_queue = QuestQueue()
    xp_system = XPSystem()
    undo_stack = UndoStack()

    # Stores the states needed to actually restore the previous state.
    undo_history = []

    while True:
        display_header(xp_system)

        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Search Tasks")
        print("7. Sort Tasks")
        print("8. Completed Task Queue")
        print("9. XP Progress")
        print("10. Undo")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_quest(quest_list, undo_stack, undo_history)

        elif choice == "2":
            view_quests(quest_list)

        elif choice == "3":
            edit_quest(quest_list, undo_stack, undo_history)

        elif choice == "4":
            delete_quest(quest_list, undo_stack, undo_history)

        elif choice == "5":
            complete_quest(
                quest_list,
                xp_system,
                completion_queue,
                undo_stack,
                undo_history
            )

        elif choice == "6":
            search_task(quest_list)

        elif choice == "7":
            sort_tasks(quest_list)

        elif choice == "8":
            show_queue(completion_queue)

        elif choice == "9":
            print("\n--- XP Progress ---")
            xp_system.display_progress()

        elif choice == "10":
            undo_last_action(
                quest_list,
                xp_system,
                undo_stack,
                undo_history
            )

        elif choice == "0":
            print("\nThank you for using Taskopoly!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()