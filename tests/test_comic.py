import unittest

from app.models.comic import *
from app.models.publisher import *

class TestComic(unittest.TestCase):
    def setUp(self):
        self.comic = Comic("Chew", "John Layman", "crime", 500, 20, 5, 2, False, "Image")

    def test_comic_has_name(self):
        comic = self.comic
        self.assertEqual("Chew", comic.name)

    def test_comic_has_author(self):
        comic = self.comic
        self.assertEqual("John Layman", comic.author)

    def test_comic_has_genre(self):
        comic = self.comic
        self.assertEqual("crime", comic.genre)

    def test_comic_has_wholesale_price(self):
        comic = self.comic
        self.assertEqual(500, comic.wholesale_price)

    def test_comic_has_markup(self):
        comic = self.comic
        self.assertEqual(20, comic.markup)

    def test_comic_has_stock_count(self):
        comic = self.comic
        self.assertEqual(5, comic.stock_count)

    def test_comic_has_min_count(self):
        comic = self.comic
        self.assertEqual(2, comic.min_count)

    def test_comic_has_out_of_stock(self):
        comic = self.comic
        self.assertEqual(False, comic.out_of_stock)

# I realised at this point I could have simplified the tests.
    
    def test_comic_has_publisher(self):
        # comic = self.comic
        self.assertEqual("Image", self.comic.publisher)