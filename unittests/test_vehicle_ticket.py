from unittest import TestCase
from unittest.mock import Mock
import sys

from server.vehicle_ticket import run_program
from app import check_command, get_commands

class TestVehicleTicket(TestCase):

    def test_run_program(self):
        command = {'Park': 'PB-01-HH-1234', 'driver_age': '21'}
        original = run_program(command)
        self.assertEqual(original, True)
