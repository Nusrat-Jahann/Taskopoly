class QueueNode:
    def __init__(self, quest):
        self.quest = quest
        self.next = None


class QuestQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, quest):
        new_node = QueueNode(quest)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        quest = self.front.quest
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return quest

    def peek(self):
        if self.front is None:
            return None

        return self.front.quest

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return

        current = self.front

        while current is not None:
            print(current.quest)
            current = current.next