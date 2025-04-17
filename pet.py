class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at middle value
        self.energy = 5  # Starting at middle value
        self.happiness = 5  # Starting at middle value
        self.tricks = []  # List to store tricks the pet has learned
    
    def eat(self):
        """Feed the pet to reduce hunger and increase happiness"""
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger by 3, but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1, but not above 10
        return f"{self.name} has been fed! Hunger decreased to {self.hunger}."
    
    def sleep(self):
        """Let the pet sleep to increase energy"""
        self.energy = min(10, self.energy + 5)  # Increase energy by 5, but not above 10
        return f"{self.name} had a good sleep! Energy increased to {self.energy}."
    
    def play(self):
        """Play with the pet to increase happiness, decrease energy, and increase hunger"""
        if self.energy < 2:
            return f"{self.name} is too tired to play! Energy level: {self.energy}"
        
        self.energy = max(0, self.energy - 2)  # Decrease energy by 2, but not below 0
        self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2, but not above 10
        self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1, but not above 10
        return f"{self.name} had fun playing! Happiness: {self.happiness}, Energy: {self.energy}, Hunger: {self.hunger}"
    
    def get_status(self):
        """Print the current state of the pet"""
        status_message = f"\n--- {self.name}'s Status ---\n"
        status_message += f"Hunger: {self.hunger}/10 ({'Very hungry' if self.hunger > 7 else 'Hungry' if self.hunger > 4 else 'Content' if self.hunger > 1 else 'Full'})\n"
        status_message += f"Energy: {self.energy}/10 ({'Fully rested' if self.energy > 7 else 'Rested' if self.energy > 4 else 'Tired' if self.energy > 1 else 'Exhausted'})\n"
        status_message += f"Happiness: {self.happiness}/10 ({'Ecstatic' if self.happiness > 7 else 'Happy' if self.happiness > 4 else 'Neutral' if self.happiness > 1 else 'Sad'})\n"
        
        # Add a general status message
        if self.hunger > 7:
            status_message += f"{self.name} needs food urgently!\n"
        if self.energy < 3:
            status_message += f"{self.name} needs rest!\n"
        if self.happiness < 3:
            status_message += f"{self.name} needs attention and playtime!\n"
        if all(stat > 6 for stat in [self.energy, self.happiness]) and self.hunger < 4:
            status_message += f"{self.name} is feeling great!\n"
            
        return status_message
    
    def train(self, trick):
        """Teach a new trick to the pet"""
        if trick in self.tricks:
            return f"{self.name} already knows how to {trick}!"
        
        # Training requires energy and increases hunger
        if self.energy < 3:
            return f"{self.name} is too tired to learn new tricks right now."
        
        self.energy = max(0, self.energy - 1)  # Training takes energy
        self.hunger = min(10, self.hunger + 1)  # Training makes pet hungry
        self.tricks.append(trick)
        return f"{self.name} has learned to {trick}! Total tricks: {len(self.tricks)}"
    
    def show_tricks(self):
        """Display all tricks the pet has learned"""
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet."
        
        tricks_message = f"\n--- {self.name}'s Tricks ---\n"
        for i, trick in enumerate(self.tricks, 1):
            tricks_message += f"{i}. {trick}\n"
        return tricks_message