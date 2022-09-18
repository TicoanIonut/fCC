command = ""
started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print('car is already started')
        else:
            started = True
            print("car starts")
    elif command == "stop":
        if not started:
            print('car is already stopped')
        else:
            started = False
            print("car stopped")
    elif command == 'help':
        print("""
start - start car
stop - stop car
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("I don't understand what you are saying")
