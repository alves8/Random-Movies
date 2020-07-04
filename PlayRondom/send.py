# %%
import random
import numpy as np
import pandas as pd

film = 'film.xlsx'
df = pd.read_excel(film) 

#number Of Films



sortition = random.randrange(1001)
selectedMovie = df.loc[sortition, 'title']
print("Let's watch :", selectedMovie)


# %%
