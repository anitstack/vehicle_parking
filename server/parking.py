from logger.logging_style import *
import traceback

class Parking:
    """
    Class for creating parking space, and updating slots based on user command

    Attribute:
        _total_slot -- slots for create parking space
        _available_slot -- list with total_slot size
        _booked_slots -- empty list, for storing data for each vehicle
    """
    def __init__(self, total_slot):
        self._total_slot = total_slot
        self._available_slots = [None]*int(self._total_slot)
        self._booked_slots = []
        green_log("Parking created for slots {}".format(int(total_slot)))
        print("Created parking of {} slots".format(total_slot))
        
    def get_booked_slot(self):
        """return booked slots with updated value"""
        return self._booked_slots
    
    def get_total_slot(self):
        """return total number of slots"""
        return self._total_slot
    
    def get_available_slots(self):
        """return available slots for the parking"""
        return self._available_slots

    def get_slot_numbers(self):
        """finding the nearest available slot,
        return: slot number if found else None"""
        if None not in self._available_slots:
            return None
        for num in range(len(self._available_slots)):
            if self._available_slots[num]==None:
                slot_number = num
                break
        self._available_slots[slot_number] = slot_number
        yellow_log("Nearest available slot is {}".format(slot_number+1))
        return slot_number
    
    def vacate_slot(self, slot_number):
        """update the instance variable for vahicle which is existing,
            return: slot number, vehicle registration number and driver age
        """
        for num in range(len(self._booked_slots)):
            if self._booked_slots[num]['slot_number']==slot_number:
                resg_number = self._booked_slots[num]['vehicle_number']
                driver_age = self._booked_slots[num]['driver_age']
                del self._booked_slots[num]
                self._available_slots[slot_number] = None
                green_log("Slot number {0} vacated, parked vehicle number {1} and driver age {2}".format(slot_number+1, resg_number, driver_age))
                return slot_number, resg_number, driver_age
        return None
    
    def booked_slot(self, vehicle_parks):
        """updating the instance variable _booked_slots for new vahicle
           return: total booked slots in list of dict
        """
        self._booked_slots.append(vehicle_parks)
        return self._booked_slots
        
    def get_slots(self, user_input, slot_number=True):
        """finding the slot number / vehicle number based on user input
           return: slot number / vehicle number if found else None
        """
        slots = []
        for slot in self._booked_slots:
            if slot_number:
                if slot['driver_age']==user_input:
                    slots.append(slot['slot_number']+1)
            else:
                if slot['driver_age']==user_input:
                    slots.append(slot['vehicle_number']+1)
        if slots:
            green_log("Find available slots {0} for - {1}".format(slots, user_input))
            return slots
        return None