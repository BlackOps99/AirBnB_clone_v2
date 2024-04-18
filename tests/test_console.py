#!/usr/bin/python3
import unittest
from console import HBNBCommand
from io import StringIO

class TestConsole(unittest.TestCase):
    """test the Console passed on the storage type."""
    def test_console_create_user(self):
        """Tests the create."""
        with unittest.mock.patch('sys.stdout', new=StringIO()) as sto:
            hmcom = HBNBCommand()
            hmcom.onecmd('create User name="mostafa" age=24 phone=01157')  
            mdl_id = sto.getvalue().strip()
            self.assertIn('User.{}'.format(mdl_id), storage.all().keys())

            hmcom.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'mostafa'", sto.getvalue().strip())
            self.assertIn("'age': 24", sto.getvalue().strip())
            self.assertIn("'phone': 01157", sto.getvalue().strip())
    
    def test_console_create_city(self):
        """Tests the create."""
        with unittest.mock.patch('sys.stdout', new=StringIO()) as sto:
            cons = HBNBCommand()
            cons.onecmd('create City name="Cario"')
            mdl_id = sto.getvalue().strip()

            self.assertIn('City.{}'.format(mdl_id), storage.all().keys())
            cons.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Cario'", sto.getvalue().strip())