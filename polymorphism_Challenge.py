class Action:
    def action(self):
        print()

class Robot(Action):
    def action(self):
        print("Robot is performing a mechanical action 🤖")

class Human(Action):
    def action(self):
        print("Human is performing a thoughtful action 🧠")

class Alien(Action):
    def action(self):
        print("Alien is performing an intergalactic action 👽")

class Superhero(Action):
    def action(self):
        print("Superhero is performing a heroic action 🦸‍♂️")

# Function to demonstrate polymorphism
def demonstrate_actions(actions):
    for action in actions:
        action.action()

# Example usage
robot = Robot()
human = Human()
alien = Alien()
superhero = Superhero()

# List of action objects
action_list = [robot, human, alien, superhero]

# Demonstrate polymorphism
demonstrate_actions(action_list)
