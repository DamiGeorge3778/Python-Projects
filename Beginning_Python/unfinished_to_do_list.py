editing = True
list = []
def welcome():
    print("Welcome this is your to-do list!")
welcome()
while editing:
    question = input("Would you like to add or remove anything to your to-do list? ").lower()
    if question == "a" or question == "add":
        add = input("What would you like to add to your to-do list? ")
        list.append(add)
        print("This is your to-do list so far!")
        print(list)
        # START CREATING REMOVE FUNCTION HERE \/\/\/\/\/\/\/\/\/\/