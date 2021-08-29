from unittest import TestCase
from unittest.mock import Mock

from server.parking import Parking
from server.vehicle import Vehicle


class TestParking(TestCase):

    def test_get_booked_slot(self):
        service = Vehicle('6')
        service.book_slot('PB-01-HH-1234', '26')
        original = service.get_booked_slot()
        expected=[{'vehicle_number':'PB-01-HH-1234',
                          'driver_age':'26',
                          'slot_number':0}]
        self.assertEqual(original, expected)

    def test_get_available_slots(self):
        service = Vehicle('3')
        service.book_slot('PB-01-HH-1234', '26')
        original = service.get_available_slots()
        self.assertEqual(original, [0, None, None])

    def test_get_slot_numbers(self):
        service = Vehicle('3')
        service.book_slot('PB-01-HH-1234', '26')
        original = service.get_slot_numbers()
        self.assertEqual(original, 1)

    def test_vacate_slot(self):
        service = Vehicle('3')
        service.book_slot('PB-01-HH-1234', '26')
        original = service.vacate_slot('1')
        self.assertEqual(original, None)

    def test_booked_slot(self):
        service = Vehicle('3')
        # service.book_slot('PB-01-HH-1234', '26')
        vehicle_parks = {'vehicle_number':'PB-01-HH-1234',
                          'driver_age':'26',
                          'slot_number':0}
        original = service.booked_slot(vehicle_parks)
        expected=[vehicle_parks]
        self.assertEqual(original, expected)

    def test_get_slots_for_vehicle(self):
        service = Vehicle('3')
        service.book_slot('PB-01-HH-1234', '26')
        original = service.get_slots('26', True)
        self.assertEqual(original, [1])

    def test_get_slots_for_driver_age(self):
        service = Vehicle('3')
        service.book_slot('PB-01-HH-1234', '26')
        original = service.get_slots('26', True)
        self.assertEqual(original, [1])