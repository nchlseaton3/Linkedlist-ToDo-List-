# Create task class

class Task:
    def __init__(self, name):
        self.name = name
        self.complete = "incomplete"  # or Boolean if you prefer (True/False)

    def __str__(self):
        return f"{self.name} - {self.complete.capitalize()}"
