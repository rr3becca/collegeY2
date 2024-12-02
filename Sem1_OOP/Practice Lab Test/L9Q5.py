class Attendees:
    def __init__(self, total=0):
        self.total = total

    def add_people(self, peopleAdded):
        self.total += peopleAdded
        print(f"Welcome, there are {self.total} people in the meeting!")

    def remove_people(self, peopleRemoved):
        if self.total <= 0:
            print("Invalid")
            return

        self.total -= peopleRemoved
        print(f"Welcome, there are {self.total} people in the meeting!")

meeting = Attendees()
meeting.add_people(10)
meeting.add_people(10)
meeting.add_people(35)
meeting.remove_people(50)


