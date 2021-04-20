class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.room_cost + room.expenses

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            monthly_cost = room.expenses + room.room_cost
            if room.budget >= monthly_cost:
                room.budget -= monthly_cost
                result += f"{room.family_name} paid {monthly_cost:.2f}$ and have {room.budget:.2f}$ left." + "\n"
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel." + "\n"
                self.rooms.remove(room)
        return result.rstrip()

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}" + "\n"

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$" + "\n"
            for i in range(len(room.children)):
                result += f"--- Child {i + 1} monthly cost: {room.children[i].cost * 30:.2f}$" + "\n"
            result += f"--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$" + "\n"

        return result.rstrip()
