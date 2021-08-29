from server.parking import Parking
from logger.logging_style import green_log, status_update

class Vehicle(Parking):
    """
    Class for creating Vehicle instance, and inheriting the parking as a parent class

    Attribute:
        _total_slot -- for creating parking space
    calling super class constructor with given slot number
    """
    def __init__(self, total_slot):
        status_update("Created instance from vehicle")
        super().__init__(total_slot)

    def get_slot_number_vehicle(self, vehicle_number):
        """finding the slot number for the given vehicle registration number
           return: slot number if found else None 
        """
        slots_list = super().get_booked_slot()
        for slot_dict in slots_list:
            if slot_dict['vehicle_number'] == vehicle_number:
                green_log("the vehicle number {} parked in slot number {}".format(slot_dict['vehicle_number'], slot_dict['slot_number']))
                return slot_dict['slot_number'] 
        else:
            return None
    
    def book_slot(self, vehicle_number, driver_age):
        """booking slot for given vahicle details
           return: vehicle details in dictionary  
        """
        slot_number = super().get_slot_numbers()
        if slot_number != None:
            vehicle_parks={'vehicle_number':vehicle_number,
                          'driver_age':driver_age,
                          'slot_number':slot_number}
            super().booked_slot(vehicle_parks)
            green_log("Vehicle number {0} parked by age of driver {1} in slot number {2}".format(vehicle_number, driver_age, slot_number))
            # print('Car with vehicle registration number {0} has been parked at slot number {1}'.format(vehicle_number, slot_number+1))
            return vehicle_parks
        return None