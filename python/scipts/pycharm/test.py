command = ""
started = False
stopped = True
true = True
while true:
    command = input(">").lower()
    if command == "start":
        if started:
            print("the car is already started")
        else:
            started = True
            print("The car has started....")
    elif command == "stop":
        if stopped:
            print("the car is already stopped")
        else:
            stopped = True
            print("The car has stopped....")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        print("your have quit")
        break