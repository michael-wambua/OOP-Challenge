
from pet import Pet

def main():
    # Get pet name from user
    pet_name = input("What would you like to name your pet? ")
    
    # Create a new pet
    my_pet = Pet(pet_name)
    print(f"\nCongratulations! You've adopted {pet_name}!")
    print(my_pet.get_status())
    
    # Main interaction loop
    while True:
        print("\nWhat would you like to do with your pet?")
        print("1. Feed")
        print("2. Let sleep")
        print("3. Play")
        print("4. Check status")
        print("5. Train a new trick")
        print("6. Show tricks")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            print(my_pet.eat())
        elif choice == '2':
            print(my_pet.sleep())
        elif choice == '3':
            print(my_pet.play())
        elif choice == '4':
            print(my_pet.get_status())
        elif choice == '5':
            trick = input("What trick would you like to teach? ")
            print(my_pet.train(trick))
        elif choice == '6':
            print(my_pet.show_tricks())
        elif choice == '7':
            print(f"\nGoodbye! Take care of {pet_name}!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()