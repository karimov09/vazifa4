class Home:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Window(Home):
    def __init__(self, name, address, window_type):
        super().__init__(name, address)
        self.window_type = window_type
    
    def open_window(self):
        print(f"{self.name}'s {self.window_type} window ochish.")

class Door(Home):
    def __init__(self, name, address, door_material):
        super().__init__(name, address)
        self.door_material = door_material
    
    def close_door(self):
        print(f"{self.name}'s {self.door_material} door yopish.")

class Room(Home):
    def __init__(self, name, address, room_type):
        super().__init__(name, address)
        self.room_type = room_type
    
    def describe_room(self):
        print(f"{self.room_type}{self.address}")

window = Window("John", "123 Main St", "casement")
door = Door("Alice", "456 Elm St", "wooden")
room = Room("Bob", "789 Oak St", "living")

window.open_window()
door.close_door()
room.describe_room()
