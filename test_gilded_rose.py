# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
    def test_agedBrie_quality(self):
        items = [Item("Aged Brie", 2, 49)]
        gilded_rose = GildedRose(items)
        for _ in range(2):
            gilded_rose.update_quality()
        #fails due to "The Quality of an item is never more than 50"
        #the Aged Brie's quality cannot pass 50 even if its sell_in is 2
        self.assertGreater(items[0].quality, 50)
    
    def test_conjured_quality(self):
        items = [Item("random", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        #fails due to "once the sell by date has passed, quality degrades twice as fast"
        #so when sell_in is -1, when we call update_quality() once, the quality will degrade to 0 instead of 1
        self.assertGreater(items[0].quality, 0)

    def test_backStageAccess_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        for _ in range(10):
            gilded_rose.update_quality()
        #fails due to ""Sulfuras" is a legendary item and as such its Quality is 80 and it never alters"
        #so even if we run update_quality 10 times, its quality will remain 80
        self.assertNotEqual(items[0].quality, 80)

if __name__ == '__main__':
    unittest.main()
