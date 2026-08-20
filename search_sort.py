def search_quests(head, search_term):
    search_term = search_term.lower()
    current = head
    found_quests = []

    while current is not None:
        if search_term in current.name.lower():
            found_quests.append(current)

        current = current.next

    return found_quests


def sort_quests_by_name(head):
    if head is None or head.next is None:
        return

    end = None

    while end != head:
        current = head

        while current.next != end:
            next_node = current.next

            if current.name.lower() > next_node.name.lower():
                current.name, next_node.name = next_node.name, current.name
                current.category, next_node.category = (
                    next_node.category,
                    current.category
                )
                current.xp, next_node.xp = next_node.xp, current.xp
                current.completed, next_node.completed = (
                    next_node.completed,
                    current.completed
                )

            current = current.next

        end = current


def sort_quests_by_xp(head, descending=False):
    if head is None or head.next is None:
        return

    end = None

    while end != head:
        current = head

        while current.next != end:
            next_node = current.next

            if descending:
                should_swap = current.xp < next_node.xp
            else:
                should_swap = current.xp > next_node.xp

            if should_swap:
                current.name, next_node.name = next_node.name, current.name
                current.category, next_node.category = (
                    next_node.category,
                    current.category
                )
                current.xp, next_node.xp = next_node.xp, current.xp
                current.completed, next_node.completed = (
                    next_node.completed,
                    current.completed
                )

            current = current.next

        end = current