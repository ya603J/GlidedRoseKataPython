# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class QualityUpdater:
    def update_quality(self, item):
        if item.sell_in < 0:
            item.quality -= 2

class AgedBrieUpdater(QualityUpdater):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

class RegularUpdater(QualityUpdater):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2

class ConjuredUpdater(QualityUpdater):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 2
        item.sell_in -= 1
        

class SulfurasUpdater(QualityUpdater):
    def update_quality(self, item):
        pass

class BackstagePassUpdater(QualityUpdater):
    def update_quality(self, item):
        if item.sell_in >= 0:
            if item.quality < 50:
                item.quality += 1
                if item.sell_in < 6 and item.quality < 50:
                                item.quality += 3
                elif item.sell_in < 11 and item.quality < 50:
                    item.quality += 2
            item.sell_in -= 1
        else:
            item.quality = 0

class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def determine(self, item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater()
        else:
            return RegularUpdater()

    def update_quality(self):
        for item in self.items:
            product = self.determine(item)
            product.update_quality(item)

