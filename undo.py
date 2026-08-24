class UndoNode:
    def __init__(self, action):
        self.action = action
        self.next = None


class UndoStack:
    def __init__(self):
        self.top = None

    def push(self, action):
        new_node = UndoNode(action)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        action = self.top.action
        self.top = self.top.next

        return action

    def peek(self):
        if self.top is None:
            return None

        return self.top.action

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.top is None:
            print("Undo stack is empty.")
            return

        current = self.top

        while current is not None:
            print(current.action)
            current = current.next