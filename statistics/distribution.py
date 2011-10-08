"""Objects representing distributions of data

A Histogram is a map from values to frequencies. Values can 
be any hashable type; frequencies are integer counters.

Kudos to Allen B. Downey, author of Think Stats 
(http://www.thinkstats.com)
for lots and lots of inspiration!
"""

import logging, operator

class Histogram(object):
    """Represents a histogram, which is a map from values to frequencies.

    Values can be any hashable type; frequencies are integer counters.
    """
    def __init__(self, values=None, name=None):
        self.data = {}
        self.name = name
        if values:
            for v in values:
                self.data[v] = self.data.get(v, 0) + 1
                
            if name:
                logging.info('Histogram: Created %s with %s items.' % (self.name, len(self.data)))
            else:
                logging.info('Histogram: Created with %s items.' % len(self.data))

        else:
            logging.warning('Histogram: Initialized without any values.')
        
    def frequency(self, value):
        frequency = self.data.get(value, 0)
        return frequency

    def values(self, sort=False):
        values = sort and sorted(self.data.keys()) or self.data.keys()
        return values

    def items(self, sort=False):
        items = sort and sorted(self.data.items()) or self.data.items()
        return items

    def mode(self, frequency=False):
        mode = max(self.data.iteritems(), key=operator.itemgetter(1))
        mode = frequency and mode or mode[0]
        return mode

    def all_modes(self, frequency=False, descending=False):
        all_modes = sorted(self.data.iteritems(), key=operator.itemgetter(1), reverse=descending)
        all_modes = frequency and all_modes or [mode[0] for mode in all_modes]
        return all_modes

    def render(self):
        return zip(*self.items(True))
        


