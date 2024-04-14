import pandas as pd
import os
import os.path as path

data_path = "/Users/tychen/workspace/class/jupyter/data"

# ##### option 1:  DOES NOT WORK in Jupyter #####
# df = pd.read_csv("data/data.csv")
# df.close()

# ##### option 2:  DOES NOT WORK in Jupyter #####
# with open("data/data.csv") as f:
#     df = pd.read_csv(f)

# ##### option 3: path.join #####
# data = path.join(data_path, "data.csv")
# with open(data) as f:
#     df = pd.read_csv(f)

# # ##### option 4: change dir #####
os.chdir(data_path)
df = pd.read_csv("data.csv")

# ##### output
print(df.describe())

