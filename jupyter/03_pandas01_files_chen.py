import pandas as pd
import os
import os.path as path
# print (os.path.expanduser('~'))
HOME = (os.path.expanduser('~'))    ### give us ~, the home directory
print("HOMMMMMMMMMMM", HOME)

data_path = HOME + '/workspace/class/jupyter/data'
print("WWWWWWWWWWWWW", data_path)

# ##### option 1:  ##### works in mac 
# df = pd.read_csv(data_path+"/data.csv")
# df.close()

# ##### option 2:  ##### works in mac 
# with open(data_path+"/data.csv") as f:
#     df = pd.read_csv(f)

# ##### option 3: path.join ##### works in mac
# data = path.join(data_path, "data.csv")
# with open(data) as f:
#     df = pd.read_csv(f)

##### option 4: change dir #####
# ##### option 3: path.join ##### works in Windows 11/macOS
# data = path.join(data_path, "data.csv")
# with open(data) as f:
#     df = pd.read_csv(f)

##### option 5: change dir ##### works in Windows 11/macOS
# os.chdir(data_path)
# df = pd.read_csv("data.csv")

# ##### output
print(df.describe())

