import pandas as pd
import numpy as np


data = pd.DataFrame({"N1":['600','600','600','600','600','600','600'],
                     "V1":['12.3', '12.4', '12.4', '12.4', '12.4', '12.4', '12.3', '12.2'],
                     "N2":['75', '750', '300', '600', '900', '1200', '1800', '3600'],
                     "V3ex":['1.513', '3.056', '6.06', '12.08', '12.13', '24.14','35.9', '72.1']})

print(data)