

def main():

    print("Welcome to the C learning framework!        \n")

    print("Would you like to start from the beginning? \n \
          Or perhaps an exact level?                   \n")
           
    print("1) From the beginning                       \n \
           2) Level 1: Operations                      \n \
           3) Level 2:  Memory functions               \n \
           4)                                          \n \
           5)                                          \n")
    
    answer = int(raw_input("Answer: "))
    
    if answer == 1:
        from modules import operators
    elif answer == 2:
        from modules import memory
    elif answer == 3:
        
    elif answer == 4:
        
    elif answer == 5:
    
    else:
        print("Option not recognized")


if __name__ == "__main__":
    main()
