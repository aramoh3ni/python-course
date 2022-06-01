class Rasturant:
    """Represent a resturnt information"""
    def __init__(self, name, cuisine_type):
        """Inisiazting name and cuisine type attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """return dic and describe resturant info..."""
        return {
            "name": self.name,
            "cuisine_type": self.cuisine_type,
            "number_served": self.number_served
        }

    def open_restaurant(self) -> str:
        """retrun string and print mesage"""
        print(f"Greeting for Everyone, {self.name} is [OPEN]")

    def set_number_served(self, number): 
        """Set the total guest served."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't not roll back.")