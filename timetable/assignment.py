class Assignment:

    def __init__(self, klass, room, teacher):
        self.klass = klass
        self.room = room
        self.teacher = teacher

    def __str__(self):
        return f"{self.klass} {self.room} {self.teacher}"

