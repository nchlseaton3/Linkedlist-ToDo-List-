# Step 1 Create task class

class Task:
    def __init__(self, name):
        self.name = name
        self.complete = "incomplete"  # or Boolean if you prefer (True/False)

    def __str__(self):
        return f"{self.name} - {self.complete.capitalize()}"


# Step 2 Node and LinkedList

class Node:
    def __init__(self, data):
        self.data = data  # cargo
        self.next = None  # link to next node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    # Append node (using tail for efficiency)
    def append_with_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # Traverse and print each node's data
    def traverse(self):
        current = self.head
        if self.is_empty():
            print("Sorry, list is empty.")
            return
        while current:
            print(current.data)
            current = current.next

    # Get data at a specific position (1-indexed)
    def get_at_position(self, position):
        if self.is_empty() or position < 1:
            return None
        current = self.head
        counter = 1
        while current:
            if counter == position:
                return current.data
            current = current.next
            counter += 1
        return None

    # Delete method
    def delete_at_position(self, position):
        if self.is_empty() or position < 1:
            return False

        # Delete head
        if position == 1:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        current = self.head
        counter = 1
        while current.next and counter < position - 1:
            current = current.next
            counter += 1

        # If next node exists, unlink it
        if current.next:
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            return True
        return False

    # Bonus: get all items as a list (used for view_all_tasks)
    def as_list(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

# Step 3 ToDo List

class ToDoList:
    def __init__(self, list_name="My Tasks"):
        self.list_name = list_name
        self.tasks = LinkedList()  # Linked list to store Task objects

    def add_task(self, task_name):
        """Add a new Task object to the list"""
        new_task = Task(task_name)
        self.tasks.append_with_tail(new_task)
        print(f"Task added: {task_name}")

    def complete_task(self, position):
        """Mark a task as complete using its position"""
        task = self.tasks.get_at_position(position)
        if task:
            task.complete = "complete"
            print(f"Task {position} marked complete: {task.name}")
            return True
        else:
            print("Invalid task position.")
            return False

    def remove_task(self, position):
        """Remove a task at a given position"""
        success = self.tasks.delete_at_position(position)
        if success:
            print(f"Task {position} removed successfully.")
            return True
        else:
            print("Invalid task position.")
            return False

    def view_all_tasks(self):
        """Display all tasks in the to-do list"""
        print(f"\n{self.list_name}")
        print("=" * len(self.list_name))
        all_tasks = self.tasks.as_list()
        if not all_tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(all_tasks, start=1):
            print(f"{i}. {task}")

# Step 4 Test Function 

def test_todo_list():
    """Verify ToDoList functionality"""
    print("=== Testing To-Do List Implementation ===\n")

    todo = ToDoList("School Tasks")

    print("1. Adding tasks...")
    todo.add_task("Study for math exam")
    todo.add_task("Write history essay")
    todo.add_task("Submit science project")
    todo.add_task("Read chapter 5")

    print("\n2. Viewing all tasks:")
    todo.view_all_tasks()

    print("\n3. Completing some tasks...")
    todo.complete_task(2)
    todo.complete_task(4)

    print("\n4. Viewing tasks after completion:")
    todo.view_all_tasks()

    print("\n5. Removing a task...")
    todo.remove_task(3)
    todo.view_all_tasks()

    print("\n6. Testing edge cases...")
    print("Trying to complete invalid position:")
    print(f"Result: {todo.complete_task(10)}")
    print("Trying to remove invalid position:")
    print(f"Result: {todo.remove_task(0)}")

    print("\n=== Test completed! ===")


# Step 5 Run test 

 