#program a car simulation
command = ""
started = False
while True:
    command = str(input(">").lower())
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""") 
    elif command == "start":
        if started == False:
            print("car started... ready to gooo!")
            started = True
        else:
            print("the car is already started")

    elif command == "stop":
        if started == True:
            print("car has stopped")
            started = False
        else:
            print("the car is already stopped")
    elif command == "quit":
        break
    else:
        print("I dont understand that...")


    

    









