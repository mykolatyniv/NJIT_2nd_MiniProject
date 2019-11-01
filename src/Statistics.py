def population_mean(a, b, c):
    d = (a + b) / c
    return d

def median(a, b, c, d, e, f):
    med_n = [a, b, c, d, e, f]
    n = len(med_n)
    med_n.sort()
    if n % 2 == 0:
        median1 = med_n[n // 2]
        median2 = med_n[n // 2 - 1]
        med = (median1 + median2) / 2
    else:
        mod = med_n[n // 2]
    return f

def mode(a, b):
    c= a + b
    return c

def population_standard_deviation(a, b):
    c= a + b
    return c

def variance_of_population_proportion(a, b):
    c= a + b
    return c

def z_score(a, b):
    c= a + b
    return c

def standardized_score(a, b):
    c= a + b
    return c

def correlation_coefficient(a, b):
    c= a + b
    return c

def confidence_interval(a, b):
    c= a + b
    return c

def population_variance(a, b):
    c= a + b
    return c

def p_value(a, b):
    c= a + b
    return c

def proportion(a, b):
    c= a + b
    return c

def sample_mean(a, b):
    c= a + b
    return c

def sample_standard_deviation(a, b):
    c= a + b
    return c

def variance_of_sample_proportion(a, b):
    c= a + b
    return c

class Statistics:
    result = 0

    def __init__(self):
        pass

    def mean(self, a, b, c):
        self.result = population_mean(a, b, c)
        return self.result

    def med(self, a, b, c, d, e, f):
        self.result = median(a, b, c, d, e, f)
        return self.result

    def mod(self, a, b):
        self.result = mode(a, b)
        return self.result

    def population(self, a, b):
        self.result = population_standard_deviation(a, b)
        return self.result

    def variance(self, a, b):
        self.result = variance_of_population_proportion(a, b)
        return self.result

    def score(self, a, b):
        self.result = z_score(a, b)
        return self.result

    def standardized(self, a, b):
        self.result = standardized_score(a, b)
        return self.result

    def population1(self, a, b):
        self.result = correlation_coefficient(a, b)
        return self.result

    def confidence(self, a, b):
        self.result = confidence_interval(a, b)
        return self.result

    def variance(self, a, b):
        self.result = population_variance(a, b)
        return self.result

    def value(self, a, b):
        self.result = p_value(a, b)
        return self.result

    def prop(self, a, b):
        self.result = proportion(a, b)
        return self.result

    def s_mean(self, a, b):
        self.result = sample_mean(a, b)
        return self.result

    def sample(self, a, b):
        self.result = sample_standard_deviation(a, b)
        return self.result

    def variance1(self, a, b):
        self.result = variance_of_sample_proportion(a, b)
        return self.result