import webbrowser
question = input('Would you like to open a new tab? y/n ')
if question == "y":
    print("Execution Completed")
    webbrowser.open("http://google.com")
if question == "n":
    print("Ok")