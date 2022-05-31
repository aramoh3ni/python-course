class Rasturant:
    """Represent a resturnt information"""
    def __init__(self, name, cuisine_type):
        """Inisiazting name and cuisine type attributes"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """return dic and describe resturant info..."""
        return {
            "name": self.name,
            "cuisine_type": self.cuisine_type
        }

    def open_restaurant(self) -> str:
        """retrun string and print mesage"""
        print(f"Greeting for Everyone, {self.name} is [OPEN]")