import pandas as pd
import numpy as np
data = pd.read_csv("crakaar.csv")
# print(data)

data = pd.read_csv("crakaar.csv")
df =data.sort_values(by=['Score'], ascending=False)
# print(df)
# print(data)
# CRID = "AK220004"

# rank_list = np.array(data['CRID']==CRID)

# rank = -1
# for i in range(len(rank_list)):
#     if rank_list[i]:
#         rank = i+1
#         break


