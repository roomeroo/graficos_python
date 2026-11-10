import pandas as pd
import numpy as np

import matplotlib.pyplot as plt 

titles = pd.read_csv('data/netflix_titles.csv', index_col=0)



#grafico: numero peliculas/series segun año
plt.figure(figsize=(10, 6))
plt.bar(titles['release_year'].value_counts(), titles['release_year'].value_counts())

plt.show()