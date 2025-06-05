try:
    age = int(input("How old are you? "))
except ValueError:
    print("You didn't enter a vaild age.")
else:
    print("No exceptions were given, continue.")

        
