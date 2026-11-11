def get_sensor_data():
    temp = int(input("Enter temperature: "))
    light = bool(int(input("Is there light in the room (1=yes, 0=no): ")))
    motion = bool(int(input("Is there motion (1=yes, 0=no): ")))
    smoke = bool(int(input("Smoke detected (1=yes, 0=no): ")))
    occup = bool(int(input("Is the room occupied (1=yes, 0=no): ")))

    return temp, motion, smoke, occup, light

def smart_home_agent():

    while True:

        temp, motion, smoke, occup, light = get_sensor_data()

        if temp > 30:
            print("Temperature over 30 --- AC TURNED ON\n")
        else:
            print("Temperature below 30 --- AC TURNED OFF\n")

        if motion and not light:
            print("Motion and darkness detected --- LIGHT TURNED ON\n")
        elif motion and light:
            print("No darkness detected --- LIGHT TURNED OFF\n")
        elif not motion and light:
            print("No motion and light detected --- LIGHT TURNED OFF\n")
        else:
            print("Darkness detected --- LIGHT TURNED ON\n")

        if smoke:
            print("Smoke detected --- FIRE ALARM TURNED ON\n")
        else:
            print("Smoke not detected --- FIRE ALARM TURNED OFF\n")

        if occup:
            print("Room occupied --- DOOR UNLOCKED\n")
        else:
            print("Room not occupied --- DOOR LOCKED\n")

        choice = input("Do you want to continue? (yes/no): ")

        if choice.lower() == "no":
            print("Smart Home Agent Exited Successfully!")
            break

smart_home_agent()
