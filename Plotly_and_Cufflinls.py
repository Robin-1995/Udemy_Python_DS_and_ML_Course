# plotly is an interactive visualisation library
# Cufflinks is used to connect plotly with pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)
cf.go_online()

# Data definition
df = pd.DataFrame(np.random.rand(100,4), columns = ["A", "B", "C", "D"]) #100 rows of 4 columns, randomly distributed numbers
df2 = pd.DataFrame({"Category":["A","B","C"], "values":[32,43,50]})

df.iplot()
plt.show()