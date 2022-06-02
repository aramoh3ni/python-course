class Privelage:
    def __init__(self, privelages):
        self.privelages = privelages

    def show_privileges(self):
        print("Admin Privelages")
        for privelage in self.privelages:
            print(f"- {privelage}")

