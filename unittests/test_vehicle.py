from unittest import TestCase
from unittest.mock import Mock

from server.vehicle import Vehicle
from server.parking import Parking


class TestVehicle(TestCase):
    
    def test_get_slot_number_vehicle(self):
        service = Vehicle('6')
        service.book_slot('PB-01-HH-1234', '26')
        slot_number = service.get_slot_number_vehicle('PB-01-HH-1234')
        self.assertEqual(slot_number, 0)


    def test_book_slot(self):
        service = Vehicle('6')
        original = service.book_slot('PB-01-HH-1234', '26')
        expected={'vehicle_number':'PB-01-HH-1234',
                          'driver_age':'26',
                          'slot_number':0}
        self.assertEqual(original, expected)