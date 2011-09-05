import math

from operator import itemgetter

import survey

def mean(data):
    numerator = float(sum(data))
    denominator = float(len(data))
    mean = numerator / denominator

    return mean

def variance(data):
    m = mean(data)
    deviation_from_mean_squared = [(x - m)**2 for x in data]
    variance = float(sum(deviation_from_mean_squared)) / len(data)

    return variance

def std_dev(data):
    v = variance(data)
    std_dev = math.sqrt(v)

    return std_dev

def histogram(data):
    histogram = {}
    for d in data: 
        histogram[d] = histogram.get(d, 0) + 1

    return histogram

def probability_mass_function(data):
    data = isinstance(data, list) and histogram(data) or data
    n = float(len(data))
    pmf = {}
    for x, freq in data.iteritems():
        pmf[x] = freq / n

    return pmf

def mode(data):
    data = isinstance(data, list) and histogram(data) or data
    max = -1
    key = -1
    for k, v in data.iteritems():
        if v > max:
            max = v
            key = k

    return (key, max)

def main():
    table = survey.Pregnancies()
    table.ReadRecords('data')

    live_births = [rec.outcome for rec in table.records if rec.outcome == 1]
    print "# of live births %s:" % sum(live_births)

    live_births_by_birthord = {'first': {},
                               'second_or_more': {}}

    for rec in table.records:
        if rec.outcome == 1:
            birthord = (rec.birthord == 1) and 'first' or 'second_or_more'
            live_births_by_birthord[birthord].setdefault('prglength', []).append(rec.prglength)

    for key, values in live_births_by_birthord.iteritems():
        print "\nCategory: %s" % key
        for value in values.keys():
            data = values.get(value)
            print "\tValue: %s" % value
            print "\t\tNumber of live birth: %s" % len(data)
            print "\t\tAvg. length of pregnancy: %s" % mean(data)
            print "\t\tStd.dev of pregnancy: %s" % std_dev(data)

            h = histogram(data)
            pmf = probability_mass_function(h)
            m = mode(h)

            print "\t\tHistogram:"
            #for x, freq in sorted(h.iteritems()):
            #    print "\t\t%s: %s (%s)" % (x, freq, pmf.get(x))
            print "\t\tMode: week %s with %s births (%s)" % (m[0], m[1], pmf[m[0]])

if __name__ == '__main__':
    main()
