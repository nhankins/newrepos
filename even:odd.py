

#Author: Nick Hankins
#Purpose: Make even/odd program more user friendly


def display_menu():
    print("Welcome to the Even or Odd Number Determiner!")


def formula():
    user_input = int(input("Enter a number: "))

    if (user_input % 2) == 0:
        print("{0} is an even number".format(user_input))
    else:
        print("{0} is an odd number".format(user_input))
    
    
def main():
    
    display_menu()
    
    command = "yes"
    
    while (command.lower() == "yes"):
        formula()
        
        
        command = input("Do you want to enter another number?(yes/no):")
        print()
        
    print("Okay Goodbye!")



if __name__ == "__main__":
    main()


