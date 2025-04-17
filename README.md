# 🐶 Python OOP Challenge: Digital Pet

## Overview
This project implements a virtual pet simulation using Object-Oriented Programming concepts in Python. It's a fun, interactive way to practice working with classes, attributes, methods, and constructors in Python. The digital pet has various needs (hunger, energy, happiness) that you must manage through different interactions.

## Features
- Create and name your own digital pet
- Feed your pet to reduce hunger and increase happiness
- Let your pet sleep to restore energy
- Play with your pet to boost happiness (at the cost of energy and increased hunger)
- Train your pet to learn new tricks
- Interactive command-line interface for pet management

## Requirements
- Python 3.6 or higher

## Installation
1. Clone this repository:
```bash
git clone https://github.com/Evans-mutuku/OOP-Challenge.git
cd OOP-Challenge
```

2. No external dependencies are required to run this project.

## Usage
Run the main script to start interacting with your digital pet:
```bash
python main.py
```

Follow the on-screen prompts to:
- Name your pet
- Choose actions (feed, sleep, play, train)
- Check your pet's status
- View the tricks your pet has learned

## Code Structure
- `pet.py`: Contains the `Pet` class with all attributes and methods
- `main.py`: The interactive interface to interact with your pet

## Pet Class Details

### Attributes
- `name`: Your pet's name
- `hunger`: Integer from 0 (full) to 10 (very hungry)
- `energy`: Integer from 0 (tired) to 10 (fully rested)
- `happiness`: Integer from 0 (sad) to 10 (ecstatic)
- `tricks`: List of tricks your pet has learned

### Methods
- `eat()`: Reduces hunger by 3 points (not below 0), increases happiness by 1
- `sleep()`: Increases energy by 5 points (not above 10)
- `play()`: Decreases energy by 2, increases happiness by 2, increases hunger by 1
- `get_status()`: Returns a detailed status report of your pet
- `train(trick)`: Teaches your pet a new trick, using some energy and increasing hunger
- `show_tricks()`: Displays all tricks your pet has learned

## Example Interaction
```
What would you like to name your pet? Bosco

Congratulations! You've adopted Bosco!

--- Bosco's Status ---
Hunger: 5/10 (Hungry)
Energy: 5/10 (Rested)
Happiness: 5/10 (Happy)

What would you like to do with your pet?
1. Feed
2. Let sleep
3. Play
4. Check status
5. Train a new trick
6. Show tricks
7. Exit

Enter your choice (1-7): 5
What trick would you like to teach? Roll over
Buddy has learned to Roll over! Total tricks: 1
```

## Future Enhancements
- Add a graphical user interface (GUI)
- Include more pet attributes like age, size, or specific species characteristics
- Implement time-based changes to pet states
- Add more complex interactions and mini-games
- Support saving/loading pets to continue playing later

## Challenge Source
This project was created as part of the Python OOP Challenge: https://github.com/Evans-mutuku/OOP-Challenge

## License
[MIT License](LICENSE)