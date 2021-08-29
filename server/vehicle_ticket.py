from server.vehicle import Vehicle
from server.error_handling import InvalidCommandException
from logger.logging_style import *
import traceback

    
def run_program(command):
    """
    the start point for calling each function based on user command

    Attribute:
        command -- user command for ticket system's operation
        InvalidCommandException -- raise exception for incorrect value of command
    """
    begin_status_update("task starting for the comand - {}".format(command))
    try:
        if 'Create_parking_lot' in command.keys():
            if len(command['Create_parking_lot'])<1000 and type(command['Create_parking_lot'])==str:
                global vehicle
                vehicle = Vehicle(int(command['Create_parking_lot']))
            else:
                raise InvalidCommandException(command)

        elif 'Park' in command.keys():
            if len(command['Park'])==13 and type(command['Park'])==str:
                parked_car = vehicle.book_slot(command['Park'], int(command['driver_age']))
                if parked_car != None:
                    print('Car with vehicle registration number {0} has been parked at slot number {1}'.format(parked_car["vehicle_number"], parked_car["slot_number"]+1))
                else:
                    print("No parked car matched with the query")
            else:
                raise InvalidCommandException(command)

        elif 'Slot_numbers_for_driver_of_age' in command.keys():
            if len(command['Slot_numbers_for_driver_of_age']) <= 2 and type(command['Slot_numbers_for_driver_of_age'])==str:
                slots = vehicle.get_slots(int(command['Slot_numbers_for_driver_of_age']))
                if slots != None:
                    print(",".join([str(slot) for slot in slots]))
                else:
                    print("No parked car matched with the query")
            else:
                raise InvalidCommandException(command)

        elif 'Slot_number_for_car_with_number' in command.keys():
            if len(command['Slot_number_for_car_with_number']) == 13 and type(command['Slot_number_for_car_with_number'])==str:
                slot_number = vehicle.get_slot_number_vehicle(command['Slot_number_for_car_with_number'])
                if slot_number!=None:
                    print(slot_number+1)
                else:
                    print("No parked car matched with the query")
            else:
                raise InvalidCommandException(command)

        elif 'Vehicle_registration_number_for_driver_of_age' in command.keys():
            vrn = command['Vehicle_registration_number_for_driver_of_age']
            if len(vrn) <= 2 and type(vrn)==str:
                slots = vehicle.get_slots(int(vrn), False)
                if slots != None:
                    print(",".join([str(slot) for slot in slots]))
                else:
                    print("No parked car matched with the query")
            else:
                raise InvalidCommandException(command)

        elif 'Leave':
            if len(command['Leave']) <= 4 and type(command['Leave'])==str:
                vacate = vehicle.vacate_slot(int(command['Leave'])-1)
                if vacate != None:
                    print('''Slot number {0} vacated, the car with vehicle registration number {1} left the space the driver of the car was age of {2}'''.format(vacate[0]+1, vacate[1], vacate[2]))
                else:
                    print("No parked car matched with the query")
            else:
                raise InvalidCommandException(command)
        else:
            pass
    except Exception as e:
        red_log("Caught exception while running for command - {}, error - {}".format(command, traceback.print_exc()))
    
    end_status_update("task ending for the comand - {}".format(command))
    return True