import sys
import os
from server.vehicle_ticket import run_program
from logger.logging_style import *
from server.error_handling import CommandNotFoundException


command_suggests = [
        "Create_parking_lot 6",
        "Park KA-01-HH-1234 driver_age 21",
        "Slot_numbers_for_driver_of_age 21",
        "Slot_number_for_car_with_number PB-01-HH-1234",
        "Leave 2",
        "Vehicle_registration_number_for_driver_of_age 18"
        ]

def check_command():
    """creating list of keys for each command"""
    command_list = []
    for line in command_suggests:
        input_command = line.strip().split()
        command_list.append(dict(zip(input_command[::2], input_command[1::2])).keys())
    return command_list


def get_commands(filename):
    """serialize the command as key-value pair,
       checking command from command_suggests variable

       return: list of dict for all command
       CommandNotFoundException: raising exception for invalid command
    """
    command_list = []
    with open(filename, 'r') as fp:
        for line in fp:
            input_command = line.strip().split()
            command = dict(zip(input_command[::2], input_command[1::2]))
            if command.keys() in check_command():
                command_list.append(command)
            else:
                red_log("The {} command not found in list".format(line))
                raise CommandNotFoundException(line)
    yellow_log("Available commands in the file are - {0}".format(command_list))
    return command_list
    

if __name__=='__main__':
    """main method of the application"""
    if sys.argv[1]=="--help":
        print("Please check your command in give list \n")
        print(" \n".join(command_suggests))
    else:
        status_update("Parking System starting for the filename - {}".format(sys.argv[0]))
        command_list = get_commands(sys.argv[1])
        flag = False
        for num in range(len(command_list)):
            if 'Create_parking_lot' in command_list[num].keys():
                run_program(command_list[num])
                flag = True
                del command_list[num]
                break
        if not flag:
            raise Exception("Parking not existing, please enter command for create parking")        
        else:
            for command in command_list:
                run_program(command)