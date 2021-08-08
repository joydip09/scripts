command = ''
started = False
stopped = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Engine starting in 3,2,1...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game 
        """)
    elif command == "quit":
        break
    else:
        print("Get outta here!")

