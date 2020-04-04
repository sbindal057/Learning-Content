# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:41:28 2020

@author: Shweta Bindal
"""


import pandas as pd
import numpy as np
xlsx_path = "C:/Users/Shweta Bindal/Desktop/Book1.xlsx"
df = pd.read_excel(xlsx_path)
xyz = np.array(df)
print(xyz)