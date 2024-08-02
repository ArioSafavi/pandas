import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('assesment task/world_population.csv')
dataset.plot(
    kind = 'bar',
    x = 'Country/Territory',
    y = 'Growth Rate',
    color = 'blue',
    alpha = 0.3,
    title = 'world population growth rate'
)
plt.show()
