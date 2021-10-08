## ParkingLot
Design a parking lot using Python

## Dependencies
You just need Python. The code is compatible with Python3. Visit the link https://www.python.org/downloads/ to install Python.

`python -m venv .venv` - this command create virtual envirement for project

## run
`python ParkingLot.py` -run the file in command. follow function of command.

## Description
we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy approach while being parked in the slots.

ParkingLot.py script defines the following functions -

1. `TYPE A ` - Given n number of slots, create a parking lot
2. `TYPE B` - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".
3. `TYPE S` - Prints the slot number, registration number and color of the parked vehicles.
4. `TYPE E` - Removes vehicle from slot number x
5. `TYPE C` - Get the registration number by type color of car
6. `TYPE F` - Get the slots number by type registration number
7. `TYPE G` - Get the slots number by type name of  car color

Vehicle.py is a separate class where we can define the type of vehicles that can be parked. As of now, it only contains class `Car`







