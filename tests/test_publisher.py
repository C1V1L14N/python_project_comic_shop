import unittest

from app.models.publisher import *
# from app.models.comic import *

class TestPublisher(unittest.TestCase):

    def test_publisher_has_name(self):
        self.publisher = Publisher("Image")
        self.assertEqual("Image", self.publisher.name)