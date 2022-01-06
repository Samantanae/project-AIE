from unittest import TestCase
from Personnage import Personnage

class TestPersonnage(TestCase):
    def test_av(self):
        self.run(Personnage())
