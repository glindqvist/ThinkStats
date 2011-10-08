import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

import survey

from statistics.distribution import Histogram
from util.functions import *

# Set up data to work with
table = survey.Pregnancies()
table.ReadRecords('data')

gestation_firstbabies = [rec.prglength for rec in table.records 
                         if rec.birthord == 1 and rec.outcome == 1]

gestation_other = [rec.prglength for rec in table.records    
                   if rec.birthord != 1 and rec.outcome == 1]

logging.info('Imported data for:')
logging.info('   Gestation, first baby (%s entries)' % len(gestation_firstbabies))
logging.info('   Gestation, second or later baby (%s entries)' % len(gestation_other))

hist_gestation_firstbabies = Histogram(gestation_firstbabies, 
                                       name='Gestation for first baby')
hist_gestation_other = Histogram(gestation_other)

logging.info(hist_gestation_firstbabies.all_modes(frequency=True))




