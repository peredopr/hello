i = ""
started = False
while True:
    i = input("> ").lower()
    if i == "start":
        if started:
            print("Car has already started.")
        else:
            started = True
            print("Car started.")
    elif i == "stop":
        if not started:
            print("Car is already stopped.")
        elif started:
            started = False
            print("Car stopped.")
    elif i == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif i == "quit":
        break
    else:
        print("Sorry, I don't understand that.")