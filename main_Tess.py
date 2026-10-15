# from patient_Tess import *

# # Imports necessary libraries
# import matplotlib.pyplot as plt
# from scipy import stats
# import numpy as np
# import statistics
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# Patient.instantiate_from_csv("C:/Users/tmvit/OneDrive/Desktop/BME 2315/Module 2/BME_2315-Module2/Module2_FSHD_Dataset.csv")

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path("C:/Users/tmvit/OneDrive/Desktop/BME 2315/Module 2/BME_2315-Module2/Module2_FSHD_Dataset.csv")
manifest = pd.read_csv(DATA_DIR / "slice_info.csv")
manifest

row = manifest[manifest["timepoint"] == "TP1"].iloc[3]  # representative mid-muscle slice

water = np.load(DATA_DIR / row["water_file"])
fat = np.load(DATA_DIR / row["fat_file"])
mask = np.load(DATA_DIR / row["mask_file"]).astype(bool)

print("Water image shape:", water.shape)
print("Fat image shape:", fat.shape)
print("Mask shape:", mask.shape)
print("Number of muscle pixels:", mask.sum())