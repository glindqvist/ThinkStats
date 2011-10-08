import math

def mean(data):
    mean = float(sum(data)) / len(data) 
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
