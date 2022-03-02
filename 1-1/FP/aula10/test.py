
from itertools import count


def areaSmaller(countries, A):
    countriesunderarea = [x for x in countries if x[2] < A]
    return countriesunderarea


country = [('Grenada', 'NA', 344.0, 108825),
   ('Kenya', 'AF', 581834.0, 47564296),
   ('Liechtenstein', "EU", 5123.0, 512435)]

print(areaSmaller(country, 6000))