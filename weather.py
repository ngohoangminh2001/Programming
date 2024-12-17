import pandas
import numpy
import matplotlib.pyplot

n_d = 365
days = numpy.arange(1, n_d + 1)

temp = numpy.random.uniform(-1, 30, n_d)
pressure = numpy.random.uniform(1000, 1000, n_d)
humidity = numpy.random.uniform(0, 101, n_d)
rain = numpy.random.randint(2, size=n_d)

weather = pandas.DataFrame({'days': days,
                            'temp': temp,
                            'pressure': pressure,
                            'humidity': humidity,
                            'rain': rain})

print(weather)

print(weather.hist(figsize=(20, 10)))

matplotlib.pyplot.show()